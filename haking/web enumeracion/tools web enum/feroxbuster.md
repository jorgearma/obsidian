
# 🧾 Explicación de los flags de feroxbuster

```bash
feroxbuster -u https://app.senaticmia.com/ \
  -x htm,php,html,js,txt,zip,bak,asp,aspx,xml,py \
  -r \
  -o 80-ferox.txt \
  -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories-lowercase.txt \
  -t 100
```

## 🔍 Parámetros explicados:

- `-u http://$RHOST/`  
  → URL objetivo (usa una variable para automatizar).

- `-x htm,php,html,js,txt,zip,bak,asp,aspx,xml,py`  
  → Extensiones comunes a buscar (archivos potencialmente sensibles o ejecutables).
- `-r`  
  → Sigue redirecciones.
- `-o 80-ferox.txt`  
  → Guarda la salida en un archivo llamado `80-ferox.txt`.
- `-w /usr/share/seclists/Discovery/Web-Content/raft-large-directories-lowercase.txt`  
  → Wordlist grande y efectiva para descubrir directorios.
- `-t 100`  
  → Usa 100 threads para acelerar la búsqueda.

---

