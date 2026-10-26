# 🎯 Hoja de reconocimiento — Foothold web

> **Para qué sirve esto:** NO es para aprender a explotar a fondo (eso lo documentas desde cada máquina real).
> Es para **RECONOCER** el vector cuando lo tengo delante. No reconozco lo que no sé que existe.
> Llevar al lado mientras hago máquinas. La profundidad vive en los write-ups de `machines/`.

---

## 🧠 La mentalidad (leer antes de cada web)

**No busco "qué versión es". Pregunto: "¿qué sabe HACER esta web, y a dónde va el dato que le meto?"**

El destino del dato = la clase de vulnerabilidad. Eso es **seguir el dato**.

### Los 3 cubos de dónde sale el foothold (por frecuencia real)

1. **🔥 Credenciales / misconfiguración** — el más grande y el más rápido. (default creds, panel expuesto, `.git`, backup, listing, anónimo)
2. **🔥 Vuln en el código propio de la app** — igual de grande. NO hay CVE, el dev lo hizo mal. (upload, LFI→RCE, cmd injection, SSTI, SQLi)
3. **CVE conocido** — el más pequeño. Y cuando es CVE suele ser del **CMS/plugin**, no del servidor web.

> La mayoría NO se googlea por versión. Se encuentra **enumerando** (probando creds + persiguiendo inputs).

---

## 👀 Recon mínimo ante TODA web (los disparadores de reconocimiento)

- [ ] `whatweb` / `curl -I` → servidor, lenguaje, **CMS + versión** (no me quedo en el banner de Apache)
- [ ] Código fuente (Ctrl+U), comentarios, rutas en JS, `/robots.txt`, `/sitemap.xml`
- [ ] `gobuster`/`feroxbuster` → `/admin`, `/login`, `/uploads`, `/backup`, `.git`, `.env`, `.bak`, `.zip`
- [ ] **VHosts / subdominios** (fuzz de `Host:`) ← foothold escondido clásico
- [ ] Listar TODA funcionalidad: cada formulario, cada parámetro (`?x=`), cada subida, cada login
- [ ] Interceptar con Burp → ¿viaja XML? ¿JSON? ¿parámetros ocultos?

---

## 📊 SIGUE EL DATO — tabla de reconocimiento

| Si veo esto (señal) | A dónde va el dato | Vector | Test de 10 segundos | A dónde lleva | Nota |
|---|---|---|---|---|---|
| Formulario de **subida** de archivos | sistema de archivos | **File upload** | subir `shell.php` / `.phtml` | webshell → RCE | [[file-upload]] |
| `?file=` `?page=` `?doc=` `?include=` | lectura de archivo | **LFI / Path traversal** | `?file=../../../../etc/passwd` | leer config/creds → **log poison / php filter → RCE** | [[lfi-rce]] |
| Campo que ejecuta algo (ping, DNS, convertir, exportar) | ejecución de comando | **Command injection** | `; id` · `\| whoami` · `` `id` `` | RCE directo | [[command-injection]] |
| Mi input me lo **devuelve renderizado** en la página | motor de plantillas | **SSTI** | `{{7*7}}` → ¿sale `49`? | RCE | [[ssti]] |
| Login / búsqueda / cualquier cosa con BBDD detrás | base de datos | **SQLi** | `'` (¿error?) · `' or 1=1-- -` | bypass login / dump creds / `INTO OUTFILE`→shell | [[sqli]] · [[login]] |
| Campo "URL de imagen", "importar de enlace", `?url=` | el servidor hace la petición | **SSRF** | meter mi IP + `python3 -m http.server` | servicios internos / metadata cloud | [[ssrf]] |
| Viaja **XML** en la petición (Burp) | parser XML | **XXE** | `<!ENTITY xxe SYSTEM "file:///etc/passwd">` | leer archivos / SSRF | [[xxe]] |
| Formulario de **login** | autenticación | **Creds / brute / bypass** | default creds · hydra · `' or 1=1-- -` | entrar al panel | [[login]] |

> SSRF y XXE suelen ser **pasos intermedios**, no el foothold final. Upload / LFI→RCE / cmd injection / SSTI son los que **dan la shell**.

---

## 🔑 Cubo 1 — Creds / misconfig (lo primero y más rápido)

Antes de romperme la cabeza con una vuln, pruebo lo gratis:

- [ ] **Default creds** del panel/servicio que identifiqué (`admin:admin`, `(nombre máquina)`, `tomcat:tomcat`...) → [[login]]
- [ ] **Paneles → RCE directo:** Tomcat Manager (deploy `.war`), Jenkins (script console), phpMyAdmin (`INTO OUTFILE`), WordPress (editor de plugin/tema)
- [ ] **Archivos expuestos:** `.git/` (dumpear repo), `.env`, `config.php.bak`, `.zip`/`.tar.gz`, directory listing
- [ ] **Acceso anónimo / sin auth** a rutas que no deberían

---

## 🧭 Cubo 3 — CVE (cuando identifico CMS/app con versión)

- [ ] `searchsploit <cms> <version>` (Google offline, PRIMERO)
- [ ] Google: `<cms> <version> exploit` · `<plugin> <version> rce github`
- [ ] WordPress → `wpscan --enumerate vp` (plugins vulnerables) → [[wpscan]]
- [ ] ⚠️ El servidor web (Apache/nginx) casi nunca es la puerta. Miro **la app**, no el banner.

---

## 🚫 Regla anti-túnel (la que de verdad decide el examen)

> Si un vector sale **limpio, NO lo fuerzo.** Cambio de puerta (creds → código → CVE) o de servicio.
> La máquina tiene entrada **seguro** — pero puede NO estar donde estoy mirando.
> Enumero a lo ancho antes de cavar hondo. Apunto lo que YA he probado para no repetir ni rendirme antes de tiempo.

---

## ⚠️ Para OSCP: bajo valor como foothold (no gastar tiempo)
- **XSS** → casi nunca es foothold en OSCP (es para web app assessment)
- **Clickjacking / CSRF / headers** → bug bounty, no gana máquinas → [[haader/clickjacking]]

---

## 🔗 Relacionadas
- [[enumeracion web]] — checklist de recon completa
- [[enumer]] — comandos rápidos de fingerprinting
- [[metodologia]] — metodología general
