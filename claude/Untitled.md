# 🧠 0. Setup inicial (antes de tocar código)

### Crear estructura mínima

project/  
├── CLAUDE.md  
├── docs/  
├── src/  
├── tests/

### CLAUDE.md (clave)

Define:

- qué hace el proyecto
    
- stack
    
- reglas (ej: TDD obligatorio)
    
- estilo de código
    

Ejemplo mínimo:

Project: Delivery system backend  
  
Stack:  
- Python / Flask  
- SQL Server  
  
Rules:  
- Always write tests first  
- Do not implement without a plan  
- Prefer simple solutions

👉 Esto es lo que “alinea” a Claude

---

# 🚀 1. Entrar al proyecto (inicio real)

### Comando:

/superpowers:brainstorm

### Qué haces tú:

- explicas la idea general
    

Ejemplo:

Quiero un sistema de pedidos con picker y repartidor,  
con dashboard en tiempo real y lógica de rutas

### Qué hace Claude:

- hace preguntas
    
- detecta problemas
    
- propone arquitectura
    

👉 NO se escribe código aún

---

# 🧩 2. Definir arquitectura

### Comando:

/superpowers:write-plan

### Resultado:

Claude genera algo como:

- módulos:
    
    - pedidos
        
    - usuarios
        
    - rutas
        
- endpoints
    
- base de datos
    
- flujo del sistema
    

👉 Aquí corriges TODO

---

# ⚠️ Regla clave

Si esto está mal → TODO lo demás estará mal

---

# 🧪 3. Generar plan de implementación

Claude divide en tareas:

Ejemplo:

1. crear modelo Pedido  
2. crear endpoint crear pedido  
3. tests de creación  
4. lógica de estados

👉 Ya tienes roadmap técnico

---

# ⚙️ 4. Ejecutar (modo serio)

### Comando:

/superpowers:execute-plan

Claude ahora:

1. escribe tests
    
2. implementa código
    
3. valida
    
4. pasa al siguiente paso
    

👉 flujo real:

test → código → test → refactor

---

# 🔁 5. Iteración continua

Para añadir features:

/superpowers:brainstorm  
→ idea nueva  
  
/superpowers:write-plan  
→ cómo integrarlo  
  
/superpowers:execute-plan  
→ implementarlo

---

# 🧠 6. Refactor (muy importante)

Cuando el proyecto crece:

/superpowers:analyze

Claude:

- detecta problemas
    
- propone mejoras
    
- reorganiza código
    

---

# 🧪 7. Debugging

/superpowers:debug

Le pasas:

- error
    
- contexto
    

👉 te da causa real, no guesses

---

# 📦 Flujo completo resumido

IDEA  
 ↓  
brainstorm  
 ↓  
write-plan  
 ↓  
validar arquitectura  
 ↓  
execute-plan  
 ↓  
tests + código  
 ↓  
iterar features  
 ↓  
analyze / refactor

---

# 🔥 Cómo sería en TU proyecto (ejemplo real)

Para tu app de pedidos:

### 1. Brainstorm

- lógica picker / repartidor
    
- estados del pedido
    
- mapa
    

### 2. Plan

- tablas SQL
    
- endpoints
    
- estados:
    
    - creado
        
    - en preparación
        
    - en reparto
        
    - entregado
        

### 3. Execute

- tests de estados
    
- backend
    
- frontend básico
    

### 4. Iterar

- rutas inteligentes
    
- dashboard
    
- métricas
    

---

# ⚠️ Errores comunes (evítalos)

### ❌ saltarte el plan

→ código roto

### ❌ pedir “haz esto rápido”

→ pierdes todo el sistema

### ❌ no usar CLAUDE.md

→ respuestas inconsistentes

---

# 🧠 Insight clave

El flujo correcto no es:

idea → código

Es:

idea → sistema → código

---

# 🚀 Nivel pro (lo que te interesa)

Si haces bien este flujo:

- reduces bugs brutalmente
    
- mejoras arquitectura automáticamente
    
- puedes escalar sin caos