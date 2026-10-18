# LDAP — la guía telefónica de Active Directory

> **En una frase:** LDAP = la **base de datos de QUIÉN existe** en el dominio (usuarios, grupos, equipos, OUs) **+ el idioma para consultarla**. Guarda **quién SON** y **qué TIENEN**, NO lo que hacen.
> Relacionado: [[kerberos-kdc]] · [[agdlp]] · [[dns-en-ad]] · [[montar-lab-ad]]
>
> 🌳 **Versión visual interactiva:** abre el archivo `ldap-arbol.html` (en esta misma carpeta `AD/`) con doble clic en el navegador → árbol navegable + recorrido "la lógica en 3 niveles" + el DN de cada nodo en vivo. Funciona sin conexión.

---

## 1. Qué es (y qué NO es)

**LDAP = Lightweight Directory Access Protocol.** Son dos cosas en una:
1. **El directorio** = la base de datos en árbol donde vive TODO el AD.
2. **El protocolo** = el "idioma" para preguntarle cosas a esa base de datos.

### ⚠️ El error típico (evítalo)
LDAP guarda lo que **EXISTE y sus propiedades**, NO la **actividad** de los usuarios.

| LDAP SÍ (quién son / qué tienen) | LDAP NO (qué hacen) |
|---|---|
| Qué usuarios/grupos/equipos existen | A qué hora hicieron login |
| De qué grupos es miembro un user | Qué archivos abrieron |
| Atributos: departamento, descripción, email, SPN | Qué comandos ejecutaron |
| La estructura de OUs | Intentos fallidos de acceso |

> "Qué hacen" = **logs de eventos / auditoría** (Event Viewer, SIEM). Eso es OTRO sistema, no LDAP.

### La analogía que lo fija
LDAP es el **fichero de RRHH / organigrama** de la empresa (quién trabaja, en qué depto, en qué equipos). **NO** es la cámara de seguridad que graba qué hizo cada uno.

### No es "de los admins"
Lo consultan admins, el propio sistema (CL01 pregunta a LDAP de qué grupos es jan.kowalski) **y el atacante** (recon con `ldapsearch`).

---

## 2. Visual: el árbol LDAP de mi lab (Nordwind)

El directorio es un **árbol jerárquico**. Así se ve `nordwind.local`:

```
                    DC=nordwind,DC=local              ← la raíz (el dominio)
                           │
          ┌────────────────┼───────────────────┐
          │                │                    │
   (contenedores        OU=Nordwind         CN=Users, CN=Computers
    por defecto)            │                 (los de fábrica)
                            │
     ┌──────────┬──────────┼──────────┬──────────────┐
     │          │          │          │              │
  OU=_Admins  OU=Users  OU=Computers OU=Groups   OU=ServiceAccounts
                 │                       │
        ┌────────┼────────┐        ┌─────┴─────┐
        │        │        │        │           │
     OU=IT   OU=Sales OU=Management OU=Security OU=Distribution
        │                                │
   ┌────┴────┐                      ┌────┴──────────────┐
   │         │                      │                   │
CN=Piotr  CN=Katarzyna     CN=G_Management_Users  CN=DL_FS01_Sales_Modify
(usuarios)                      (grupos)
```

- Cada **nodo** es un **objeto** (usuario, grupo, OU, equipo).
- Las **OU** son ramas (carpetas); los **usuarios/grupos** son hojas.
- `CN` = Common Name (objeto hoja) · `OU` = Organizational Unit (rama) · `DC` = Domain Component (el dominio troceado).

---

## 3. Visual: el DN (Distinguished Name) = la dirección postal

Cada objeto tiene una ruta **única** que lo localiza. Se lee **de lo específico (izq) a lo general (der)**:

```
CN=G_Management_Users , OU=Security , OU=Groups , OU=Nordwind , DC=nordwind , DC=local
└──── el objeto ─────┘ └─ carpeta ─┘ └ carpeta ┘ └ carpeta ─┘ └──── el dominio ────┘
       (hoja)              padre       abuelo      ...            (la raíz del árbol)
```

> Es como una ruta de carpetas pero **al revés**:
> `local → nordwind → Nordwind → Groups → Security → G_Management_Users`

**Por qué importa:** al enumerar con `ldapsearch` indicas un **DN base** (`-b`) = desde qué rama empiezas a buscar.

---

## 4. Visual: cómo viaja una consulta LDAP

