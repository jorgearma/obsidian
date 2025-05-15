
# 🧰 Comandos esenciales de `curl` para pentesters


# 🔧 Comandos `curl` combinados con herramientas para pentesters

## 📰 1. Obtener HTML limpio en texto legible
```bash
curl -i -s http://$RHOST | html2text
```
📌 Convierte el HTML en texto plano legible.

---

## 🕵️ 2. Buscar comentarios en el HTML
```bash
curl -s http://$RHOST | grep -iE '<!--|//'
```
📌 Detecta comentarios HTML y JavaScript que pueden filtrar información sensible.

---

## 🔎 3. Extraer enlaces del código fuente
```bash
curl -s http://$RHOST | grep -Eo '(href|src)="[^"]+"' | cut -d'"' -f2
```
📌 Extrae rutas y enlaces para descubrir recursos ocultos.

---

## 📂 4. Buscar archivos `.php`, `.bak`, `.zip`, etc.
```bash
curl -s http://$RHOST | grep -Eo '[^"]+\.(php|bak|zip|txt|conf|sql)'
```
📌 Detecta archivos potencialmente interesantes para enumeración o explotación.

---

## 🧪 5. Detectar formularios en la página
```bash
curl -s http://$RHOST | grep -i "<form"
```
📌 Identifica formularios de login o subida de archivos.

---

## 🔐 6. Ver cookies en la respuesta
```bash
curl -s -I http://$RHOST | grep -i set-cookie
```
📌 Extrae cookies enviadas por el servidor, útil para pruebas de sesión.

---

## 🛠️ 7. Probar cabeceras para bypass de IPs
```bash
curl -s -H "X-Forwarded-For: 127.0.0.1" http://$RHOST/admin
```
📌 Prueba acceso a rutas protegidas usando headers comunes de bypass.

---

## 🧠 8. Detectar redirecciones y saber adónde apuntan
```bash
curl -s -I http://$RHOST | grep -i location
```
📌 Muestra si hay redirecciones activas en el servidor.

---

💡 Consejo: Usa alias o funciones en `.bashrc` para automatizar estas tareas.



## 🔍 1. Ver respuesta HTTP completa (cabeceras + contenido)
```bash
curl -i http://$IP
url -i -s http://$RHOST | html2text
```

## 🧠 2. Ver solo cabeceras de respuesta
```bash
curl -I http://$IP
```

## 🔐 3. Autenticación básica
```bash
curl -u admin:admin http://$IP/secret/
```

## 🚪 4. Ver métodos HTTP habilitados
```bash
curl -X OPTIONS http://$IP -i
```

## 📤 5. Subir archivo (PUT)
```bash
curl -T shell.php http://$IP/uploads/
```

## 🗃️ 6. Enviar datos POST
```bash
curl -X POST -d "username=admin&password=admin" http://$IP/login.php
```

## 🧪 7. Probar inyecciones en parámetros GET
```bash
curl "http://$IP/index.php?id=1' OR '1'='1"
```

## 🪪 8. Enviar cabeceras personalizadas
```bash
curl -H "X-Forwarded-For: 127.0.0.1" http://$IP/admin
curl -H "Host: admin.local" http://$IP
```

## 🍪 9. Enviar cookies
```bash
curl -b "PHPSESSID=abc123" http://$IP/dashboard
```

## 🔄 10. Seguir redirecciones
```bash
curl -L http://$IP
```

## 🕵️ 11. User-Agent personalizado
```bash
curl -A "Mozilla/5.0" http://$IP
```

## ⚠️ 12. Guardar respuesta en archivo
```bash
curl http://$IP/index.php -o index.html
```

## 🎯 13. Cabeceras para bypass de filtros
```bash
curl -H "X-Originating-IP: 127.0.0.1" http://$IP/admin
```

---

