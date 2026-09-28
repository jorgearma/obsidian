# Selectores no obvios (checklist de pivotes OSINT)

> Lo básico (email, nombre, apodo, teléfono) lo mira todo el mundo. Esta lista es lo que **casi nadie mira** y donde están los mejores pivotes. Un selector es cualquier dato que te lleva a otro dato. Aplica a [[OSINT/auditoria-osint-personal]] y a [[OSINT/investigacion-figuras-publicas-y-estafadores]].

---

## 1. Identificadores digitales ocultos (los más potentes)

| Selector | Por qué es oro | Cómo |
|---|---|---|
| **ID de Google Analytics / AdSense** (`UA-`, `G-`, `pub-`) | Dos webs con el mismo ID = mismo dueño. Destapa redes enteras de scams | spyonweb, analyzeid, dnslytics, builtwith |
| **Hash del favicon** | El mismo favicon en varios servidores = infra hermana, aunque cambien dominio/IP | Shodan: `http.favicon.hash:<n>` |
| **Certificado SSL** (fingerprint, campo Organization, SANs) | Reúsan certificados y datos de organización entre dominios | crt.sh, censys, shodan |
| **Gravatar** | El MD5 del email → foto de perfil, nombre, a veces webs enlazadas | `gravatar.com/avatar/<md5-del-email>` |
| **Google/GAIA ID, canal de YouTube, review de Maps** | Un mismo Google ID enlaza Maps, YouTube, Fotos, reseñas | herramientas tipo GHunt sobre un email @gmail |
| **Wallet cripto** | La blockchain es pública: sigues el dinero de una address | etherscan, blockchair, breadcrumbs |

---

## 2. Metadatos de archivos (lo que el documento delata)

- **EXIF de fotos:** GPS (¡casa/trabajo!), modelo de cámara/móvil, fecha, número de serie.
- **Documentos Office/PDF:** autor, "última modificación por", **nombre de usuario de Windows**, ruta de red interna (`\\SERVIDOR\...`), software y versión, plantilla usada.
- **PDFs escaneados:** modelo de impresora/escáner.
- Herramienta: `exiftool` sobre cualquier archivo → ver [[tools/exiftool]].

---

## 3. Trucos de "recuperación de cuenta" (confirmación sin login)

**Por qué:** los formularios de "he olvidado mi contraseña" te confirman datos gratis.

- Google / Twitter / etc. muestran el email o teléfono **parcialmente enmascarado**: `j****o@gmail.com`, "termina en 87". Cruzando el mismo email en varias plataformas reconstruyes el dato completo.
- "¿Este email tiene cuenta aquí?" → confirma en qué plataformas está registrado.
- Truecaller / apps de "quién me llama" → nombre asociado a un número.

---

## 4. Comportamiento y estilo (stylometry / patrones)

- **Horario de actividad** (tuits, commits de GitHub) → deduce zona horaria y hasta horario de sueño.
- **Modismos, faltas recurrentes, idioma nativo** → región y a veces la persona detrás de una cuenta anónima.
- **Reutilización de textos** (bios, descripciones legales de una web scam) → Google entre comillas encuentra los clones.

---

## 5. Cuentas y rastros que nadie asocia

- **Gamertags:** Steam, PSN, Xbox, Discord (ID numérico), Riot, Epic.
- **Avatar reutilizado:** reverse image (Yandex, Google, TinEye) del mismo avatar en cuentas "anónimas".
- **GitHub / GitLab:** `git log` expone el **email real del autor en cada commit** aunque el perfil lo oculte; commits borrados en forks; secretos y API keys en el historial.
- **Strava / apps de fitness:** las rutas dibujan **dónde vive y trabaja** el objetivo.
- **Reseñas** (Google Maps, Amazon, TripAdvisor) → sitios que frecuenta, a veces nombre real.
- **Wishlist de Amazon, Spotify público, Venmo/Bizum público, Letterboxd, Goodreads.**
- **Pastebin / Ghostbin / Scribd / SlideShare** → documentos y volcados olvidados.
- **Telegram:** username, ID numérico, grupos donde participa.

---

## 6. Números y códigos del mundo real

- **Matrículas de coche** en fotos → propiedad/ubicación.
- **NIF/CIF, número de colegiado, matrícula profesional** → registros oficiales.
- **Teléfono** → apps que lo usan, sync de contactos, anuncios de segunda mano (Wallapop, Milanuncios) con ese número.
- **Direcciones postales compartidas** entre empresas (mismo domicilio social = mismo grupo) → ver [[OSINT/investigacion-figuras-publicas-y-estafadores]].

---

## 7. Infra técnica que revela al dueño

- **WHOIS histórico:** el registrante antes de activar la privacidad (whoxy, securitytrails, viewdns).
- **Subdominios de dev/staging** expuestos, paneles de admin, directorios abiertos, buckets S3.
- **Cabeceras HTTP y mensajes de error** → stack, rutas internas, a veces usuario del sistema.
- **Wayback Machine / archive.today:** versiones antiguas de la web con datos que luego borraron (teléfono, nombre, dirección).

---

## Regla mental

```
Cada selector encontrado → ¿a qué OTRO dato me lleva?
El grafo se expande solo. Para cuando dejas de encontrar cosas nuevas.
```

Vuelca cada hallazgo en `hallazgos.md` con: dato · fuente · fecha · confianza.
