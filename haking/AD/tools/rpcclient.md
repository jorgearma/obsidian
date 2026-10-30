# 🧰 rpcclient — Enumeración (y abuso) de AD por MS-RPC

> Herramienta de **Samba** que habla el protocolo **MS-RPC** sobre SMB (named pipes, puerto 445).
> Es el "teléfono directo" al DC: le haces preguntas (usuarios, grupos, política) y, si tienes
> permisos, también le das órdenes (cambiar contraseñas). Su gran baza: la **sesión nula**.
> Relacionado: [[enumeracion-ad-sin-credenciales]] · [[sacar-nombre-de-dominio]] · [[netexec]] · [[impacket]] · [[acl-abuse]] · [[ldap]]

---

## Idea central
RPC (Remote Procedure Call) = llamar funciones de la máquina remota como si fueran locales.
En AD, el DC expone funciones de gestión (SAMR, LSA) por named pipes. `rpcclient` te deja
invocarlas a mano. Si el DC permite **sesión nula** (usuario anónimo), puedes enumerar medio
dominio **sin una sola credencial** → es el primer tiro contra un DC.

## Sintaxis base
```bash
rpcclient -U "" -N <IP>                 # sesión NULA (anónima): -U usuario vacío, -N sin pass
rpcclient -U "usuario%password" <IP>    # sesión autenticada (user%pass en una línea)
rpcclient -U "dominio/usuario" <IP>     # te pide la pass de forma interactiva
```
Entras a un prompt interactivo `rpcclient $>`. Desde ahí lanzas los comandos de abajo.

### Modo "un disparo" (sin entrar al prompt) → el que uso en scripts
```bash
rpcclient -U "" -N <IP> -c "enumdomusers"              # ejecuta y sale
rpcclient -U "" -N <IP> -c "querydispinfo"
```
`-c "comando"` = ejecuta ese comando y vuelve a la shell. Ideal para pipes y bucles.

---

## 🔎 Enumeración — lo que pregunto (sin credenciales si hay null)

### Usuarios (el objetivo nº1 → alimenta [[asrep-roasting]])
```
enumdomusers          # lista TODOS los usuarios: user:[nombre] rid:[0x...]
querydispinfo         # usuarios + DESCRIPCIÓN (¡a veces hay passwords apuntadas aquí!)
queryuser 0x47b       # ficha completa de un usuario por su RID (último login, flags...)
queryusergroups 0x47b # a qué grupos pertenece ese usuario
```

**Cómo leer la salida de `enumdomusers`:**
```
user:[svc-alfresco] rid:[0x47b]
       └─ nombre         └─ RID en hexadecimal
```
El RID separa grano de paja (detalle del ruido en [[enumeracion-ad-sin-credenciales]]):
RIDs altos y correlativos = cuentas creadas por el admin = **señal**. Prefijo `svc-` = cuenta
de servicio = objetivo prioritario (AS-REP / Kerberoast).

### Grupos
```
enumdomgroups         # grupos del dominio (con su RID)
querygroup 0x200      # ficha de un grupo (0x200 = Domain Admins)
querygroupmem 0x200   # MIEMBROS de un grupo por RID → ¿quién es Domain Admin?
enumalsgroups domain  # grupos locales de dominio (builtin incluidos)
```

### Política de contraseñas (antes de hacer spraying/brute)
```
getdompwinfo          # longitud mínima, complejidad
getusrdompwinfo 0x47b # política aplicada a un usuario concreto
```
El porqué: saber el **lockout** antes de pulverizar contraseñas ([[netexec]] spraying).

### Traducir SID ↔ nombre (base del RID cycling)
```
lookupnames administrator      # nombre  → SID
lookupsids S-1-5-21-...-500    # SID     → nombre
lsaenumsid                     # SIDs que la LSA conoce
```

### Otros servicios (menos usado pero cae en el examen)
```
netshareenum          # recursos compartidos (shares SMB)
netshareenumall
enumprinters          # impresoras (relevante para el bug PrinterBug/spooler)
srvinfo               # info del servidor (versión, tipo)
```

---

## ⚔️ Abuso — cuando SÍ tengo permisos (ACL abuse)

Esto es lo que mucha gente no sabe: `rpcclient` no solo lee, también **escribe**. Si por
[[acl-abuse|abuso de ACL]] consigo `GenericAll`/`ForceChangePassword` sobre un usuario, puedo
**resetear su contraseña** sin saber la antigua, directamente por RPC:

```bash
rpcclient -U 'dominio/mi_usuario%mi_pass' <IP>
rpcclient $> setuserinfo2 victima 23 'NuevaPass123!'
#                         └usuario └nivel └contraseña nueva
```
`setuserinfo2 ... 23 ...` = cambiar la contraseña (nivel de info 23). Es la vía RPC equivalente
a `net rpc password` o a `--reset-password` de bloodyAD/pth-net. Exam-friendly: manual, sin MSF.

---

## 🧠 Mental model OSCP
1. ¿Es un DC? (puertos 88/389/445) → `rpcclient -U "" -N <IP>`.
2. `enumdomusers` + `querydispinfo` → `users.txt` (filtrar ruido) **y** mirar descripciones.
3. `getdompwinfo` → conozco el lockout antes de tocar contraseñas.
4. Con la lista → [[asrep-roasting]] (gratis). Con creds → [[kerberoasting]] + BloodHound.
5. Si gano `GenericAll` sobre alguien → `setuserinfo2` para resetear su pass → pivot.

## 🩹 Errores típicos
| Mensaje | Qué significa | Qué hago |
|---|---|---|
| `NT_STATUS_ACCESS_DENIED` al conectar | el DC **no** permite sesión nula | pruebo con credenciales, o [[ldap]] / RID cycling |
| `enumdomusers` vacío pero conecta | SAMR capado para anónimo | **RID cycling** (`--rid-brute` en [[netexec]]) |
| `NT_STATUS_LOGON_FAILURE` | user/pass mal | reviso credenciales / formato `dominio/user%pass` |
| `NT_STATUS_ACCESS_DENIED` en `setuserinfo2` | no tengo ese permiso sobre la víctima | confirmo la ACL en BloodHound antes |

---

## 🔑 Checklist
- [ ] Primer tiro a un DC: `rpcclient -U "" -N <IP>`
- [ ] `enumdomusers` → `users.txt` · `querydispinfo` → ¿passwords en descripciones?
- [ ] `querygroupmem 0x200` → quién es Domain Admin
- [ ] `getdompwinfo` → lockout antes de spraying
- [ ] Recordar que **también escribe**: `setuserinfo2` para reset de pass (ACL abuse)
- [ ] Todo manual, sin Metasploit → exam-friendly

---

## Caso real — Forest (HTB)
`rpcclient -U "" -N` → `enumdomusers` soltó la lista completa. Filtrando el ruido de Exchange
(`SM_*`, `HealthMailbox*`) quedaban los usuarios reales, entre ellos `svc-alfresco`. Esa lista
alimentó el [[asrep-roasting]] sin credenciales → foothold. Es el patrón de [[enumeracion-ad-sin-credenciales]] en acción.
