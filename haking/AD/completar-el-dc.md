# Completar el DC — lo que falta tras Kerberos y los grupos

> **En una frase:** ya entiendes el DC por dentro (LDAP, Kerberos, grupos, OUs). Faltan **3 fundamentos** que sostienen casi todos los ataques de AD: **NT hash/NTLM**, **ACL/ACE/DACL** y **NTDS.dit**. Con estos, Pass-the-Hash, BloodHound y DCSync dejan de ser magia.
> Relacionado: [[kerberos-kdc]] · [[ldap]] · [[agdlp-y-bloodhound]] · [[dns-en-ad]] · [[montar-lab-ad]]

> **Prioridad examen:** 🔥 = fundamento transversal (OSCP + CRTP) · ✅ = CRTP sobre todo · ⚪ = cultura

---

## 🔴 Los 3 fundamentales (apréndetelos de verdad)

### 1. NT hash + NTLM 🔥🔥
Kerberos no es el único protocolo de autenticación de AD. También existe **NTLM**, más viejo, de **reto-respuesta**. Se usa cuando Kerberos no puede:
- te conectas por **IP** en vez de por nombre de host
- equipos **fuera del dominio** / workgroup
- cosas **legacy**

**El NT hash** = cómo se guarda la contraseña de cada usuario. Es un **MD4 sin sal**.

> ⚠️ **Sin sal = el hash ES la contraseña.** No necesitas crackearlo: si lo robas, te autenticas presentando el hash directamente.

```
Contraseña "Verano2026!"  ──MD4──►  NT hash (32 hex)
   El NT hash NO lleva sal → dos usuarios con la misma pass tienen el mismo hash
```

- **Ataque que habilita:** **Pass-the-Hash** (vive en NTLM, NO en Kerberos).
- **Herramientas OSCP:** `psexec.py / wmiexec.py -hashes :<NThash>`
- **Conecta con:** [[kerberos-kdc]] (el otro protocolo). Los dos conviven en todo dominio.

---

### 2. ACL / ACE / DACL 🔥🔥🔥
Cada objeto de AD (usuario, grupo, OU, el propio dominio) lleva una lista de **"quién puede hacerle qué"**:

```
OBJETO (ej: usuario anna)
   └─ DACL  (Discretionary Access Control List)
        ├─ ACE: "jan  puede  ForceChangePassword  sobre anna"
        ├─ ACE: "GG_IT  puede  GenericAll  sobre anna"
        └─ ACE: ...
```

- **DACL** = la lista completa de permisos de un objeto.
- **ACE** = una entrada de esa lista (un permiso concreto).
- Permisos jugosos: `GenericAll`, `GenericWrite`, `WriteDacl`, `WriteOwner`, `ForceChangePassword`, `AddMember`.

> 🩸 **Esto es LO QUE LEE BloodHound.** Come todas las ACL/ACE del dominio y dibuja la ruta más corta a Domain Admin. Sin este concepto, BloodHound te suena a magia; con él, lo entiendes.

- **Ataque que habilita:** abuso de ACLs (meterte en un grupo, cambiar la pass de otro, tomar control de un objeto).
- **Conecta con:** [[agdlp-y-bloodhound]]. Es el motor detrás de las rutas.

---

### 3. NTDS.dit 🔥
Dónde vive **físicamente TODO** AD. Toda la base de datos del dominio —usuarios, grupos, **y todos los hashes**— está en un archivo en el DC:

```
C:\Windows\NTDS\ntds.dit        ← la base de datos
   + la SYSTEM hive del registro ← la clave para descifrarla
```

> 💰 **Premio gordo:** si te llevas `ntds.dit` + la clave, tienes **TODAS las contraseñas del dominio de golpe.**

- **Ataque que habilita:** volcado de hashes → `secretsdump.py` (o copia del archivo vía VSS).
- **Conecta con:** DCSync (ver abajo) saca lo mismo **sin tocar el archivo en disco**.

---

## 🟡 Apéndice — cultura (saber que existen)

### krbtgt — Golden / Silver Ticket ✅ (🔥 en CRTP)
La cuenta **`krbtgt`** es cuya hash **firma TODOS los TGT** del dominio.
- Si robas su hash → **fabricas un TGT falso de quien quieras** (hasta un DA inventado) = **Golden Ticket** = persistencia total.
- **Silver Ticket** = falsificas un **TGS** con el hash de una cuenta de servicio (acceso a 1 servicio, más sigiloso).
- Conecta con [[kerberos-kdc]]: krbtgt es la llave maestra que no vimos al estudiar el KDC.

### Replicación entre DCs → DCSync ✅ (🔥 en CRTP)
Una empresa tiene **varios DC** que **sincronizan** sus datos copiándose entre ellos.
- **DCSync:** un atacante con permisos de replicación le pide a un DC *"replícame las contraseñas"* **fingiendo ser otro DC** → saca hashes **sin tocar `ntds.dit` en disco**.
- Necesita derechos de replicación (DA, o delegados por error).

### Bosque / Dominio / Trusts ✅ (🔥 en CRTP, ⚪ en OSCP)
- **Bosque** = frontera de seguridad real. **Dominio** = partición. Mi lab `nordwind.local` = 1 bosque, 1 dominio.
- **Trusts** = relaciones que dejan a usuarios de un dominio autenticarse en otro.
- **Enterprise Admins** manda sobre todo el bosque.
- OSCP suele ser **1 solo dominio** → trusts casi no salen. CRTP sí (módulo de forest).

### SYSVOL / NETLOGON ⚪
Carpetas compartidas del DC con las **GPO y scripts de inicio**, **legibles por cualquier usuario del dominio**.
- Viejo truco: contraseñas en **GPP** (`cPassword`) guardadas ahí → descifrables.

### Cuentas de equipo · LAPS · gMSA ⚪
- Las máquinas también son cuentas: `CL01$`, `DC01$` (pass aleatoria de 120 chars, rota sola → **incrackeable**, ver [[kerberos-kdc]] por qué no se roastean).
- **LAPS** = contraseña de admin local **única por equipo**.
- **gMSA** = cuentas de servicio con pass gestionada por AD (incrackeable).
- Para qué sirve saberlo: **reconocer cuándo un ataque NO va a funcionar**.

---

## Mapa mental de cierre

```
NÚCLEO (hecho ✅):  LDAP · KDC · TGT/TGS · SPN · AGDLP · OU · SID/RID · delegación · tiers
FUNDAMENTO 🔴:      NT hash/NTLM → Pass-the-Hash
                    ACL/ACE/DACL → BloodHound
                    NTDS.dit     → volcado de hashes
CULTURA 🟡:         krbtgt(Golden) · replicación(→DCSync) · trusts · SYSVOL · LAPS/gMSA
```

> **Regla:** casi todos estos conceptos ya SON ataques. A partir de aquí, aprender un concepto nuevo = aprender a atacarlo. Siguiente paso real = **Fase 2 del lab** (plantar los agujeros con mis propias manos), no más teoría.
