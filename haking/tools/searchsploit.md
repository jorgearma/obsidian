
# 🛠️ `searchsploit` Cheat Sheet

## 🔍 Búsqueda básica
```bash
searchsploit <término>
```
Busca exploits relacionados con el término especificado.
```bash
searchsploit apache
searchsploit wordpress 5.2
```

## 🧠 Búsqueda inteligente
```bash
searchsploit -w <término>
```
Muestra resultados con links web (Exploit-DB).
```bash
searchsploit -w openssl
```

```bash
searchsploit -x <path/to/exploit>
```
Muestra el contenido de un exploit específico.

## 🔍 Búsqueda exacta
```bash
searchsploit -t <término>
```
Solo muestra resultados con coincidencia exacta en el título.

## 🎯 Búsqueda por múltiples términos
```bash
searchsploit <palabra1> <palabra2>
```
Ambos términos deben aparecer en el resultado.
```bash
searchsploit linux kernel
```

## 📁 Copiar exploit al directorio actual
```bash
searchsploit -m <ID_o_path>
```
Copia el exploit a tu directorio de trabajo.
```bash
searchsploit -m exploits/windows/remote/12345.py
```

## 🗃️ Actualizar base de datos
```bash
searchsploit -u
```
Actualiza la base de datos de exploits locales.

## 🛠️ Usar con grep para refinar
```bash
searchsploit samba | grep Remote
```
Filtra resultados que contengan "Remote".

## 🧾 Mostrar nombre del archivo en resultados
```bash
searchsploit -p <término>
```

## ⚙️ Mostrar opciones de ayuda
```bash
searchsploit -h
```