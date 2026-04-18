## Cómo sería el flujo ideal

### Caso: “quiero cambiar la lógica de reparto”

**Paso 1 — planner**  
Pregunta al agente de contexto:

- qué flujo afecta
- qué estados toca
- qué endpoints toca
- qué tablas toca
- qué pantallas toca

**Paso 2 — planner**  
Genera un plan:

- backend primero
- luego API
- luego UI
- luego tests

**Paso 3 — implementador backend**  
Hace solo backend

**Paso 4 — implementador frontend**  
Hace solo frontend

**Paso 5 — reviewer**  
Comprueba que el cambio respeta el plan

Ese flujo sí es muy razonable.



task.md
  ↓
READER
  ├─ PROJECT_SUBREADER
  ├─ DB_SUBREADER
  ├─ FLOW_SUBREADER
  ├─ STATE_SUBREADER
  ├─ API_SUBREADER
  └─ UI_SUBREADER
  ↓
reader_report.md
  ↓
PLANNER
  ├─ BACKEND_SCOPE_SUBPLANNER
  ├─ FRONTEND_SCOPE_SUBPLANNER
  ├─ DB_SCOPE_SUBPLANNER
  └─ RISK_SUBPLANNER
  ↓
plan.md
  ↓
IMPLEMENTER
  ↓
AUDITOR
  ├─ SCOPE_AUDITOR
  ├─ DB_CHANGE_AUDITOR
  ├─ API_CHANGE_AUDITOR
  └─ UI_CHANGE_AUDITOR
  ↓
audit_report.md