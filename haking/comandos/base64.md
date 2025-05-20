# 🔐 `base64` Cheat Sheet (Pentesting Edition)

El comando `base64` se usa para codificar y decodificar datos en base64. Es útil para manipular datos en texto plano durante pruebas de penetración, análisis forense o scripting.

---

## 📦 Sintaxis básica

```bash
base64 [opciones] [archivo]
```

---

## 🛠️ Opciones comunes

| Opción | Descripción |
|--------|-------------|
| `-d` / `--decode` | Decodifica datos codificados en base64 |
| `-w <num>` | Establece el número máximo de caracteres por línea (por defecto 76; `-w 0` desactiva el salto de línea) |
| `-i` | Ignora caracteres no base64 durante la decodificación (en algunas implementaciones) |

---

## 🔁 Ejemplos prácticos

### 🧬 Codificar un archivo
```bash
base64 archivo.txt > archivo.b64
```

### 🧬 Decodificar un archivo
```bash
base64 -d archivo.b64 > archivo.txt
```

### 🔤 Codificar una cadena
```bash
echo -n 'admin:password' | base64
# Resultado: YWRtaW46cGFzc3dvcmQ=
```

### 🔓 Decodificar una cadena
```bash
echo 'YWRtaW46cGFzc3dvcmQ=' | base64 -d
# Resultado: admin:password
```

### ⛓️ Evitar saltos de línea en la salida
```bash
echo -n 'test123' | base64 -w 0
```

---

## 🔎 Casos de uso en Pentesting

- Manipular cabeceras HTTP con Basic Auth:
```bash
echo -n 'admin:admin' | base64
# Luego usar: Authorization: Basic YWRtaW46YWRtaW4=
```

- Decodificar parámetros URL sospechosos:
```bash
echo 'cGFzc3dvcmQ9cm9vdA==' | base64 -d
```

- Extraer contenido codificado en base64 desde binarios o scripts:
```bash
strings script.sh | grep -i '[A-Za-z0-9+/=]\{20,\}' | base64 -d
```

---

## 🧠 Tip

Muchos lenguajes permiten codificar/decodificar base64 (Python, Bash, PHP, etc.), pero el comando `base64` es ideal en terminales Linux para tareas rápidas.

---

## 📚 Recursos adicionales

- [man base64](https://man7.org/linux/man-pages/man1/base64.1.html)
- [RFC 4648 - The Base64 Alphabet](https://datatracker.ietf.org/doc/html/rfc4648)