# BloodHound — recolectar el AD y dibujar el camino a Domain Admin

> **En una frase:** BloodHound no "escanea y te da el resultado". Guarda todo el dominio (usuarios, grupos, ACLs, sesiones) como un **grafo de relaciones** y tú le preguntas *caminos*: "¿cómo llego desde esta cuenta hasta Domain Admins?". Un **recolector** (bloodhound-python / SharpHound) saca los datos; la **app** los dibuja.
> Relacionado: [[acl-abuse]] · [[agdlp-y-bloodhound]] · [[kerberoasting]] · [[asrep-roasting]] · [[kerberos-kdc]] · [[montar-lab-ad]]

---

## Las dos piezas (no confundirlas)
| Pieza | Qué es | En mi Kali |
|---|---|---|
| **Recolector** | Se conecta al DC con cualquier credencial y vuelca el dominio a `.json`/`.zip` | `bloodhound-python` (desde Kali, remoto) o `SharpHound.exe` (desde Windows) |
| **App / visor** | Importa esos datos y dibuja el grafo | **BloodHound CE** (Community Edition) |

> **Clave:** el recolector **no sabe ni le importa** que la app exista. Lo corres cuando quieras, en paralelo. Solo necesita **red al DC + reloj OK** (Kerberos ±5 min).

---

## Recolección — `bloodhound-python` (OSCP-friendly, desde Kali)
Lo potente: con las credenciales de **un usuario cualquiera y sin privilegios** (ej. `piotr`), LDAP te deja leer **todo el dominio**. Un solo foothold de bajo nivel → el grafo entero de rutas a DA.

```bash
mkdir -p ~/nordwind-bh && cd ~/nordwind-bh
bloodhound-python -u piotr.wisniewski -p 'Autumn2024!' \
  -d nordwind.local -ns 192.168.10.10 -c All --zip
```
| Flag | Qué hace |
|---|---|
| `-u / -p` | usuario y pass de bajo privilegio (el foothold) |
| `-d nordwind.local` | dominio objetivo |
| `-ns 192.168.10.10` | usa el **DC como DNS** (sin esto no resuelve nombres del dominio) |
| `-c All` | recolecta todo (grupos, ACLs, sesiones, SPNs, trusts…) |
| `--zip` | empaqueta los `.json` en un solo `.zip` listo para subir |

**Output esperado:**
```
INFO: Found 10 users
INFO: Found 14 groups
INFO: Found 2 computers
INFO: Compressing output into 20261018xxxxxx_bloodhound.zip
```
Si suelta `KRB_AP_ERR_SKEW` → es el **reloj** desincronizado: `sudo ntpdate pool.ntp.org` y repites.

---

## Setup de BloodHound CE en Kali (el lío de los 3 passwords)
En Kali actual `bloodhound` a secas está deprecado → se usa `bloodhound-start` (la primera vez pide `bloodhound-setup`). La UI **no** es la web de neo4j, vive en **otro puerto**.

```bash
bloodhound-start        # primera vez: acepta el setup (levanta PostgreSQL + neo4j)
```

**El 90% de los fallos = confundir TRES contraseñas distintas:**
| Contraseña | Para qué | Dónde se pone |
|---|---|---|
| **neo4j** | la base de datos de grafos | la fijas en `http://localhost:7474` (login `neo4j`/`neo4j` → nueva) |
| **neo4j.secret** en `/etc/bhapi/bhapi.json` | que la API *hable* con neo4j | **tiene que ser IDÉNTICA** a la de arriba |
| **default_admin** (`admin`/`admin`) | login de la *web* de BloodHound | ya viene fijo en `bhapi.json` |

```bash
sudo nano /etc/bhapi/bhapi.json   # bloque "neo4j": pon "secret" = la pass real de neo4j
bloodhound-start                   # ahora la API levanta el :8080
ss -tlnp | grep 8080               # confirmar que escucha
```

**Dos puertos, no confundir:**
- **`:7474`** = Neo4j (consolas + botón ▶). Solo lo tocas para cambiar la pass. **NO es BloodHound.**
- **`:8080`** = BloodHound CE de verdad. Login `admin`/`admin`. Aquí subes el zip y ves el grafo.

**Subir datos:** `:8080` → Administration / **File Ingest** → arrastra el `.zip` → Upload → espera a `Complete`.

---

## Cómo LEER el grafo (3 reglas)
**1. Nodos = objetos del AD** (por icono): 👤 usuario · 👥 grupo · 🖥️ equipo · 🌐 dominio.

**2. Flechas (aristas) = qué puede hacer uno sobre otro.** Se leen en el sentido de la flecha:
> **`A ──[RELACIÓN]──► B`** = *"A puede ejercer RELACIÓN sobre B"*.

