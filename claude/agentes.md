┌────────────┐
│  Usuario   │
└─────┬──────┘
      │
      v
┌──────────────────────────┐
│ 1. Request Normalizer    │
│ - mejora prompt          │
│ - mete spec/contexto     │
│ - detecta dudas          │
│ - hace preguntas         │
└─────┬────────────────────┘
      │
      v
┌──────────────────────────┐
│ normalized-request.json  │
└─────┬────────────────────┘
      │
      v
┌──────────────────────────┐
│ 2. Sense Checker         │
│ - valida si tiene sentido│
│ - detecta riesgos        │
│ - no planifica           │
└─────┬───────────┬────────┘
      │           │
      │ ok        │ falta info / riesgo grave
      │           │
      v           v
┌──────────────────────┐   ┌──────────────────────┐
│ validated-request    │   │ preguntas / invalid  │
│ .json                │   │ / warning            │
└─────┬────────────────┘   └──────────────────────┘
      │
      v
┌──────────────────────────┐
│ 3. Router                │
│ - decide readers         │
│ - usa maps/reglas        │
└─────┬────────────────────┘
      │
      v
┌──────────────────────────┐
│ selected-readers.json    │
└─────┬────────────────────┘
      │
      v
┌──────────────┬──────────────┬──────────────┬──────────────┐
│ API Reader   │ DB Reader    │ UI Reader    │ Query Reader │
│ Services ... │ Jobs ...     │ Project ...  │ etc.         │
└─────┬────────┴───────┬──────┴───────┬──────┴───────┬──────┘
      │                │              │              │
      └────────────────┴──────────────┴──────────────┘
                       │
                       v
┌──────────────────────────┐
│ reader-context.json      │
│ - files_to_open          │
│ - files_to_review        │
│ - key_symbols            │
│ - riesgos/contexto       │
└─────┬────────────────────┘
      │
      v
┌──────────────────────────┐
│ 4. Planner               │
│ - abre código real       │
│ - verifica readers       │
│ - lee secciones justas   │
│ - arma plan real         │
└─────┬────────────────────┘
      │
      v
┌──────────────────────────┐
│ plan.json                │
└─────┬────────────────────┘
      │
      v
┌──────────────────────────┐
│ 5. Writer                │
│ - convierte a handoff    │
│ - reparte por agentes    │
└─────┬────────────────────┘
      │
      v
┌──────────────────────────┐
│ execution-brief.json     │
└─────┬────────────────────┘
      │
      v
┌──────────────────────────┐
│ 6. Plan Reviewer         │
│ - detecta huecos         │
│ - contradicciones        │
│ - depends_on             │
│ - riesgos sin cubrir     │
└─────┬────────────────────┘
      │
      v
┌──────────────────────────┐
│ plan aprobado            │
│ listo para ejecución     │
└──────────────────────────┘
