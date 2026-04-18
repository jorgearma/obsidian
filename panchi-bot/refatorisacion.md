3. Flujo principal de ejecución

  WhatsApp msg
      │
      ▼
  /webhook
      │
      ├─ Bloqueado en Redis? → 403 y fin
      │
      ├─ ¿existe en DB?
      │    │
      │    NO → manejar_registro()       [controllers/no_resgistrados.py]
      │         Lee estado desde Redis
      │         saludo → confirmacion → nombre (spaCy) → direccion (Maps) → confirmando
      │         Al final: guardar_usuario() + iniciar_pedido()
      │
      │    SÍ → ManejadorMensajesRegistrados.manejar_mensajes_registrados()
      │         [controllers/mensajes_registrados.py]
      │
      │         Lee estado del pedido más reciente
      │         ├─ "Pendiente" → procesar_pedido() [menu.py]
      │         │    opción "1" → generar_enlace() → token en Redis
      │         │                  actualizar estado DB → "enlace"
      │         │                  enviar link por WhatsApp
      │         │
      │         ├─ "enlace"/"enlace2" → reenviar link guardado en DB
      │         └─ "confirmando-pago" → reenviar URL de pago Monei
      │
      ▼
  Cliente abre /menu/<token>
      │
      ├─ Lee datos de Redis con token
      ├─ Valida estado del pedido en DB ("enlace")
      └─ Renderiza quiniela.html
           │
           AJAX POST /api/confirmacion
                → guarda carrito en Redis (UUID)
                → actualiza pedido → "enlace2"
                → redirige a /confirmacion_pago
                     │
                     AJAX POST /api/agregar_pedido
                          → valida precios contra DB
                          → guarda detalles en pedido_detalles
                          → crea pago en Monei
                          → actualiza pedido → "confirmando-pago"
                          → redirige a URL de Monei

  Monei llama POST /webhoo/monei
      → actualiza pedido → "pagado"
      → envía WhatsApp de confirmación al cliente


