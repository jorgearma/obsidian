# DNS en Active Directory

> **Qué es esto:** cómo funciona DNS dentro de AD y por qué para un atacante es (1) la huella para identificar el DC, (2) una vía de enumeración de la red interna, y (3) un requisito técnico sin el cual Kerberos no funciona.
> **Conecta con:** [[montar-lab-ad]] · [[reconocimiento-dns-pentesting]] · [[metodologia]]

**Idea en una frase:** en AD, DNS no solo traduce nombres a IPs — **resuelve servicios**. Los clientes preguntan a DNS *"¿quién hace de DC aquí?"* antes de autenticarse. Por eso **el DNS casi siempre vive en el propio DC**.

---

## 1. Por qué AD depende del DNS

Un cliente recién encendido no sabe dónde está el Domain Controller. Lo **descubre preguntando a DNS**. Antes de hacer login, aplicar GPOs o pedir un ticket Kerberos, lanza una consulta DNS del tipo *"¿quién ofrece el servicio Kerberos en este dominio?"*.

Eso se hace con los **registros SRV** (service records): el mecanismo que diferencia DNS normal de DNS en AD.

```
   ┌─────────────┐                               ┌────────────────────┐
   │  Cliente     │  "¿Dónde está el DC de        │  DNS Server         │
   │ (CL01)      │   nordwind.local p/ Kerberos?" │  (= el propio DC)   │
   │             │ ───────────────────────────►  │                     │
   │             │  "Es DC01, 192.168.10.10 :88"  │                     │
   │             │ ◄───────────────────────────  │                     │
   └─────────────┘                               └────────────────────┘
          │  Ahora va directo a DC01:88 a pedir ticket Kerberos
          ▼
   ┌─────────────┐
   │  DC01       │  = DNS + Kerberos(KDC) + LDAP + Catálogo Global
   └─────────────┘
```

> **Pista OSCP #1 — identificar el DC:** si nmap muestra **53 (DNS) + 88 (Kerberos) + 389 (LDAP)** juntos en un host → es el Domain Controller. Esa combinación de puertos es su huella digital.

---

## 2. Registros SRV: el corazón de AD

Formato:

```
_servicio._protocolo.dominio   →   prioridad  peso  puerto  host-destino
```

Los que importan en AD:

| Registro | Para qué | Puerto |
|---|---|---|
| `_ldap._tcp.dc._msdcs.nordwind.local` | encontrar DCs | 389 |
| `_kerberos._tcp.nordwind.local` | dónde autenticar (Kerberos) | 88 |
| `_kerberos._udp.nordwind.local` | idem (UDP) | 88 |
| `_gc._tcp.nordwind.local` | Catálogo Global | 3268 |
| `_kpasswd._tcp.nordwind.local` | cambiar password | 464 |
| `_ldap._tcp.pdc._msdcs.nordwind.local` | el PDC emulator | 389 |

La subzona especial **`_msdcs`** es la de localización de DCs. Si la listas, ves **todos los DCs del bosque**. Es oro en enumeración.

---

## 3. Jerarquía de zonas DNS

```
nordwind.local                      ← zona del dominio
│
├── dc01            A    192.168.10.10   ← registro A: nombre → IP
├── cl01            A    192.168.10.100
│
├── _msdcs.nordwind.local            ← SUBZONA de localización de DCs
│   └── dc._msdcs
│       └── _ldap._tcp  SRV → dc01.nordwind.local:389
│
├── _tcp.nordwind.local              ← servicios sobre TCP
│   ├── _ldap        SRV → dc01:389
│   ├── _kerberos    SRV → dc01:88
│   └── _gc          SRV → dc01:3268
│
└── _udp.nordwind.local              ← servicios sobre UDP
    └── _kerberos    SRV → dc01:88
```

| Tipo | Qué hace | Uso ofensivo |
|---|---|---|
| **A** | nombre → IP | mapear hosts internos |
| **SRV** | servicio → host que lo ofrece | localizar el DC y sus servicios |
| **PTR** | IP → nombre (DNS inverso) | mapear la red interna tras pivotar |

---

## 4. AD-Integrated DNS (el concepto que lo cambia todo)

En DNS clásico los registros viven en **archivos de texto** en el servidor. En AD pueden estar **integrados en AD**: se guardan **dentro de la base de datos (NTDS.dit), replicados vía LDAP** junto con usuarios, grupos y máquinas.

