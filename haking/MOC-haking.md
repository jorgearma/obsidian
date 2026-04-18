# Hacking / Ciberseguridad — Mapa de Contenido

Notas de pentesting, recon, escalada de privilegios y herramientas.
Contexto: aprendizaje personal, CTFs, máquinas de práctica.

---

## Metodología

- [[metodologia]] — metodología general (referencia OSCP)
- [[importante]] — cheatsheet rápido de referencia

---

## Reconocimiento y enumeración

### Red
- [[1. nmap]] — escaneos, scripts NSE
- [[notas]] — pendiente: mejorar script nmap con SMB scripts, DNS recon

### Web
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
