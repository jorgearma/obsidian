# NTLM — autenticación por reto-respuesta

> **En una frase:** el protocolo **viejo** de autenticación de Windows. En vez de tickets (eso es Kerberos), el servidor te lanza un **reto** y tú lo respondes demostrando que conoces tu **hash NT** — nunca mandas la contraseña. Que la prueba sea el *hash* (no la contraseña) es justo lo que hace posible el **Pass-the-Hash**.
> Relacionado: [[kerberos-kdc]] · [[trusts]] · [[ldap]] · [[montar-lab-ad]]

---

## El problema que resuelve (y por qué sigue vivo)
Kerberos es el protocolo moderno y preferido en un dominio. Pero Kerberos **necesita un DC alcanzable y nombres (SPN/hostname)**. Cuando eso no se da, Windows cae a NTLM:
- Te conectas **por IP** en vez de por nombre (`\\10.10.10.5\share`).
- Máquina en **workgroup** (sin dominio) o cuentas locales.
- No hay DC accesible / software legacy.

Por eso NTLM está **en todas partes** aunque sea viejo → es superficie de ataque permanente.

## La pieza clave: el hash NT
```
hash NT = MD4( contraseña en UTF-16LE )    ← sin sal, estático
```
- No lleva sal → **la misma contraseña = el mismo hash siempre** (por eso sirve para reutilizar).
- Es lo que se guarda en la **SAM** (local) y en **NTDS.dit** (en el DC).
- **Demuestras que lo conoces sin enviarlo** (reto-respuesta). Y aquí está el truco: si el *hash* es lo que prueba tu identidad... **tener el hash = ser tú.** No hace falta la contraseña.

## El flujo (NTLMv2, reto-respuesta)
```
1. NEGOTIATE   cliente ──► servidor   "quiero autenticarme por NTLM"
2. CHALLENGE   cliente ◄── servidor   "toma este número aleatorio (reto)"
3. RESPONSE    cliente ──► servidor   "respuesta = reto cifrado/HMAC con mi hash NT"
               → el servidor valida. Si la cuenta es de dominio, reenvía la
                 comprobación al DC por el canal Netlogon (pass-through auth).
```

## NTLM vs Kerberos
| | **NTLM** | **Kerberos** |
|---|---|---|
| Edad | Viejo (fallback) | Moderno (preferido) |
| Cómo pruebas | Reto-respuesta con el hash NT | Tickets (TGT/TGS) emitidos por el KDC |
| Necesita DC/nombres | No (sirve por IP, workgroup) | Sí (KDC + SPN/hostname) |
| Dónde lo verás | IP directa, legacy, cuentas locales | Acceso normal por nombre en el dominio |
| Puerto típico | SMB 445 | Kerberos 88 |

## 🔑 Por qué se ataca (y con qué)
1. **Pass-the-Hash (PtH)** — con el **hash NT** te autenticas directamente, sin crackear nada, porque el hash *es* el secreto que calcula la respuesta. Herramientas: impacket `psexec.py/wmiexec.py -hashes :<NT>`, `mimikatz sekurlsa::pth`. → **el ataque estrella de NTLM** (Tramo 2, lateral movement).
2. **Capturar Net-NTLMv2** — un atacante que hace de servidor (`Responder`) recoge el paso 3 (la respuesta al reto) de víctimas de la red. Eso es un **Net-NTLMv2**, que NO sirve para PtH → o lo **crackeas offline** (`hashcat -m 5600`) o lo **relayeas**.
3. **NTLM Relay** — en vez de crackear, **reenvías** esa autenticación a otro servidor que no exige firma SMB y te autenticas como la víctima (`ntlmrelayx.py`).

> ⚠️ **Distinción que confunde a todo el mundo:**
> - **Hash NT** (de SAM/LSASS/NTDS) → se usa **tal cual** para PtH.
> - **Net-NTLMv2** (capturado en red con Responder) → NO sirve para PtH; se **crackea o se relaya**.
> Son cosas distintas aunque las dos se llamen "hash NTLM".

## Dónde encaja en el examen
- **OSCP:** dumpear la SAM/LSASS (`secretsdump.py`, mimikatz) → hashes NT → **PtH** con impacket a otras máquinas = reutilización de credenciales. Muy frecuente.
- **CRTP:** PtH + captura/relay como movimiento lateral dentro del dominio.

## Lo que DEBO recordar (checklist)
- [ ] NTLM = protocolo **viejo**, reto-respuesta; Kerberos lo sustituye pero NTLM nunca muere.
- [ ] Hash NT = `MD4(UTF-16LE(pass))`, **sin sal** → estático y reutilizable.
- [ ] Nunca viaja la contraseña: pruebas que conoces el **hash** → por eso el hash = tú (**PtH**).
- [ ] **Hash NT = PtH directo. Net-NTLMv2 = crackear o relayear.** No confundirlos.
- [ ] Aparece cuando entras por **IP**, en **workgroup**, o sin DC/nombres.