```
   DNS clásico                      AD-Integrated DNS
   ───────────                      ─────────────────
   zona = archivo .dns         vs.  zona = objetos dentro de AD/LDAP
   replicación manual               replicación automática entre DCs
   lo gestiona el admin DNS         lo gestionan los DCs y cuentas de máquina
```

**Dos consecuencias ofensivas:**
1. **Cualquier usuario autenticado del dominio puede consultar la zona por LDAP** → enumeras máquinas internas sin tocar el servicio DNS directamente.
2. Por defecto **las cuentas de máquina pueden crear/modificar registros DNS** (Dynamic Updates) → abre envenenamiento DNS/DHCP (nivel avanzado, pero conviene saberlo).

---

## 5. Explotación práctica (manual, OSCP exam-friendly)

### a) Transferencia de zona (AXFR) — jackpot si está mal configurado

Te descargas **toda la zona de golpe**: cada host, cada IP, cada DC.

```bash
dig axfr nordwind.local @192.168.10.10
```

**Output si funciona** (vomita la zona entera):
```
nordwind.local.        IN SOA  dc01.nordwind.local. ...
dc01.nordwind.local.   IN A    192.168.10.10
cl01.nordwind.local.   IN A    192.168.10.100
fileserver.nordwind.local. IN A 192.168.10.20
```
Si sale `Transfer failed` / `connection timed out` → bien configurado, no permite AXFR (lo normal). Cuando funciona, es regalo.

### b) Preguntar por los SRV (funciona siempre que tengas acceso al DNS)

```bash
# ¿Dónde están los DCs? (la query estrella)
nslookup -type=SRV _ldap._tcp.dc._msdcs.nordwind.local 192.168.10.10

# Equivalente con dig
dig SRV _ldap._tcp.dc._msdcs.nordwind.local @192.168.10.10
dig SRV _kerberos._tcp.nordwind.local @192.168.10.10
```

**Output esperado:**
```
_ldap._tcp.dc._msdcs.nordwind.local.  SRV  0 100 389 dc01.nordwind.local.
dc01.nordwind.local.                  A    192.168.10.10
```

### c) Desde nmap

```bash
nmap -p 53,88,389,445 --script=dns-srv-enum,ldap-rootdse 192.168.10.10
```

---

## 6. Flujo de decisión en el examen

```
Escaneas máquina Windows
        │
        ▼
¿Puertos 53 + 88 + 389 juntos?
        │
   SÍ ──┴── NO → Windows normal, no DC
   │
   ▼
¡Es un Domain Controller! → Fase AD
   │
   ├─ 1. dig axfr dominio @IP        (¿AXFR abierto? jackpot)
   ├─ 2. nslookup -type=SRV ...      (confirmar DCs, FQDN, IPs)
   ├─ 3. Añadir el FQDN a /etc/hosts  ← CRÍTICO (abajo)
   └─ 4. rpcclient / ldapsearch / enum4linux-ng
```

> **Pista OSCP #2 — la que más tiempo salva:** Kerberos **no funciona por IP, solo por nombre**. Si lanzas `GetUserSPNs.py` o `GetNPUsers.py` contra la IP pelada → error feo (`KRB_AP_ERR_SKEW` o fallo de resolución). Arréglalo mapeando el nombre en Kali:

```bash
# /etc/hosts en Kali
192.168.10.10   nordwind.local dc01.nordwind.local dc01
```

Y sincroniza el reloj con el DC (Kerberos es quisquilloso con la hora):
```bash
sudo ntpdate 192.168.10.10    # o rdate / timedatectl
```

---

## TL;DR

- DNS en AD = directorio telefónico de **servicios**, no solo de nombres.
- **53+88+389 juntos = DC.**
- Enumera: `dig axfr` (si abierto) → `nslookup -type=SRV _ldap._tcp.dc._msdcs.<dom>`.
- Antes de cualquier ataque Kerberos: **FQDN en `/etc/hosts` + reloj sincronizado.**

## Pendiente (siguiente nota)
- [ ] [[enumeracion-ad-sin-credenciales]] — rpcclient `-U "" -N`, ldapsearch, enum4linux-ng
- [ ] Probar AXFR y SRV contra DC01 en mi lab [[montar-lab-ad]] y pegar output real aquí
