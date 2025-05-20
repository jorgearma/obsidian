# 🧵 `strings` Cheat Sheet (Pentesting Edition)

El comando `strings` se usa para extraer texto legible (ASCII o Unicode) de archivos binarios o ejecutables. Es una herramienta útil para encontrar contraseñas, rutas, comandos ocultos o indicadores dentro de binarios.

---

## 📦 Sintaxis básica

```bash
strings [opciones] archivo
```

---

## 🛠️ Opciones útiles

| Opción          | Descripción                                                                                                                                           |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-n <num>`      | Mínimo número de caracteres consecutivos para considerar como texto (por defecto: 4)                                                                  |
| `-t <format>`   | Muestra la **posición** donde se encuentra la cadena dentro del archivo (`d` = decimal, `x` = hex, `o` = octal)                                       |
| `-e <encoding>` | Fuerza la codificación: `s` (single-7-bit), `S` (single-8-bit), `b` (16-bit little endian), `B` (16-bit big endian), `l` (16-bit LE), `L` (32-bit LE) |
| `-a`            | Escanea el archivo completo (por defecto se comporta igual, pero en algunos entornos puede ser necesario)                                             |
| `-f`            | Muestra el nombre del archivo antes de cada línea de salida                                                                                           |

---

## 📋 Ejemplos prácticos

### 🔍 Extraer strings legibles
```bash
strings binario
```

### 🔍 Con strings de al menos 6 caracteres
```bash
strings -n 6 binario
```

### 🧭 Mostrar offset en hexadecimal
```bash
strings -t x binario
```

### 🧠 Buscar cadenas con codificación UTF-16 LE
```bash
strings -e l archivo
```

### 🧪 Extraer y filtrar por palabra clave (credenciales, comandos, URLs)
```bash
strings archivo | grep -i "password"
strings archivo | grep -iE "http|https|/bin/bash|/sh"
```

---

## 💡 Uso común en Pentesting

- Buscar contraseñas hardcoded.
- Ver rutas internas en binarios SUID.
- Detectar comandos del sistema ejecutados internamente.
- Extraer scripts embebidos o configuraciones.

---

## 🔒 Buenas prácticas

- Usar junto con `grep`, `less`, `awk` para filtrar.
- Complementar con `ltrace`, `strace`, `gdb` para entender el comportamiento del binario.
- Ideal como paso de *reconocimiento estático* antes de ejecutar binarios.

---

## 📚 Recursos adicionales

- [man strings](https://man7.org/linux/man-pages/man1/strings.1.html)
- Herramienta alternativa: `binwalk`, `xxd`, `hexdump` para análisis más profundo.