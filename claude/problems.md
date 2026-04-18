Entonces el reader podría extraer:

- `blueprints/dashboard.py` → `files_to_open` o `files_to_review`
- `["rendimiento", "estadisticas"]` → `key_symbols`
- Y el planner recibiría todo sin adivinanzas

**Sí, el problema es el mapeo inicial.** El analizador de API (`claude/hooks/analyzers/`) no está detectando los blueprints de Flask. Eso es lo que hay que arreglar.