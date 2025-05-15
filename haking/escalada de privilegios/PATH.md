
# 🧠 Cheat Sheet: Variable de Entorno `$PATH`

## ¿Qué es `$PATH`?
`$PATH` es una variable de entorno que le dice al sistema **dónde buscar los ejecutables** cuando escribes un comando en la terminal.

---

## 📋 Ver el contenido del `PATH`

```bash
echo $PATH
```

---

## ➕ Añadir una ruta al `PATH` (temporal)

**Al principio (más prioridad):**

```bash
export PATH="/nueva/ruta:$PATH"
```

**Al final (menos prioridad):**

```bash
export PATH="$PATH:/nueva/ruta"
```

> Estas modificaciones solo duran hasta que cierres la terminal.

---

## 📌 Hacer permanente (por usuario)

### Bash

```bash
echo 'export PATH="/nueva/ruta:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Zsh

```bash
echo 'export PATH="/nueva/ruta:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

---

## 🔄 Restaurar el `PATH` a valores por defecto

```bash
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
```

---

## 🛡️ Añadir solo si no está ya presente (evita duplicados)

```bash
case ":$PATH:" in
  *":/nueva/ruta:"*) ;;  # Ya está
  *) export PATH="/nueva/ruta:$PATH" ;;
esac
```

---

## 📂 Comprobar si un ejecutable está en el PATH

```bash
which nombre_comando
# o
command -v nombre_comando
```

---

## 🔍 Buscar un ejecutable en todas las rutas del PATH

```bash
type -a nombre_comando
```