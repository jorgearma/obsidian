# Hacking / Ciberseguridad — Mapa de Contenido

Notas de pentesting, recon, escalada de privilegios y herramientas.
Contexto: aprendizaje personal, CTFs, máquinas de práctica.

---

## Metodología

- [[metodologia]] — metodología general (referencia OSCP)
- [[importante]] — cheatsheet rápido de referencia

---

## Active Directory y labs

- [[montar-lab-ad]] — bitácora de construcción del lab AD propio (Nordwind): DC, OUs, usuarios, AGDLP, cliente
- [[virtualbox-labs-config]] — **config perfecta de VMs en VirtualBox** (red interna, EFI/TPM, Win11, Guest Additions, snapshots, troubleshooting)
- [[AD/dns-en-ad]] — por qué AD depende del DNS (SRV records)
- [[AD/ldap]] — la "guía telefónica" del dominio: directorio + protocolo, el DN, enumeración con ldapsearch
- [[AD/kerberos-kdc]] — Kerberos explicado: TGT→TGS, el KDC, y cómo cada ataque abusa de un cifrado del flujo

**Herramientas visuales interactivas** (abrir el `.html` con doble clic → navegador):
- `AD/ldap-arbol.html` — árbol LDAP navegable + "la lógica en 3 niveles" + el DN en vivo
- `AD/permisos-corp.html` — empresa interactiva: los 2 poderes (recursos vía grupos / autoridad vía delegación en OU)
- `AD/explorador-ad.html` — explorador tipo ADUC: directorio + recursos de red + PC local, con ficha y riesgo de cada objeto

---

## Reconocimiento y enumeración

### Red
- [[1. nmap]] — escaneos, scripts NSE
- [[notas]] — pendiente: mejorar script nmap con SMB scripts, DNS recon

### Web
- [[web enumeracion/foothold-reconocimiento]] — **hoja de reconocimiento de footholds** (sigue el dato: señal → vector → test)
- [[web enumeracion/enumeracion web]] — proceso general
- [[web enumeracion/enumer]] — comandos rápidos
- [[web enumeracion/login]] — ataques a login
- [[web enumeracion/DNS/reconocimiento-dns-pentesting]] — subfinder, amass, dig

### Herramientas web
- [[web enumeracion/tools web enum/curl]]
- [[web enumeracion/tools web enum/dig]]
- [[web enumeracion/tools web enum/feroxbuster]]
- [[web enumeracion/tools web enum/nikto]]
- [[web enumeracion/tools web enum/openssl]]
- [[web enumeracion/tools web enum/wfuzz]]
- [[web enumeracion/tools web enum/wpscan]]

---

## OSINT

- [[OSINT/checklist-maestra-selectores]] — **índice maestro**: taxonomía completa de qué mirar (28 categorías, marcable por caso)
- [[OSINT/auditoria-osint-personal]] — metodología de auto-auditoría (5 áreas: identidad, credenciales, técnica, social, documental)
- [[OSINT/investigacion-figuras-publicas-y-estafadores]] — investigación patrimonial/corporativa de políticos y estafadores (registros públicos, infra de scams, link analysis, cadena de custodia)
- [[OSINT/selectores-no-obvios]] — checklist de pivotes poco obvios (analytics ID, favicon hash, gravatar, EXIF, recuperación de cuenta, git log, strava...)

---

## Hardware y consolas

- [[hardware-consolas/xbox360-badupdate-abadavatar]] — Xbox 360 liberada por software (ABadAvatar + Aurora): setup, rutina, añadir juegos GOD, backup NAND

---

## Protocolos y servicios

- [[FTP-TCP 21]] — enumeración FTP
- [[SSH/ssh-comandos]] — comandos SSH
- [[SSH/ssh-enumeracion]] — enumeración SSH
- [[2. gobuster]] — directory brute-force
- [[cheat.page]] — referencia general

---

## Escalada de privilegios

- [[escalada de privilegios/sudo -l]] — abusar sudo
- [[escalada de privilegios/SUID]] — binarios SUID
- [[escalada de privilegios/PATH]] — PATH hijacking
- [[escalada de privilegios/buscar credenciales]] — encontrar credenciales
- [[escalada de privilegios/enumerar puertos internos]] — puertos locales

---

## Herramientas

- [[tools/hashcat]] — cracking de hashes
- [[tools/hydra]] — fuerza bruta
- [[tools/linpeas]] — enumeración Linux post-explotación
- [[tools/searchsploit]] — buscar exploits
- [[tools/pspy/pspy]] — monitorizar procesos
- [[tools/pspy/como leer]] — interpretar output de pspy
- [[tools/exiftool]] — metadatos
- [[tools/ike-scan]] — VPN/IKE
- [[tools/SNMP]] — enumeración SNMP
- [[burnp suite/sniper atack]] — Burp Suite intruder

---

## Comandos útiles

- [[comandos/base64]]
- [[comandos/find]]
- [[comandos/grep]]
- [[comandos/opne ssl]]
- [[comandos/smb]]
- [[comandos/string]]
- [[comandos/tr]]
- [[hash]] — tipos de hash, identificación
- [[transferencia de archivos]] — mover archivos entre máquinas
- [[upgrade shell]] — obtener shell interactiva

---

## Pendiente / estudiar

- [[tareas]] — tareas de hacking
- Estudiar pspy en profundidad
- Hacer herramienta para dogscan
- Retomar OverTheWire
- Hacer una máquina de práctica
