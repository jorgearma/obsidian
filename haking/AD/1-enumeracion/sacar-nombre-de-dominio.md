# Sacar el nombre del dominio (dominio / FQDN / hostname)

> **Qué es esto:** todas las técnicas para, tras confirmar que un host es un DC, averiguar **cómo se llama** el dominio y la máquina — sin credenciales. Es el **paso 0** de la fase AD: sin el nombre, los ataques Kerberos no funcionan.
> **Conecta con:** [[dns-en-ad]] · [[1. nmap]] · [[enumeracion-ad-sin-credenciales]] · [[metodologia]] · [[montar-lab-ad]]

**Idea en una frase:** antes de atacar nada en AD, fijas la **identidad** del objetivo (nombre del dominio + FQDN del DC) y la metes en `/etc/hosts`. Es lo primero que haces en cuanto nmap te dice "esto es un DC".

---

## 0. Los 3 "nombres" que hay que distinguir

Mucha confusión en AD viene de mezclar estos tres. Son cosas distintas:

| Nombre | Ejemplo (Forest) | Dónde se usa |
|---|---|---|
| **Dominio NetBIOS** (corto, legacy) | `HTB` | logins `HTB\usuario`, herramientas viejas |
| **Dominio DNS / FQDN del dominio** | `htb.local` | Kerberos, LDAP, `/etc/hosts` |
| **Hostname del DC / FQDN del host** | `FOREST` / `FOREST.htb.local` | apuntar ataques al DC concreto |

> **Por qué importa:** algunas herramientas piden el NetBIOS (`HTB`), otras el FQDN (`htb.local`). Si usas el que no es → error. Ten los tres apuntados.

---

## 1. Por qué necesito el nombre SÍ o SÍ

- **Kerberos valida por NOMBRE, no por IP.** `GetNPUsers.py` / `GetUserSPNs.py` / `secretsdump.py` contra la IP pelada → errores crípticos (`KRB_AP_ERR_*`, fallo de resolución).
- Solución: meter el FQDN en `/etc/hosts` (ver §7) **antes** de atacar.

---

## 2. netexec / crackmapexec — la más rápida ⭐

La forma más rápida de sacar dominio + hostname + SO en una sola línea.

```bash
netexec smb 10.10.10.161          # (antes: crackmapexec smb 10.10.10.161)
```

**Output esperado:**
```
SMB  10.10.10.161  445  FOREST  [*] Windows Server 2016 Build 14393 x64 (name:FOREST) (domain:htb.local) (signing:True) (SMBv1:True)
```
- `name:FOREST` → hostname del DC
- `domain:htb.local` → FQDN del dominio
- `signing:True` → SMB signing (relevante para relay, otra nota)

> **Exam-friendly:** ✅ netexec/cme están permitidos en OSCP (no es Metasploit).

---

## 3. nmap con scripts (`-sC`) — la fuente más completa ⭐

El script `smb-os-discovery` te da **todo** de golpe.

```bash
sudo nmap -p 53,88,135,139,389,445,636,3268 -sV -sC 10.10.10.161
```

**Output esperado (el trozo que importa):**
```
| smb-os-discovery:
|   OS: Windows Server 2016 Standard 14393
|   Computer name: FOREST
|   NetBIOS computer name: FOREST
|   Domain name: htb.local
|   Forest name: htb.local
|   FQDN: FOREST.htb.local
```
Aquí lees: dominio = `htb.local`, host = `FOREST`, FQDN = `FOREST.htb.local`. Y el `ldap-rootdse` te confirma `defaultNamingContext: DC=htb,DC=local`.

---

## 4. LDAP anónimo (rootDSE / namingContexts)

Muchos DCs responden a LDAP sin autenticar la consulta base (rootDSE).

```bash
# Lo esencial: el naming context = el dominio
ldapsearch -x -H ldap://10.10.10.161 -s base -b '' namingContexts

# rootDSE completo (da también dnsHostName, nivel funcional, etc.)
ldapsearch -x -H ldap://10.10.10.161 -s base -b '' '(objectclass=*)'
```

**Output esperado:**
```
namingContexts: DC=htb,DC=local          ← dominio = htb.local
dnsHostName: FOREST.htb.local            ← FQDN del DC
```
> **Traducir:** `DC=htb,DC=local` se lee de derecha a izquierda y con puntos → `htb.local`.
> **Exam-friendly:** ✅ manual, limpio, fiable. Mi favorito cuando netexec no está.

---

## 5. rpcclient (sesión nula) — NetBIOS + SID

La sesión nula también suelta el nombre NetBIOS y el SID del dominio.

```bash
rpcclient -U "" -N 10.10.10.161
```
```
rpcclient $> lsaquery
Domain Name: HTB                          ← dominio NetBIOS
Domain Sid: S-1-5-21-3072663084-364016917-1341370565

rpcclient $> querydominfo
Domain:         HTB
Server:
Total Users:    ...
```
> El **SID del dominio** también es útil luego (RID cycling, forjar tickets). Apúntalo.
> Esta misma sesión nula es la que usaremos para sacar la **lista de usuarios** → [[enumeracion-ad-sin-credenciales]].