4. Dependencias externas críticas

  Servicio: SQL Server
  Uso: Toda la persistencia
  Hardcodeado: Sí (database.py:38-63)
  Fallo =: App no arranca — conectar_bd1() se llama al importar
  ────────────────────────────────────────
  Servicio: Redis
  Uso: Estado de registro, tokens, rate-limit
  Hardcodeado: No (localhost:6379)
  Fallo =: App no arranca — redismanager = RedisManager() al importar gestor_redis.py
  ────────────────────────────────────────
  Servicio: Twilio
  Uso: Enviar y recibir WhatsApp
  Hardcodeado: Sí (utils/mensajes.py:10-12)
  Fallo =: No se pueden enviar mensajes; webhook sigue funcionando
  ────────────────────────────────────────
  Servicio: Monei
  Uso: Pagos
  Hardcodeado: Sí (main.py:40)
  Fallo =: /api/agregar_pedido falla; flujo de pago roto
  ────────────────────────────────────────
  Servicio: ngrok URL
  Uso: Links de menú y pago
  Hardcodeado: Sí (3 sitios)
  Fallo =: Links enviados a usuarios no funcionan al cambiar túnel
  ────────────────────────────────────────
  Servicio: spaCy es_core_news_sm
  Uso: Validar nombres en registro
  Hardcodeado: No (modelo local)
  Fallo =: Registro bloqueado si el modelo no está instalado
  ────────────────────────────────────────
  Servicio: Google Maps API
  Uso: Validar direcciones
  Hardcodeado: Implícito en utils/maps.py
  Fallo =: Registro bloqueado si falla

  ---
  5. Módulos más acoplados

  El nodo más crítico: main.py

  main.py hace demasiado: define todas las rutas, instancia todos los servicios globales
  (gestor_pedidos, gestor_usuarios, gestor_productos, cache, monei), y los demás módulos
  importan de vuelta desde él:

  # controllers/mensajes_registrados.py:15-16
  from main import gestor_pedidos
  from main import gestor_usuarios

  # managers/gestor_usuarios.py:102
  from main import gestor_pedidos

  # menu.py:50
  from main import gestor_pedidos

  Esto crea importaciones circulares reales resueltas solo porque Python las difiere al
  interior de funciones. Si alguno de esos imports se mueve al nivel de módulo, la app se
  rompe.

  Segundo problema: db_session global compartido

  database.py:78 crea una única SessionLocal() que es compartida por todos los managers. No
  hay manejo de sesiones por request — cualquier error no-capturado puede dejar la sesión en
   estado corrupto para todas las peticiones siguientes.

  Tercer problema: gestor_redis.py:128 instancia redismanager al importar

  redismanager = RedisManager() se ejecuta en tiempo de import. Si Redis no está disponible,
   la app explota antes de arrancar, sin posibilidad de degradación controlada.

  ---
  6. Riesgos para refactorizar

  ┌──────────────────────┬───────────┬──────────────────────────────────────────────────┐
  │        Riesgo        │ Severidad │                      Causa                       │
  ├──────────────────────┼───────────┼──────────────────────────────────────────────────┤
  │ Romper las           │           │ from main import X en 3+ archivos — mover        │
  │ importaciones        │ 🔴 Alto   │ instancias sin cuidado rompe todo                │
  │ circulares           │           │                                                  │
  ├──────────────────────┼───────────┼──────────────────────────────────────────────────┤
  │ Sesión SQLAlchemy    │ 🔴 Alto   │ Un rollback parcial puede corromper el estado de │
  │ compartida           │           │  otra petición concurrente                       │
  ├──────────────────────┼───────────┼──────────────────────────────────────────────────┤
  │ URL de ngrok         │           │ crear_token.py:30, main.py:204, main.py:330 —    │
  │ hardcodeada en 3     │ 🟡 Medio  │ fácil de cambiar pero fácil de olvidar uno       │
  │ sitios               │           │                                                  │
  ├──────────────────────┼───────────┼──────────────────────────────────────────────────┤
  │ Estado de pedido     │           │ obtener_pedido_mas_reciente devuelve el último   │
  │ "más reciente" sin   │ 🟡 Medio  │ pedido sin importar su estado — un pedido        │
  │ filtro               │           │ "pagado" puede bloquear nuevos pedidos           │
  ├──────────────────────┼───────────┼──────────────────────────────────────────────────┤
  │                      │           │ redismanager.set(token, ...) en                  │
  │ Tokens sin TTL       │ 🟡 Medio  │ crear_token.py:24 no pasa ex= — los tokens de    │
  │                      │           │ menú nunca expiran                               │
  ├──────────────────────┼───────────┼──────────────────────────────────────────────────┤
  │ Typo en ruta         │ 🟡 Medio  │ Si se corrige, hay que actualizar la URL en el   │
  │ /webhoo/monei        │           │ panel de Monei antes de desplegar                │
  ├──────────────────────┼───────────┼──────────────────────────────────────────────────┤
  │ estado_usuarios en   │           │ data/estado_usuarios.py — diccionario en         │
  │ memoria              │ 🟡 Medio  │ proceso, se pierde al reiniciar; actualmente     │
  │                      │           │ solo se usa para recien_registrado               │
  ├──────────────────────┼───────────┼──────────────────────────────────────────────────┤
  │ Tests con            │ 🟡 Medio  │ Sin mocks de DB/Redis, los tests requieren       │
  │ dependencias reales  │           │ infraestructura levantada                        │
  └──────────────────────┴───────────┴──────────────────────────────────────────────────┘

  ---
  7. Plan por fases (menor → mayor riesgo)

  Fase 1 — Configuración (riesgo: ninguno)

  Extraer credenciales y URLs a .env y leerlas con os.environ.get():
  - utils/mensajes.py:10-12 → TWILIO_*
  - main.py:40 → MONEI_API_KEY
  - database.py:38-63 → DB_*
  - crear_token.py:30, main.py:204, main.py:330 → PUBLIC_URL

  Sin cambios de lógica. Verificable corriendo la app.

  ---
  Fase 2 — Fixes de bajo riesgo (riesgo: bajo)

  - Añadir TTL a tokens de menú en crear_token.py:24 (ex=86400)
  - Corregir typo /webhoo/monei (coordinado con el panel de Monei)
  - Filtrar obtener_pedido_mas_reciente para excluir pedidos en estado "pagado"
  (data/order.py:57)
  - Eliminar data/estado_usuarios.py y el uso de recien_registrado en gestor_usuarios.py:111
   (el estado ya está en Redis)

  ---
  Fase 3 — Sesión de base de datos (riesgo: medio)

  Reemplazar la db_session global por una sesión por request usando g de Flask o un context
  manager. Esto requiere actualizar GestorPedidos, GestorUsuariosBD, y ProductoManager. La
  firma de los constructores cambia pero la lógica no.

  ---
  Fase 4 — Romper el acoplamiento circular (riesgo: alto)

  Crear un módulo de contenedor de dependencias (o usar Flask app.extensions) donde vivían
  las instancias globales. Así mensajes_registrados.py, gestor_usuarios.py y menu.py dejan
  de importar de main.

  Este paso requiere pruebas exhaustivas porque toca la cadena de importación completa.

  ---
  Fase 5 — Separar responsabilidades de main.py (riesgo: alto)

  Mover las rutas a blueprints:
  - blueprint_webhook → /webhook, /webhoo/monei
  - blueprint_menu → /menu/<token>, /confirmacion_pago, /pago_confirmado
  - blueprint_api → /api/*

  Hacer esto antes de la Fase 4 agrava el acoplamiento circular; hacerlo después es más
  seguro.











  7. Plan por fases (menor → mayor riesgo)

  Fase 1 — Configuración (riesgo: ninguno)

  Extraer credenciales y URLs a .env y leerlas con os.environ.get():
  - utils/mensajes.py:10-12 → TWILIO_*
  - main.py:40 → MONEI_API_KEY
  - database.py:38-63 → DB_*
  - crear_token.py:30, main.py:204, main.py:330 → PUBLIC_URL

  Sin cambios de lógica. Verificable corriendo la app.

  ---
  Fase 2 — Fixes de bajo riesgo (riesgo: bajo)

  - Añadir TTL a tokens de menú en crear_token.py:24 (ex=86400)
  - Corregir typo /webhoo/monei (coordinado con el panel de Monei)
  - Filtrar obtener_pedido_mas_reciente para excluir pedidos en estado "pagado"
  (data/order.py:57)
  - Eliminar data/estado_usuarios.py y el uso de recien_registrado en gestor_usuarios.py:111
   (el estado ya está en Redis)

  ---
  Fase 3 — Sesión de base de datos (riesgo: medio)

  Reemplazar la db_session global por una sesión por request usando g de Flask o un context
  manager. Esto requiere actualizar GestorPedidos, GestorUsuariosBD, y ProductoManager. La
  firma de los constructores cambia pero la lógica no.

  ---
  Fase 4 — Romper el acoplamiento circular (riesgo: alto)

  Crear un módulo de contenedor de dependencias (o usar Flask app.extensions) donde vivían
  las instancias globales. Así mensajes_registrados.py, gestor_usuarios.py y menu.py dejan
  de importar de main.

  Este paso requiere pruebas exhaustivas porque toca la cadena de importación completa.

  ---
  Fase 5 — Separar responsabilidades de main.py (riesgo: alto)

  Mover las rutas a blueprints:
  - blueprint_webhook → /webhook, /webhoo/monei
  - blueprint_menu → /menu/<token>, /confirmacion_pago, /pago_confirmado
  - blueprint_api → /api/*

  Hacer esto antes de la Fase 4 agrava el acoplamiento circular; hacerlo después es más
  seguro.
