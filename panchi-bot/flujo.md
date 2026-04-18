LOGIN
  |
  v
¿qué tipo de usuario entra?
  |
  +--> EMPLEADO OPERATIVO
  |       |
  |       v
  |   ¿ya fichó / tiene rol activo?
  |       |
  |       +--> NO
  |       |      |
  |       |      v
  |       |   CHECK-IN / SELECCIÓN DE ACCIÓN
  |       |      |
  |       |      +--> Entrar como Picker
  |       |      +--> Entrar como Repartidor
  |       |      +--> Ver turno de hoy
  |       |
  |       +--> SÍ
  |              |
  |              v
  |         HUB DE EMPLEADO
  |              |
  |              +--> Ir a Picking
  |              +--> Ir a Reparto
  |              +--> Ver mis métricas
  |              +--> Cambiar de rol
  |              +--> Cerrar turno
  |
  +--> ADMIN / MANAGER
          |
          v
      DASHBOARD PRINCIPAL
          |
          +--> Monitor de operación
          +--> Dashboard de métricas
          +--> Control de empleados


# distribucion de pantallas

1. LOGIN
   |
   +--> acceso único para todos

2. ZONA EMPLEADO
   |
   +--> Check-in
   |     - iniciar turno
   |     - elegir cómo entra hoy
   |
   +--> Hub empleado
   |     - resumen personal
   |     - botones de acción
   |
   +--> Modo Picker
   |     - preparar pedidos
   |
   +--> Modo Repartidor
   |     - repartir pedidos
   |
   +--> Mis métricas
         - rendimiento del día
