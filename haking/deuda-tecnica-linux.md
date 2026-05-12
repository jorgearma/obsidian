# Deuda técnica Linux — OSCP

## Lo que está bien cubierto
- Enumeración de servicios (nmap, FTP, SSH, SMTP, SMB, MSSQL, MySQL, RDP, VNC, SNMP)
- Web hacking (SQLi, LFI/RFI, file upload, log poisoning, webdav)
- Privesc básico (SUID, sudo -l, PATH hijacking)
- Linpeas y pspy (interpretación documentada)
- Shells y upgrade de shell
- Transferencia de archivos
- Búsqueda de credenciales

---

## Deuda técnica — por prioridad

### 🔴 Crítico (antes del PEN-200)

#### Pivoting y tunneling
- [ ] Chisel — client/server, forward y reverse tunnels
- [ ] Proxychains — configuración y uso con nmap/herramientas
- [ ] Socat — port forwarding básico
- [ ] Sshuttle — VPN over SSH
- [ ] Doble pivoting (dos saltos de red)

#### Privesc Linux — huecos concretos
- [ ] Capabilities (cap_setuid, cap_net_raw) — GTFOBins capabilities
- [ ] Cron jobs — modificar scripts ejecutados como root
- [ ] Wildcard injection — tar y rsync con wildcards
- [ ] Writeable /etc/passwd o /etc/shadow — añadir usuario root

### 🟡 Importante (durante el PEN-200)

#### Privesc Linux — menos frecuente pero aparece
- [ ] NFS privesc — no_root_squash
- [ ] Docker breakout — montar el sistema de archivos del host

#### Web — técnicas que faltan
- [ ] SSRF (Server-Side Request Forgery) — acceso a servicios internos
- [ ] XXE (XML External Entity) — lectura de archivos internos

#### Password cracking — más profundidad
- [ ] John the Ripper con reglas personalizadas
- [ ] Generación de wordlists con cewl + reglas de mutación
- [ ] Identificación rápida de tipos de hash (hash-identifier, hashid)

### 🟢 No necesario para OSCP
- Buffer overflow Linux — eliminado del examen en 2023
- Metasploit avanzado — solo una máquina del examen, básico suficiente

---

## Recursos para cubrir la deuda

### Pivoting
- THM — "Wreath" (lab completo de pivoting, gratuito)
- THM — "Throwback" (red interna con pivoting)
- HackTricks — Tunneling and Port Forwarding

### Privesc Linux completo
- THM — "Linux PrivEsc" (gratuito, cubre todo)
- GTFOBins — referencia para capabilities y SUID
- PayloadsAllTheThings — Linux Privilege Escalation

### Web (SSRF y XXE)
- PortSwigger Web Academy — gratuito, los mejores labs de SSRF y XXE
- HackTricks — SSRF y XXE

### Password cracking
- THM — "Crack the Hash" (gratuito)
- Hashcat wiki — reglas y modos

---

## Estimación de tiempo para cerrar esta deuda
- Pivoting → 4-5 días (THM Wreath es un lab completo)
- Privesc huecos → 3-4 días (THM Linux PrivEsc)
- SSRF y XXE → 2-3 días (PortSwigger labs)
- Password cracking → 1-2 días

**Total: ~2 semanas antes de entrar al PEN-200**
