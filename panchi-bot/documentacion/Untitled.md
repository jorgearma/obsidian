  Flujo: usuario sin registrar envía un mensaje                                                                           
                                                                                                                          
  0. Entrada HTTP → RQ (asíncrono)                                                                                        
                                                                                                                          
  WhatsApp (Twilio o Meta) → POST /webhook o /webhook/meta        
                                                                                                                          
  El blueprint valida la firma HMAC del proveedor. Si es válida, llama a encolar_mensaje() y devuelve 200 inmediatamente —
   el webhook no espera el procesamiento.                                                                                 
                                                                                                                          
  El worker RQ ejecuta _job_procesar_mensaje() en background, que llama a enrutar_mensaje().                              
   
  ▎ Duplicados Meta: si el mensaje tiene wamid y ya está en Redis como procesado, se descarta antes de encolar.           
                                                                  
  ---                                                                                                                     
  1. enrutar_mensaje() — ¿registrado o no?                        
                                                                                                                          
  # inbound_whatsapp.py:118-136
                                                                                                                          
  1. Anti-spam: si el número está bloqueado en Redis (bloqueo:<phone>, TTL 4s) → 403, no procesa.                         
  2. Bloquea el número durante 4s para evitar flood.
  3. Consulta DB: gestor_usuarios.verificar_usuario(numero).                                                              
    - Si da error de DB → envía mensaje de error al usuario, devuelve 500.                                                
  4. Si no está en DB → llama a manejar_registro().                                                                       
                                                                                                                          
  ---                                                                                                                     
  2. Máquina de estados de registro (Redis)                                                                               
                                                                                                                          
  El estado vive en Redis con clave = número de teléfono. Si no existe la clave, obtener_estado() devuelve {"estado": 
  "saludo_inicial"} como default.                                                                                         
                                                                  
  ---                                                                                                                     
  Estado SALUDO_INICIAL (cualquier primer mensaje)                
                                                                                                                          
  # controllers/registro.py:78-81
                                                                                                                          
  - Envía mensaje de bienvenida (_enviar_bienvenida)                                                                      
  - Transición: SALUDO_INICIAL → ESPERANDO_CONFIRMACION                                                                   
  - No importa qué diga el usuario — el primer mensaje siempre dispara esto.                                              
                                                                                                                          
  ---
  Estado ESPERANDO_CONFIRMACION                                                                                           
                                                                  
  # controllers/registro.py:83-92
                                                                                                                          
  El bot preguntó "¿quieres registrarte?". Dos caminos:                                                                   
                                                                                                                          
  ┌────────────────────────────┬──────────────────────────────────────────────────────────────────────────────────────┐   
  │    Mensaje del usuario     │                                        Acción                                        │
  ├────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
  │ "si", "sí", "quiero",      │ Pide nombre → ESPERANDO_NOMBRE                                                       │
  │ "adelante"                 │                                                                                      │
  ├────────────────────────────┼──────────────────────────────────────────────────────────────────────────────────────┤   
  │ cualquier otra cosa        │ Borra clave Redis, envía mensaje de despedida. Fin del registro (puede reiniciarlo   │   
  │                            │ mandando otro mensaje).                                                              │   
  └────────────────────────────┴──────────────────────────────────────────────────────────────────────────────────────┘   
                                                                  
  ---
  Estado ESPERANDO_NOMBRE

  # controllers/registro.py:94-103

  El bot pidió el nombre completo. Se valida con regex (_es_nombre_valido): solo letras, espacios, apóstrofos, guiones;   
  entre 2 y 60 chars.
                                                                                                                          
  ┌─────────────────┬─────────────────────────────────────────────────────────────────┐
  │    Resultado    │                             Acción                              │
  ├─────────────────┼─────────────────────────────────────────────────────────────────┤
  │ Nombre válido   │ Guarda nombre en Redis → ESPERANDO_DIRECCION                    │
  ├─────────────────┼─────────────────────────────────────────────────────────────────┤
  │ Nombre inválido │ Envía error, permanece en ESPERANDO_NOMBRE (sin cambiar estado) │                                   
  └─────────────────┴─────────────────────────────────────────────────────────────────┘                                   
                                                                                                                          
  ---                                                                                                                     
  Estado ESPERANDO_DIRECCION                                      

  # controllers/registro.py:105-123

  El bot pidió la dirección. Se llama a validar_direccion() del maps_module (311 calles + Google Maps + polígono de zona).
   
  ┌───────────┬─────────────────┬──────────────────────────────────────────────────────────────────────────────────────┐  
  │ Resultado │     Motivo      │                                        Acción                                        │
  ├───────────┼─────────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
  │ Válida    │ —               │ Guarda dirección en Redis → CONFIRMANDO_DIRECCION                                    │
  ├───────────┼─────────────────┼──────────────────────────────────────────────────────────────────────────────────────┤
  │ Inválida  │ "fuera_de_zona" │ Envía error sin sugerencia, permanece en ESPERANDO_DIRECCION                         │  
  ├───────────┼─────────────────┼──────────────────────────────────────────────────────────────────────────────────────┤  
  │ Inválida  │ cualquier otro  │ Intenta sugerir_calle() → envía error con/sin sugerencia, permanece en               │  
  │           │                 │ ESPERANDO_DIRECCION                                                                  │  
  └───────────┴─────────────────┴──────────────────────────────────────────────────────────────────────────────────────┘
                                                                                                                          
  ▎ Si sugerir_calle() lanza excepción, se captura y se continúa sin sugerencia.                                          
   
  ---                                                                                                                     
  Estado CONFIRMANDO_DIRECCION                                    
                                                                                                                          
  # controllers/registro.py:125-135
                                                                                                                          
  El bot mostró la dirección normalizada y pregunta "¿es correcta?".                                                      
   
  ┌──────────────────────────┬───────────────────────────────────────────────────────────────┐                            
  │         Mensaje          │                            Acción                             │
  ├──────────────────────────┼───────────────────────────────────────────────────────────────┤
  │ nada de "si", "sí", "no" │ Pide que responda sí o no, permanece en CONFIRMANDO_DIRECCION │
  ├──────────────────────────┼───────────────────────────────────────────────────────────────┤
  │ "no"                     │ Rollback → ESPERANDO_DIRECCION, pide dirección de nuevo       │                            
  ├──────────────────────────┼───────────────────────────────────────────────────────────────┤                            
  │ "si" / "sí"              │ Llama a _confirmar_direccion()                                │                            
  └──────────────────────────┴───────────────────────────────────────────────────────────────┘                            
                                                                  
  ---                                                                                                                     
  _confirmar_direccion() — escritura final                        

  # controllers/registro.py:41-70
                                                                                                                          
  1. Guardia idempotencia: si el usuario ya existe en DB (reintento Meta), borra Redis y retorna 200. No crea duplicado.  
  2. gestor_usuarios.guardar_usuario() → escribe en DB.                                                                   
  3. gestor_pedidos.iniciar_pedido() → crea el primer pedido en estado PENDIENTE.                                         
  4. Envía mensaje de bienvenida con el menú de opciones.                                                                 
  5. Borra la clave de Redis — limpieza de estado fantasma.
                                                                                                                          
  Si la DB falla en el paso 2 o 3, se captura la excepción, se loguea el error y se devuelve 200 (para que Meta no        
  reintente). El estado Redis no se limpia en este caso de error.                                                         
                                                                                                                          
  ---                                                             
  Diagrama de estados
                                                                                                                          
  (primer mensaje)
        ↓                                                                                                                 
  SALUDO_INICIAL ──────────────────→ ESPERANDO_CONFIRMACION       
                                            │                                                                             
                            "si/quiero" ←──┤──→ otro: borrar Redis, fin
                                            ↓                                                                             
                                     ESPERANDO_NOMBRE             
                                            │                                                                             
                            válido ←────────┤──→ inválido: quedar aquí
                                            ↓                                                                             
                                     ESPERANDO_DIRECCION ←──────────────┐
                                            │                            │                                                
                            válida ←────────┤──→ inválida: quedar aquí  │
                                            ↓                            │                                                
                                     CONFIRMANDO_DIRECCION               │
                                            │                            │                                                
                             "si" ←─────────┤──→ "no": rollback ────────┘
                                            ↓                                                                             
                                     [escribe DB + borra Redis]                                                           
                                     → usuario pasa a flujo registrado               