# Checklist maestra de selectores OSINT (qué mirar)

> Taxonomía completa de recolección: el **índice de todo lo que se puede mirar** de un objetivo. Esta nota es el "QUÉ"; el "CÓMO" está en [[OSINT/auditoria-osint-personal]], [[OSINT/investigacion-figuras-publicas-y-estafadores]] y [[OSINT/selectores-no-obvios]].
>
> Marca `[x]` lo cubierto en cada caso. Cada hallazgo → `hallazgos.md` (dato · fuente · fecha · confianza).
> Leyenda: 🌍 pasivo · ⚡ activo (deja rastro) · 📍 depende de país · ⚖️ zona legal delicada.

---

## Identidad base

### 1. Nombres e identidad real 🌍
- [ ] Nombre completo, segundos apellidos
- [ ] Variantes, transliteraciones, nombre de soltera
- [ ] Fecha de nacimiento, edad
- [ ] Identificadores oficiales 📍: NIF/DNI, CIF, nº de colegiado, pasaporte (a veces parciales en documentos filtrados)

### 2. Emails 🌍
- [ ] Email actual y antiguos
- [ ] Patrón (nombre.apellido / iniciales) → deducir emails corporativos con theHarvester, hunter.io
- [ ] Gravatar (MD5 del email → foto/perfil), GHunt sobre @gmail (Google ID, reseñas, Fotos)

### 3. Números de teléfono 🌍
- [ ] Número actual y antiguos · operador · país (prefijo)
- [ ] Apps asociadas: WhatsApp, Telegram, Signal, Viber (foto y "última vez" a veces visibles)
- [ ] Truecaller / "quién me llama" → nombre asociado
- [ ] Anuncios con ese número: Wallapop, Milanuncios, segunda mano
- [ ] Filtraciones donde aparece (ver 10)

---

## Presencia digital

### 4. Redes sociales 🌍
- [ ] Facebook, Instagram, X/Twitter, Threads, TikTok, LinkedIn
- [ ] Reddit, Discord (ID numérico), Snapchat, Pinterest, Bluesky, Mastodon
- [ ] Twitch, YouTube, Medium, Quora
- [ ] Gaming: Steam, PSN, Xbox, Riot, Epic
- [ ] Otras: Spotify, Last.fm, Letterboxd, Goodreads, Strava (¡rutas = casa/trabajo!), Venmo/Bizum público, Wishlist de Amazon

### 5. Nicknames reutilizados 🌍
- [ ] Buscar el MISMO alias en cientos de webs → relaciona cuentas "independientes"
- [ ] Herramientas: sherlock, maigret, whatsmyname.app
- [ ] Ej.: `DarkWolf99` en GitHub + Reddit + Steam + foros = misma persona

### 6. Avatares e imágenes (reverse image) 🌍
- [ ] Google Images, Yandex (mejor para caras), Bing, TinEye
- [ ] Reconocimiento facial ⚖️: PimEyes, FaceCheck (potentes pero delicados legalmente)
- [ ] Revela: otras cuentas, fotos antiguas, perfiles olvidados, blogs

### 7. Fotografías (contenido + metadatos) 🌍
- [ ] EXIF: modelo de móvil, fecha, GPS, software, nº de serie, miniaturas ocultas
- [ ] Contenido: objetos, matrículas, carteles/direcciones, reflejos, personas etiquetadas
- [ ] Herramienta: `exiftool` → ver [[tools/exiftool]]

---

## Infraestructura y código

### 8. Dominios 🌍→⚡
- [ ] WHOIS (actual e histórico: whoxy, securitytrails, viewdns)
- [ ] DNS, subdominios (subfinder, amass), historial DNS
- [ ] Wayback Machine / archive.today (versiones viejas con datos borrados)
- [ ] Certificados SSL (crt.sh), servidores, tecnología (builtwith, wappalyzer)
- [ ] Enlaza con [[web enumeracion/DNS/reconocimiento-dns-pentesting]] y [[1. nmap]]

### 9. GitHub / código 🌍
- [ ] Repos, contribuciones, lenguajes
- [ ] **`git log` → email real del autor** (aunque el perfil lo oculte)
- [ ] Claves/secretos/API keys en el historial (trufflehog, gitleaks)
- [ ] Horarios de commits → zona horaria y rutina
- [ ] GitLab, Bitbucket también