---

## 6. Otras vías (de respaldo / confirmación)

### a) enum4linux-ng (lo automatiza casi todo)
```bash
enum4linux-ng -A 10.10.10.161
```
En la sección `Domain Information` te muestra Domain/Workgroup y FQDN. Lo malo: mucho ruido. Útil como "red de seguridad".

### b) NetBIOS crudo — nmblookup / nbtscan
```bash
nmblookup -A 10.10.10.161
```
```
        FOREST          <20> -  B <ACTIVE>    ← Server service (hostname)
        HTB             <00> - <GROUP> B ...  ← nombre de dominio/grupo NetBIOS
        HTB             <1C> - <GROUP> B ...  ← <1C> = Domain Controllers (¡es un DC!)
```
> El sufijo **`<1C>`** significa "grupo de Domain Controllers" → confirma DC por NetBIOS.

### c) smbclient — listado null
```bash
smbclient -L //10.10.10.161 -N        # a veces muestra "Domain=[HTB]" en la cabecera
```

### d) Certificado LDAPS (636) — el CN lleva el FQDN
```bash
openssl s_client -connect 10.10.10.161:636 2>/dev/null | openssl x509 -noout -subject
# subject=CN=FOREST.htb.local
```
Útil cuando SMB está capado pero 636 está abierto.

### e) RDP (si 3389 abierto)
```bash
nmap -p 3389 --script rdp-ntlm-info 10.10.10.161
# devuelve Target_Name (dominio NetBIOS), DNS_Domain_Name, DNS_Computer_Name
```

### f) DNS → ver [[dns-en-ad]]
AXFR (`dig axfr`) y registros SRV (`_ldap._tcp.dc._msdcs.<dom>`) para el nombre y el mapa de la red. No lo repito aquí.

---

## Tabla resumen: qué nombre te da cada técnica

| Técnica | NetBIOS (`HTB`) | FQDN dominio (`htb.local`) | Hostname (`FOREST`) | Sin creds |
|---|:--:|:--:|:--:|:--:|
| `netexec smb` | | ✅ | ✅ | ✅ |
| `nmap -sC` (smb-os-discovery) | ✅ | ✅ | ✅ | ✅ |
| `ldapsearch` rootDSE | | ✅ | ✅ (dnsHostName) | ✅ |
| `rpcclient` lsaquery | ✅ | | | ✅ |
| `enum4linux-ng` | ✅ | ✅ | ✅ | ✅ |
| `nmblookup -A` | ✅ | | ✅ | ✅ |
| cert LDAPS (636) | | ✅ | ✅ | ✅ |

> **Orden recomendado:** `netexec` (rápido) → `nmap -sC` (completo) → `ldapsearch` (confirmar) → `rpcclient` (NetBIOS + SID + usuarios).

---

## 7. Paso final: `/etc/hosts` + reloj (OBLIGATORIO antes de Kerberos)

```bash
echo "10.10.10.161 forest.htb.local htb.local FOREST" | sudo tee -a /etc/hosts
sudo ntpdate 10.10.10.161        # sincronizar reloj (Kerberos es quisquilloso con la hora)
# alternativa si falla ntpdate: sudo rdate -n 10.10.10.161
```
> Detalle de por qué, en [[dns-en-ad]] (Pista OSCP #2).

---

## Flujo de decisión (para el examen)

```
nmap confirma DC (53+88+389, y 3268 lo confirma)
        │
        ▼
1. Sacar nombre:  netexec smb IP   →   domain + host
        │         (respaldo: nmap -sC, ldapsearch rootDSE, rpcclient lsaquery)
        ▼
2. /etc/hosts  +  ntpdate            ← CRÍTICO (habilita Kerberos)
        │
        ▼
3. Enumerar sin creds → LISTA DE USUARIOS → [[enumeracion-ad-sin-credenciales]]
```

---

## TL;DR

- **El nombre lo DESCUBRES** con `netexec` / `nmap -sC` / `ldapsearch` / `rpcclient`. `dig` solo **resuelve** un nombre que ya conoces.
- Distingue: **NetBIOS** (`HTB`) ≠ **FQDN dominio** (`htb.local`) ≠ **hostname** (`FOREST`).
- Lo más rápido: `netexec smb IP`. Lo más completo: `nmap -sC` (`smb-os-discovery`).
- En cuanto lo tengas: **`/etc/hosts` + `ntpdate`** → o Kerberos no funciona.

---

## Aplicado a Forest (caso real)

| Dato | Valor |
|---|---|
| Dominio NetBIOS | `HTB` |
| Dominio FQDN | `htb.local` |
| Hostname / FQDN DC | `FOREST` / `FOREST.htb.local` |
| IP | `10.10.10.161` |
| AXFR | denegado (bien configurado) |

## Pendiente
- [ ] Reproducir `netexec`, `ldapsearch rootDSE` y `rpcclient lsaquery` contra mi Forest y pegar **mi** output.
- [ ] Siguiente nota: [[enumeracion-ad-sin-credenciales]] (sacar usuarios con la sesión nula → `svc-alfresco`).