```
   ATACANTE / sistema / admin                        EL DC (192.168.10.10)
   ┌─────────────────────┐                      ┌──────────────────────────┐
   │ ldapsearch ...      │  ─── pregunta ───►   │  Servicio LDAP (pto 389)  │
   │ "dame los usuarios  │                      │        │                  │
   │  de OU=Users"       │                      │        ▼                  │
   │                     │  ◄── respuesta ───   │   [ Base de datos ]       │
   │  (lista de objetos  │   (objetos + sus     │   usuarios, grupos,       │
   │   + sus atributos)  │    atributos)        │   equipos, OUs, atributos │
   └─────────────────────┘                      └──────────────────────────┘
```

Dos modos de preguntar:
- **Anónimo / sin credenciales:** a veces el DC deja leer algo sin login → recon gratis.
- **Autenticado:** con un usuario del dominio (aunque sea de bajo privilegio) → ves MUCHO más.

---

## 5. Puertos (para el OSCP)

| Puerto | Servicio | Nota |
|---|---|---|
| **389** | LDAP (texto claro / STARTTLS) | el habitual |
| **636** | LDAPS (LDAP sobre SSL/TLS) | cifrado |
| **3268** | Global Catalog (LDAP) | búsqueda en TODO el bosque |
| **3269** | Global Catalog sobre SSL | — |

> 🎯 **Si `nmap` saca 389/636/3268 (+ 88 Kerberos + 53 DNS) → es un Domain Controller.**

---

## 6. Enumeración LDAP (manual, OSCP-friendly, sin Metasploit)

### Sin credenciales (anónimo) — recon inicial
```bash
# Info del dominio (naming contexts) — a veces sale sin login
ldapsearch -x -H ldap://192.168.10.10 -s base namingcontexts

# Volcar todo bajo la raíz del dominio
ldapsearch -x -H ldap://192.168.10.10 -b "DC=nordwind,DC=local"
```
`-x` = autenticación simple · `-H` = host · `-b` = **DN base** desde donde buscar.

### Con credenciales (un usuario cualquiera del dominio)
```bash
ldapsearch -x -H ldap://192.168.10.10 \
  -D "jan.kowalski@nordwind.local" -w 'Nordwind2026!' \
  -b "DC=nordwind,DC=local" "(objectClass=user)" sAMAccountName description memberOf
```
`-D` = usuario (bind DN) · `-w` = password · lo del final = **filtro** + atributos a mostrar.

### Atributos que SIEMPRE miras en pentesting
| Atributo | Por qué te importa |
|---|---|
| `sAMAccountName` | el nombre de login (`jan.kowalski`) |
| `description` / `info` | **¡a veces hay passwords puestas aquí!** clásico |
| `memberOf` | de qué grupos es → privilegios |
| `servicePrincipalName` | tiene SPN → **Kerberoasteable** |
| `userAccountControl` | flags: cuenta deshabilitada, **sin preauth (AS-REP)**, etc. |
| `adminCount=1` | fue/es miembro de un grupo privilegiado |

---

## 7. Cómo encaja con el resto de AD

```
        ┌──────────────── EL DC ────────────────┐
        │                                        │
        │   LDAP  ──►  "¿quién es jan.kowalski   │
        │   (389)      y de qué grupos?"         │
        │                                        │
        │   KDC   ──►  "dale un ticket Kerberos" │  ← ver [[kerberos-kdc]]
        │   (88)                                 │
        │                                        │
        │   DNS   ──►  "¿dónde está el DC?"      │  ← ver [[dns-en-ad]]
        │   (53)                                 │
        └────────────────────────────────────────┘
```
- **LDAP** responde el "quién/qué" (identidades y estructura).
- **KDC** responde el "puedes entrar" (tickets).
- **DNS** responde el "dónde está el DC".
- Los **permisos** (quién accede a qué) se guardan como relaciones en LDAP, organizadas con [[agdlp]]. **BloodHound lee LDAP** para dibujar las rutas de ataque.

---

## 8. Lo que DEBO saber (checklist mental)
- [ ] LDAP = directorio (base de datos) + protocolo. Guarda **quién existe**, no qué hacen.
- [ ] El directorio es un **árbol**; cada objeto tiene un **DN** (dirección única, se lee de derecha a izquierda = dominio → ... → objeto).
- [ ] Puerto **389** (636 cifrado, 3268 global catalog). Verlos = es un DC.
- [ ] Se enumera con **`ldapsearch`** (`-b` = DN base). Anónimo o autenticado.
- [ ] Miro siempre: `description` (passwords!), `memberOf`, `servicePrincipalName`, `userAccountControl`.
- [ ] **BloodHound consulta LDAP** para mapear grupos/permisos → rutas a Domain Admin.