### 24. Huella técnica 🌍
- [ ] IPs antiguas, ASN, DNS, certificados, servidores
- [ ] Fingerprints (favicon hash en Shodan, JA3/JARM), usernames de sistema
- [ ] ID de Google Analytics/AdSense compartido → redes de sitios del mismo dueño

---

## Datos filtrados y registros

### 10. Filtraciones de datos ⚖️
- [ ] Have I Been Pwned (🌍 seguro), DeHashed, LeakCheck, IntelligenceX, Snusbase
- [ ] Puede aparecer: passwords antiguas, direcciones, IPs, teléfonos, emails
- [ ] ⚖️ Usar passwords ajenas para acceder = delito. Para auto-auditoría, OK

### 19. Metadatos de documentos 🌍
- [ ] PDF, DOCX, PPTX, XLSX → autor, empresa, software, fecha, "modificado por", rutas de red internas
- [ ] `exiftool documento.pdf`

### 20. Archivos públicos 🌍
- [ ] Dork: `site:dominio filetype:pdf` / `"Nombre" filetype:pdf`
- [ ] CVs, presentaciones, manuales, informes, cachés

### 21. Caché e histórico de internet 🌍
- [ ] Wayback Machine, archive.today, cachés de buscadores
- [ ] Versiones antiguas de webs (datos que luego borraron)

---

## Mundo físico y patrimonial 📍

### 11. Direcciones físicas 📍
- [ ] Actual y antiguas, códigos postales, lugares donde ha vivido

### 12. Propiedades 📍 (España: Catastro, Registro de la Propiedad)
- [ ] Viviendas, parcelas, hipotecas, cargas → ver [[OSINT/investigacion-figuras-publicas-y-estafadores]]

### 13. Empresas 📍 (España: BORME, Registro Mercantil)
- [ ] Nombre, CIF/CVR, participaciones, cargo (administrador/socio/apoderado), historial
- [ ] Domicilios sociales compartidos = mismo grupo empresarial

### 14. Información fiscal / mercantil pública 📍
- [ ] Empresas de alta, IVA, licencias, registros mercantiles
- [ ] (Las declaraciones de renta personales normalmente NO son públicas)

### 15. Vehículos 📍
- [ ] Matrículas, ITV, historial, accidentes, fotos (muy dependiente de país)

### 23. Geolocalización / patrones de vida 🌍
- [ ] Casa, trabajo, gimnasio, cafeterías, rutina, vacaciones
- [ ] Fuentes: Strava, geotags, check-ins, fondos de fotos, horarios de posts

---

## Vida, relaciones y reputación

### 16. Estudios 🌍
- [ ] Universidad, cursos, certificados, TFG/TFM, publicaciones académicas (Dialnet, Google Scholar)

### 17. Trabajo 🌍
- [ ] Empresas, CV, puestos, antigüedad, organigrama, salarios publicados (Glassdoor)

### 18. Publicaciones 🌍
- [ ] Blogs, foros, comentarios, reviews, Stack Overflow, Reddit, Quora

### 22. Relaciones personales 🌍
- [ ] Likes, amigos, seguidores, fotos, etiquetas, comentarios
- [ ] Overlap de followers → círculo real; co-autores en GitHub; conexiones LinkedIn

### 25. Criptomonedas 🌍
- [ ] Wallets (BTC/ETH), ENS, NFTs, transacciones, exchanges públicos
- [ ] etherscan, blockchair, breadcrumbs, arkham

---

## Añadidos que faltaban en el borrador

### 26. Registros judiciales y boletines oficiales 📍
- [ ] BOE/boletines autonómicos: sanciones, concursos, nombramientos
- [ ] Sentencias públicas (CENDOJ en España), concursos de acreedores

### 27. Menciones en prensa y hemerotecas 🌍
- [ ] Hemerotecas, Google News, archivos de periódicos → historia y contexto del objetivo

### 28. Motores de personas / data brokers 📍⚖️
- [ ] Pipl, Spokeo, BeenVerified (muy US), 411, whitepages
- [ ] Bots de Telegram de filtraciones ⚖️ (existen; legalidad muy delicada, cuidado)

---

## Recordatorio
```
Ningún dato es el final: cada uno es un pivote al siguiente.
Verifica con 2 fuentes. Archiva la evidencia. Separa dato de inferencia.
```
Marco legal → [[OSINT/investigacion-figuras-publicas-y-estafadores]] (líneas rojas).
