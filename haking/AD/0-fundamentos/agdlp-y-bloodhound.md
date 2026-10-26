# AGDLP y BloodHound

> **Qué es esto:** por qué AGDLP (el diseño limpio de permisos vía grupos anidados) y BloodHound aparecen siempre juntos — AGDLP es *cómo* se encadenan los permisos, BloodHound es la herramienta que *recorre* esa cadena para encontrar la ruta a Domain Admin.
> **Conecta con:** [[dns-en-ad]] · [[montar-lab-ad]] · [[metodologia]]

**Idea en una frase:** el `MemberOf` que ves repetido en BloodHound **es literalmente** el anidamiento G→DL de AGDLP. BloodHound convierte ese anidamiento en un grafo y te calcula la ruta de ataque que lo atraviesa.

---

## 1. Qué es AGDLP

Nemotécnica de Microsoft para asignar permisos usando **grupos anidados**, no usuarios sueltos. Las siglas son el orden del anidamiento:

```
A  →  G  →  DL  →  P
│     │     │      │
│     │     │      └─ Permission        (el permiso real sobre un recurso)
│     │     └──────── Domain Local group (grupo que AGRUPA el permiso)
│     └────────────── Global group       (grupo que AGRUPA usuarios por rol)
└──────────────────── Account            (el usuario / la cuenta)
```

Se lee: **A**ccounts → dentro de grupos **G**lobal → dentro de grupos **D**omain **L**ocal → a los que se asigna el **P**ermiso.

### El porqué (esto importa, no la sigla)

Separa el **"quién eres"** del **"qué puedes tocar"**:

| Grupo | Responde a | Agrupa |
|---|---|---|
| **Global (G)** | ¿quién eres en la organización? (rol) | **personas** por rol: "RRHH", "Admins TI" |
| **Domain Local (DL)** | ¿qué da acceso a este recurso? | **permisos**: "Lectura Nóminas", "Admin FILE01" |

Ventaja: cuando alguien cambia de puesto, lo mueves de grupo Global y hereda/pierde recursos **sin tocar la ACL de cada carpeta**.

### Ejemplo

```
Jorge (Account)
   └─ MemberOf → GG_Contabilidad (Global: "soy de contabilidad")
                    └─ MemberOf → DL_Nominas_Lectura (Domain Local)
                                     └─ tiene → READ sobre \\FILE01\Nominas
```

Jorge lee Nóminas, pero **el permiso nunca se le dio a él directo** — lo heredó recorriendo la cadena.

---

## 2. Por qué esto te importa como atacante

Los permisos se heredan **a través del anidamiento**, y la cadena puede tener muchos saltos:

```
Usuario → GG_Soporte → DL_Helpdesk → GG_Admins_WS → DL_Admin_FILE01 → ...
```

Windows te muestra a mano solo el primer nivel. Nadie sigue eso en un dominio con cientos de grupos. **Ahí entra BloodHound.**

---

## 3. BloodHound: nodos, aristas y por qué va con AGDLP

SharpHound recolecta (usuarios, grupos, membresías, ACLs, sesiones) → BloodHound lo mete en un grafo (Neo4j) → le preguntas *"¿camino más corto de este usuario a Domain Admin?"*.

Esos caminos **son las cadenas AGDLP** (+ abusos de ACL):

```
 [Usuario] ──MemberOf──► [GG_Grupo] ──MemberOf──► [DL_Grupo] ──GenericAll──► [Objetivo]
  (nodo)     (arista)      (nodo)      (arista)     (nodo)       (arista)      (nodo)
```

- **Nodos** (círculos): usuarios, grupos, equipos, GPOs, dominios.
- **Aristas / edges** (flechas): la relación.

| Edge | Qué significa | Relación con AGDLP |
|---|---|---|
| `MemberOf` | X es miembro del grupo Y | **es el anidamiento A→G→DL** |
| `AdminTo` | X es admin local de la máquina Y | el resultado del "P" (permiso) |
| `GenericAll` / `GenericWrite` | control total / escritura sobre objeto | abuso de ACL (fuera de AGDLP sano) |
| `HasSession` | sesión de ese usuario en esa máquina | de dónde robar credenciales |
| `ForceChangePassword`, `CanRDP`, `Owns` | otros vectores | rutas de escalada |

> **La clave:** el atacante no necesita que la red use AGDLP perfecto — al revés, los **errores** sobre esa estructura (un Global donde no debe, un `GenericAll` mal puesto, un usuario normal dentro de un DL potente) son justo lo que BloodHound resalta como camino corto a DA.

---

## 4. En el examen OSCP

```
Consigues credenciales de dominio (AS-REP / Kerberoast / password spray)
        │
        ▼
Recolectas el grafo con SharpHound:
   # desde Windows comprometido:
   .\SharpHound.exe -c All
   # remoto desde Kali:
   bloodhound-python -u jorge -p 'Pass123' -d nordwind.local -ns 192.168.10.10 -c All
        │
        ▼
Importas el .zip en BloodHound (GUI) → "Shortest Path to Domain Admins"
        │
        ▼
Sigues las flechas: MemberOf → MemberOf → AdminTo / GenericAll → Domain Admin
```

> **OSCP exam-friendly:** BloodHound para *analizar* rutas SÍ está permitido (es visualización, no explotación automática). El abuso que te sugiere lo ejecutas **a mano** (PowerView, impacket, `net`, etc.), no con Metasploit.

---

## TL;DR

- **AGDLP** = Account → Global → Domain Local → Permission. Separa "quién eres" de "qué tocas".
- `MemberOf` en BloodHound = la G→DL de AGDLP.
- **BloodHound dibuja el anidamiento como grafo y calcula la ruta a Domain Admin.**
- Recolectas con **SharpHound** (`-c All`), analizas "Shortest Path to Domain Admins", explotas los edges **a mano**.

## Pendiente (siguiente nota)
- [ ] [[enumeracion-ad-sin-credenciales]] — rpcclient, ldapsearch, enum4linux-ng
- [ ] [[sharphound-y-edges]] — lectura detallada de cada edge y cómo abusarlo
- [ ] En mi lab [[montar-lab-ad]] fase 2: plantar una cadena AGDLP rota y encontrarla con BloodHound en fase 3
