1. Copia la carpeta al proyecto destino
  cp -r /home/siemprearmando/agentes/losgretis/claude/ /tu/proyecto/.claude/

  2. Rellena los mapas con contexto real del proyecto

  Edita estos 4 archivos con la informacion de tu proyecto:
  - .claude/maps/PROJECT_MAP.md — arquitectura, modulos, entry points
  - .claude/maps/DB_MAP.md — tablas, relaciones, modelos
  - .claude/maps/QUERY_MAP.md — queries importantes, acceso a datos
  - .claude/maps/UI_MAP.md — vistas, componentes, rutas

  3. Valida la estructura
  python3 .claude/hooks/pre-commit.py
  Esperado: Claude plugin structure ok

  Como usarlo en Claude Code

  Una vez instalado, el flujo es:

  4. Abres Claude Code en el proyecto
  5. Describes tu tarea al agente reader (el entry point)
  6. El pipeline corre: Reader → Planner → Writer → [tu aprobacion] → Frontend/Backend → Reviewer
  7. Antes de ejecutar, apruebas el plan:
  python3 .claude/hooks/approve-plan.py approve --by "tu-nombre"
  8. Luego ejecutas:
  python3 .claude/hooks/execute-plan.py

  Requisito clave

  Los mapas *_MAP.md son lo mas importante. Sin contexto real del proyecto, los readers no pueden hacer su
  trabajo. Cuanto mas detallados, mejor sera el plan generado.