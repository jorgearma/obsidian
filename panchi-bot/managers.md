 Estructura general

  managers/ es la capa de acceso a datos y lógica de negocio. Está entre los blueprints (rutas HTTP) y la base
  de datos/Redis. Ningún blueprint debe hablar directamente con la DB — siempre pasa por un manager.

  El patrón usado es Composite Manager: cada gestor público (gestor_*.py) es un ensamblador delgado que hereda
  de varios mixins. La lógica real vive en los mixins.

  ---
  Archivos planos (raíz de managers/)

  ┌─────────────────────┬─────────────────────────────────────────────────────────┐
  │       Archivo       │                        Qué hace                         │
  ├─────────────────────┼─────────────────────────────────────────────────────────┤
  │ gestor_redis.py     │ Acceso a Redis: estados de registro, bloqueos anti-spam │
  ├─────────────────────┼─────────────────────────────────────────────────────────┤
  │ gestor_usuarios.py  │ CRUD de usuarios/clientes en BD                         │
  ├─────────────────────┼─────────────────────────────────────────────────────────┤
  │ gestor_productos.py │ Catálogo, precios, stock de productos                   │
  ├─────────────────────┼─────────────────────────────────────────────────────────┤
  │ estado_usuario.py   │ Máquina de estados de registro (Redis-backed)           │
  └─────────────────────┴─────────────────────────────────────────────────────────┘

  ---
  managers/pedidos/ → gestor_pedidos.py

  El flujo de vida completo de un pedido.

  ┌────────────────────┬───────────────────────────────────────────────────────────────────────────┐
  │       Mixin        │                              Responsabilidad                              │
  ├────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ lifecycle_mixin.py │ Crear pedido, agregar productos, confirmar pago (online/efectivo)         │
  ├────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ workflow_mixin.py  │ Cambios de estado, guardar carrito, coordenadas, procesar pago confirmado │
  ├────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ items_mixin.py     │ Cancelar pedido, eliminar/sustituir ítems individuales                    │
  └────────────────────┴───────────────────────────────────────────────────────────────────────────┘

  ---
  managers/dashboard/ → gestor_dashboard.py

  La vista de operaciones del dashboard (operadores, picking, reparto).

  ┌──────────────────────────────┬───────────────────────────────────────────────────────────────────────────┐
  │            Mixin             │                              Responsabilidad                              │
  ├──────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ gestor_pedidos_mixin.py      │ Métricas, pedidos activos, alertas, historial, detalle                    │
  ├──────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ picking_flujo.py             │ Asignar/reasignar picker, completar picking, actualizar ítem (modo        │
  │                              │ warehouse)                                                                │
  ├──────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ picking_basico.py            │ Cola de cocina simplificada (modo restaurant)                             │
  ├──────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ reparto_asignacion.py        │ Asignar repartidor, repartos sin asignar, reclamar reparto                │
  ├──────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ reparto_tracking.py          │ Mapa, marcar salida/entregado/no-entregado                                │
  ├──────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ reparto_cobro.py             │ Registrar cobro, cierre de caja del repartidor                            │
  ├──────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ empleados_lista.py           │ Lista de empleados disponibles por rol/turno                              │
  ├──────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ empleados_monitor.py         │ Monitor en tiempo real de empleados activos                               │
  ├──────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ empleados_rendimiento.py     │ Resumen y detalle de rendimiento por empleado                             │
  ├──────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ gestor_estadisticas_mixin.py │ Estadísticas históricas por rango de fechas                               │
  ├──────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤
  │ gestor_turnos_mixin.py       │ (existe pero sin métodos públicos aún)                                    │
  ├──────────────────────────────┼───────────────────────────────────────────────────────────────────────────┤  
  │ jobs.py                      │ Función RQ para descontar stock tras picking                              │
  └──────────────────────────────┴───────────────────────────────────────────────────────────────────────────┘  
                                                                  
  ---                                                                                                           
  managers/empleado/ → gestor_empleado.py                         
                                         
  Todo lo relacionado con el empleado individualmente (no desde el dashboard del operador).
                                                                                                                
  ┌────────────────────────┬──────────────────────────────────────────────────────────────────────┐
  │         Mixin          │                           Responsabilidad                            │             
  ├────────────────────────┼──────────────────────────────────────────────────────────────────────┤
  │ checkin_mixin.py       │ Iniciar/cerrar turno, fichar entrada/salida, resumen del día         │
  ├────────────────────────┼──────────────────────────────────────────────────────────────────────┤
  │ turnos_mixin.py        │ Turno de hoy, próximos turnos, historial, planificación, crear turno │             
  ├────────────────────────┼──────────────────────────────────────────────────────────────────────┤             
  │ metricas_mixin.py      │ Carga operativa, métricas diarias, puntualidad, ausencias            │             
  ├────────────────────────┼──────────────────────────────────────────────────────────────────────┤             
  │ profile_roles_mixin.py │ Perfil, cambiar estado/rol, capacidades, rol activo                  │
  └────────────────────────┴──────────────────────────────────────────────────────────────────────┘             
                                                                  
  ---                                                                                                           
  managers/metricas/ → gestor_metricas.py                         
                                                                                                                
  Analytics e indicadores, separados del dashboard operativo.
                                                                                                                
  ┌──────────────────────┬────────────────────────────────────────────────────────────────────────────────┐     
  │        Mixin         │                                Responsabilidad                                 │
  ├──────────────────────┼────────────────────────────────────────────────────────────────────────────────┤     
  │ tiempo_real_mixin.py │ Resumen operación, colas en vivo, alertas, asistencia hoy                      │
  ├──────────────────────┼────────────────────────────────────────────────────────────────────────────────┤
  │ analitica_mixin.py   │ Métricas de pedidos/picking/reparto/incidencias por periodo                    │     
  ├──────────────────────┼────────────────────────────────────────────────────────────────────────────────┤     
  │ empleados_mixin.py   │ Rendimiento comparativo de empleados, ficha individual, asistencia por periodo │     
  └──────────────────────┴────────────────────────────────────────────────────────────────────────────────┘     
                                                                  
  ---
  Relación con el resto del proyecto
                                                                                                                
  blueprints/  →  container.py (singletons)  →  gestor_*.py  →  mixins  →  models.py / Redis
                                                                                                                
  - Los blueprints importan de container.py, nunca instancian managers directamente.                            
  - Los mixins son los únicos que abren sesiones de DB o tocan Redis.                                           
  - Si hay que añadir lógica nueva a un gestor, va al mixin correspondiente, no al ensamblador.                 
                                                                                                 