| Arista | Significado |
|---|---|
| `MemberOf` | A es miembro del grupo B (hereda sus poderes) |
| `ForceChangePassword` | A puede resetear la pass de B sin saber la antigua |
| `GenericAll` | control total de A sobre B |
| `AddMember` | A puede meter miembros en el grupo B |
| `DCSync` | A puede replicar secretos del DC (→ todos los hashes) |

**3. Un "camino" se lee siguiendo las flechas** desde una cuenta comprometida hasta `Domain Admins`. Cada flecha = un paso del ataque.

**Truco que lo hace click:** haz **clic en una flecha** → panel **Help / Abuse Info** → te da el comando exacto para explotar esa relación (Windows Abuse / Linux Abuse). BloodHound te enseña el ataque que hiciste a mano.

---

## El tab Cypher — es un LIENZO, no una hoja de cálculo
> **Regla que me costó una hora:** el editor de Cypher de BloodHound **solo dibuja grafos**. Hay que devolver **nodos (`u`), relaciones (`r`) o caminos (`p`)** — NUNCA `.name` ni `count()`. Si devuelves un número o un texto, no tiene qué dibujar y te suelta **"No results match your criteria"** aunque la query esté perfecta.

> **Otro error que tuve:** pegar la query en la **barra de la lupa** (buscar nodos) en vez de en la **pestaña `</>` Cypher**. La lupa solo busca nombres; "No results match your criteria" ahí = estás en la caja equivocada.

Queries útiles (todas devuelven nodos/relaciones → se dibujan):
```cypher
MATCH (u:User) RETURN u                                  // todos los usuarios
MATCH (u:User) WHERE toLower(u.name) CONTAINS 'piotr' RETURN u   // buscar (case-insensitive)
MATCH (u:User)-[r]->(n) WHERE toLower(u.name) CONTAINS 'piotr' RETURN u, r, n  // qué puede hacer piotr
MATCH p = shortestPath((u {name:'PIOTR.WISNIEWSKI@NORDWIND.LOCAL'})-[*1..]->(g {name:'DOMAIN ADMINS@NORDWIND.LOCAL'})) RETURN p  // camino concreto
```
Query predefinida (botón, no escribes nombres): **"Find Shortest Paths to Domain Admins"** → dibuja TODAS las rutas del dominio a DA.

---

## 🏆 Lección de oro — BloodHound es una FOTO del momento (lab, 2026-10-18)
Hoy ataqué mi lab a mano y **gané** (robert → Domain Admins, confirmado con DCSync). Pero cuando monté BloodHound **después**, el camino `piotr → robert → Domain Admins` **no aparecía**. ¿Por qué?

> **BloodHound solo sabe lo que había en el instante de la recolección.** Yo recolecté *después* de explotar, cuando la cadena ya estaba rota.

Y lo rompió **mi propia defensa #4 de [[acl-abuse]]: AdminSDHolder / SDProp**, actuando a **dos niveles**:
1. Al meter a robert en Domain Admins, borró el `GenericAll` de robert sobre el grupo (grupo protegido, ACL restaurada cada ~60 min).
2. robert, al ser miembro de DA, se volvió **cuenta protegida** (`adminCount=1`) → SDProp reescribió **también la ACL de robert** → borró el `ForceChangePassword` que piotr tenía sobre él.

Diagnóstico en BloodHound: `MATCH (u:User)-[r]->(n) WHERE toLower(u.name) CONTAINS 'piotr' RETURN u,r,n` → piotr solo tenía `MemberOf → Domain Users`. **Pelado.** La cadena se había desmantelado sola.

### La regla que me llevo (de examen real)
> **BloodHound PRIMERO, explotar DESPUÉS.** Se recolecta al inicio del engagement, con el AD en su estado vulnerable intacto. Si recolectas después de romper cosas, la foto sale "después del crimen" y las rutas que usaste pueden haber caducado. Además: **el grafo puede mostrar rutas ya muertas** (SDProp revierte en <1h) — la foto no garantiza que la arista siga viva en el momento del ataque.

---

## Dónde encaja en el OSCP
- El **set de AD (40 pts)**: comprometes una cuenta cualquiera → BloodHound desde Kali con `bloodhound-python` → "Shortest path to Domain Admins" → sigues las flechas.
- **OSCP-friendly:** `bloodhound-python` es manual y sin Metasploit. El flujo real: AS-REP/Kerberoasting → foothold → **recolectar YA** → analizar grafo → ejecutar la ruta.
- Máquinas calcadas a esto: HTB **Forest** y **Sauna** (AS-REP → BloodHound → DCSync).
