  🔴 Problema 1: Duplicación de lógica de turnos en dos lugares

  La responsabilidad de gestión de turnos está dividida:

  - managers/empleado/turnos_mixin.py → Consultas (turno_hoy, puede_iniciar_turno)
  - managers/dashboard/gestor_turnos_mixin.py → CRUD (crear_turno, editar_turno, cancelar_turno)

  Ambos tienen lógica similar. Por ejemplo:
  - Ambos calculan ventanas de fichaje
  - Ambos buscan turnos del día
  - gestor_dashboard.turnos_hoy() (línea 15) duplica lógica que debería estar en gestor_empleado

  Solución: Todo lo de turnos debería vivir en GestorEmpleado. El dashboard solo debería consultar turnos, no crear/editar.

  ---
  🟡 Problema 2: GestorTurnosMixin tiene responsabilidades del dashboard que no debería tener

  managers/dashboard/gestor_turnos_mixin.py contiene:
  - ✅ turnos_hoy() — Aquí va bien (es información del dashboard)
  - ❌ crear_turno(), editar_turno(), cancelar_turno(), eliminar_turno() — Estas NO son del dashboard, son operaciones sobre empleados

  Problema: Si otro componente necesita crear un turno (e.g., API rest para empleados), tendría que importar gestor_dashboard, que es confuso.

  Solución: Mover CRUD de turnos a managers/empleado/turnos_mixin.py.

  ---
  🟡 Problema 3: Validación de solapamiento de turnos está en el lugar equivocado

  En managers/dashboard/gestor_turnos_mixin.py:crear_turno() (línea 324), agregas validación de solapamiento. Está bien el validar, pero debe estar en GestorEmpleado donde vive la lógica de
  turnos.









