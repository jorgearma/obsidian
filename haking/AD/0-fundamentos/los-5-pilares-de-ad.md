# AD — Qué entender de verdad (los 5 pilares)

> **Qué es esto:** la diferencia entre "saber teclear la herramienta" y **tener nivel real** en AD. Las herramientas son fáciles; lo difícil (y lo que da nivel) son los **conceptos** que hay debajo. Aquí están los pocos que NO te puedes saltar.
> **Conecta con:** [[sacar-nombre-de-dominio]] · [[dns-en-ad]] · [[enumeracion-ad-sin-credenciales]] · [[metodologia]] · [[montar-lab-ad]]

**Idea en una frase:** si te quito la herramienta y sabes explicar **qué hace y por qué funciona**, tienes nivel. Si solo sabes el comando, eres copia-pega.

---

## 0. El giro mental: usar ≠ entender

Casi todas las herramientas de AD se usan con una línea. Lo difícil no es teclearlas, es **entender el protocolo que explotan**.

| Herramienta | Usarla | Concepto detrás | Lo que de verdad cuesta |
|---|:--:|:--:|---|
| netexec | 🟢 | 🟡 | qué enumerar y leer el output |
| rpcclient | 🟢 | 🟡 | qué es RPC / sesión nula |
| ldapsearch | 🟡 | 🟠 | la estructura de AD |
| kerbrute | 🟢 | 🟡 | enum de usuarios vía Kerberos |
| **GetNPUsers** (AS-REP) | 🟢 | 🔴 | **pre-autenticación Kerberos** |
| **GetUserSPNs** (Kerberoast) | 🟢 | 🔴 | **SPNs y tickets TGS** |
| hashcat | 🟡 | 🟡 | modos y reglas |
| **BloodHound** | 🟡 | 🔴 | **leer el grafo = entender ACLs** |
| evil-winrm | 🟢 | 🟢 | casi nada |
| **secretsdump** (DCSync) | 🟢 | 🔴 | **replicación (DRSUAPI)** |
| mimikatz | 🟡 | 🔴 | LSASS, tickets, SSPs |
| **PowerView** | 🟠 | 🔴 | **ACLs y objetos de AD** |
| PtH (psexec -hashes) | 🟢 | 🔴 | **por qué un hash = una contraseña** |

> La columna "usarla" es casi toda verde. La columna "concepto" tiene el rojo. **Ahí está el nivel.**

---

## Los 5 pilares (en orden de prioridad)

### 1. 🥇 Kerberos — EL rey (máximo ROI)

Entender el baile: `AS-REQ → AS-REP (TGT) → TGS-REQ → TGS-REP`. Qué es la **pre-autenticación**, un **TGT** y un **TGS**.

**Qué desbloquea:** AS-REP Roasting · Kerberoasting · Pass-the-Ticket · Golden/Silver tickets · delegación.
> Media docena de ataques salen de **un solo protocolo**. Si estudias UNA cosa a fondo, que sea esta.

Nota futura: [[kerberos-kdc]]

---

### 2. 🥈 NTLM y Pass-the-Hash

Qué es un hash NT y **por qué para autenticarte por NTLM el hash ES la contraseña** (no hace falta crackearlo).

**Qué desbloquea:** PtH · por qué `secretsdump` da poder · movimiento lateral reutilizando hashes.
> El "ajá" de *"¿no necesito la contraseña en claro?"* es un salto de nivel.

Nota futura: [[ntlm]]

---

### 3. 🥉 ACLs / DACLs (permisos sobre objetos)

Qué es una **ACE**, qué significan **GenericAll · WriteDacl · WriteOwner · GenericWrite**, y **cómo se encadenan**.

**Qué desbloquea:** TODO BloodHound · la escalada de Forest (Account Operators → WriteDacl → DCSync).
> Sin esto, BloodHound te pinta flechas que no sabes traducir a comandos.

Nota futura: [[acl-abuse]]

---

### 4. Estructura de AD / LDAP

Objetos · OUs · atributos · **SID/RID** · grupos · **membresía anidada** (un grupo dentro de otro hereda permisos).

**Qué desbloquea:** enumeración con sentido · entender *por qué* un usuario hereda permisos que no parecía tener.

Nota futura: [[ldap]]

---

### 5. DCSync / Replicación

Por qué un usuario con el permiso adecuado puede **pedirle al DC que le replique los hashes**, como si fuera otro DC.

**Qué desbloquea:** el golpe final de casi todo AD. Es "hacerse pasar por un Domain Controller".

Nota futura: [[fundamentos-del-dc]]

---

## El test honesto de "¿tengo nivel?"

> **Si te quito la herramienta, ¿sabes explicar QUÉ hace y POR QUÉ funciona?**

- ❌ "AS-REP Roasting es `GetNPUsers`" → copia-pega.
- ✅ "AS-REP Roasting funciona porque una cuenta sin pre-autenticación hace que el KDC me entregue un AS-REP con un bloque cifrado con el hash de su contraseña, que crackeo offline" → **nivel real**.

Cuando puedas contar el ataque como una **historia del protocolo** sin nombrar la herramienta → lo tienes.

---

## Mínimo vital (si priorizas)

> **Domina Kerberos + NTLM/PtH + ACLs.** Con esos tres explicas la mitad de cualquier máquina de AD. LDAP y DCSync los rematas enseguida.

No son 50 cosas difíciles: son **5 pilares**, y Kerberos pesa como tres. Las ~20 herramientas son la parte fácil.

---

## TL;DR

- Las herramientas son fáciles de **usar**; lo difícil es el **concepto** → ahí está el nivel.
- **5 pilares:** Kerberos (🥇) · NTLM/PtH (🥈) · ACLs (🥉) · estructura AD/LDAP · DCSync.
- Test de nivel: **explica el ataque sin nombrar la herramienta.**
- Prioridad: **Kerberos primero** (máximo retorno).

## Forest toca 4 de los 5 pilares
Kerberos (AS-REP) · estructura AD (anidamiento de grupos) · ACLs (WriteDacl) · DCSync. Por eso es la máquina ideal para arrancar el gap AD.

## Pendiente
- [ ] Escribir las notas de cada pilar, empezando por [[kerberos-kdc]].
- [ ] Autoevaluación: ¿puedo explicar los 5 sin mirar? (marcar fecha cuando sí)
