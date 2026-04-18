# 🧠 TMUX — Cheat Sheet para Entrevistas

## 🎯 Objetivo

Demostrar fluidez real trabajando con múltiples terminales, navegación rápida y control del entorno sin perder tiempo.

---

# 🔑 1. Lo mínimo que DEBES dominar

## Crear / entrar / salir

```bash
tmux new -s dev        # crear sesión
tmux attach -t dev     # entrar
tmux ls                # ver sesiones
```

```plaintext
Ctrl + b  d            # salir sin cerrar (clave)
```

---

# 🧱 2. Dividir pantalla (lo más visible en entrevista)

```plaintext
Ctrl + b  %   # dividir vertical
Ctrl + b  "   # dividir horizontal
```

👉 Esto demuestra multitarea real.

---

# 🔄 3. Moverte rápido (muy importante)

```plaintext
Ctrl + b  ← ↑ ↓ →
Ctrl + b  o
```

👉 Si te mueves fluido = nivel alto.

---

# ❌ 4. Cerrar paneles

```bash
exit
```

---

# 🧩 5. Ventanas (nivel pro)

```plaintext
Ctrl + b  c   # nueva ventana
Ctrl + b  n   # siguiente
Ctrl + b  p   # anterior
```

👉 Separar tareas = mentalidad senior.

---

# ⚡ 6. Layout automático (truco rápido)

```plaintext
Ctrl + b  espacio
```

👉 Reorganiza todo en segundos.

---

# 🔍 7. Scroll (muy útil en debugging)

```plaintext
Ctrl + b  [
```

Salir con:

```plaintext
q
```

---

# 🧠 8. Mentalidad que buscan

En entrevista NO quieren ver comandos.  
Quieren ver:

- No pierdes contexto
    
- Sabes dividir trabajo
    
- No abres 20 ventanas del sistema
    
- Controlas logs, server y pruebas a la vez
    

---

# 🧪 9. Ejemplo real (di esto mientras lo haces)

"Voy a dividir la terminal para separar logs y servidor"

Luego:

```plaintext
Ctrl + b  %
```

En un lado:

```bash
python app.py
```

En otro:

```bash
tail -f logs.txt
```

👉 Esto impresiona más que mil palabras.

---

# 🏁 10. Regla de oro

```plaintext
Ctrl + b → sueltas → tecla
```

Si fallas esto, todo falla.

---

# 🚀 RESUMEN ULTRA RÁPIDO

- Crear sesión → tmux new -s dev
    
- Dividir → Ctrl+b % o "
    
- Moverte → Ctrl+b flechas
    
- Nueva ventana → Ctrl+b c
    
- Salir sin cerrar → Ctrl+b d
    

---

Si dominas SOLO esto y lo haces fluido → ya das imagen profesional.