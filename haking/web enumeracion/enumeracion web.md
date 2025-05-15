- Versiones vulnerables de servicios o complementos
- Parámetros de URL
- Formularios de inicio de sesión
- Campos de búsqueda
- Subidas de archivos
- Recorrido de ruta
- Inclusión de archivos locales y/o remotos
- Omisión del filtro de tipo de contenido
- Inyección SQL
- Credenciales predeterminadas
- Relleno de credenciales
- Pulverización de contraseñas

# 🧾 Checklist de Recolección de Información en Enumeración Web

Esta lista te ayudará a recolectar toda la información esencial cuando encuentres una web expuesta (puerto 80/443) durante un pentest o en el OSCP.

---

## 🧠 Información General

- [ ] Título de la página
- [ ] CMS detectado (WordPress, Joomla, etc)
- [ ] Frameworks JS detectados (React, Vue, Angular, etc)
- [ ] Dirección IP y hostname (si aplica)
- [ ] Páginas visibles y rutas exploradas

---

## 📦 Versiones y Tecnologías

- [ ] Servidor web (Apache, Nginx, etc) → `curl -I http://IP`
- [ ] Lenguaje de backend (PHP, Python, etc)
- [ ] Sistema operativo (si se puede inferir)
- [ ] Versiones de CMS o frameworks
- [ ] Certificado SSL (dominios, fechas) → `openssl s_client -connect IP:443`

---

## 📁 Rutas y Archivos

- [ ] `/robots.txt`
- [ ] `/sitemap.xml`
- [ ] Directorios interesantes (`/admin`, `/login`, `/uploads`, `/backup`, etc)
- [ ] Archivos de configuración o backup (`.git`, `.env`, `.bak`, `.zip`, etc)

---

## 🧪 Funcionalidades del sitio

- [ ] Formularios (login, búsqueda, contacto)
- [ ] Posibles puntos de inyección (GET/POST)
- [ ] Posibilidad de subida de archivos
- [ ] Redirecciones internas
- [ ] Parámetros observables en URLs

---

## 🔐 Seguridad y Cabeceras

- [ ] Métodos HTTP habilitados → `curl -X OPTIONS http://IP`
- [ ] Cookies asignadas por el servidor
- [ ] Headers de seguridad (CSP, HSTS, X-Frame-Options)
- [ ] ¿Hay autenticación básica o personalizada?

---

## 🔍 Enumeración dinámica

- [ ] Rutas descubiertas con `gobuster`, `ffuf`, etc
- [ ] Parámetros fuzzed y respuestas (status, errores)
- [ ] Pistas en el código fuente (comentarios, rutas JS)
- [ ] Scripts JS que revelen lógica interna o APIs

---

## 📄 Posibles vectores de ataque

- [ ] ¿LFI/RFI? → prueba `?file=../../etc/passwd`
- [ ] ¿SQLi? → prueba `' or '1'='1`
- [ ] ¿XSS? → prueba `<script>alert(1)</script>`
- [ ] ¿Upload no filtrado? → prueba subir `shell.php`
- [ ] ¿Brute force posible? (usuarios, login sin protección)
- [ ] ¿Vulnerabilidades conocidas del CMS o framework?

---

## 🛠️ Herramientas utilizadas

- [ ] `whatweb`
- [ ] `gobuster` / `ffuf` / `dirsearch`
- [ ] `nikto`
- [ ] `curl`
- [ ] `burpsuite`
- [ ] `nmap` (con script de http)
- [ ] `openssl` (para ver certificados)

---

## 🧠 Anotaciones adicionales

- [ ] Usuarios o emails descubiertos
- [ ] Posibles subdominios
- [ ] VHosts detectados
- [ ] Mensajes de error interesantes
- [ ] Comportamientos inusuales

---



