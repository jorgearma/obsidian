# Kerberos y el KDC — TGT → TGS

> **En una frase:** demuestras quién eres UNA vez (login) y recibes una **pulsera (TGT)**; luego, por cada servicio, cambias la pulsera por un **ticket (TGS)** que presentas al recurso. Todo lo gestiona el **KDC**, que vive en el DC.
> Relacionado: [[ldap]] · [[agdlp]] · [[dns-en-ad]] · [[montar-lab-ad]]

---

## El problema que resuelve
Cada acceso a un recurso del dominio exige demostrar quién eres. ¿Mandar la contraseña cada vez? Peligroso (viajaría mil veces). Kerberos: **demuestras quién eres solo UNA vez** (al loguearte) y luego usas **tickets**, no tu contraseña.

## La analogía — parque de atracciones
```
1. Entras → enseñas el DNI una vez → te dan una PULSERA de día   → TGT
2. Quieres una atracción → enseñas la pulsera en taquilla
                         → te dan un TICKET para esa atracción    → TGS
3. Das el ticket al operador de la atracción → subes             → accedes al servicio
```
La **taquilla** (da pulsera y tickets) = el **KDC** (en el DC).

## Quién es quién
| Pieza | Qué es |
|---|---|
| **Cliente** | Tú / tu PC (CL01 con jan.kowalski) |
| **KDC** | Servicio Kerberos en el DC. 2 ventanillas: **AS** (da TGT) y **TGS** (da tickets de servicio) |
| **Servicio** | El recurso final (share, MSSQL, otro PC...) |

## El flujo (con los nombres de los mensajes)
```
Login:   jan ──AS-REQ──►  KDC(AS)    "soy jan, prueba cifrada con mi contraseña"
         jan ◄──AS-REP──  KDC(AS)    "toma tu TGT" (pulsera, ~10h)

Acceso:  jan ──TGS-REQ─►  KDC(TGS)   "tengo el TGT, dame ticket para \\DC01\share"
         jan ◄──TGS-REP─  KDC(TGS)   "toma el TGS de ese servicio"

Uso:     jan ──AP-REQ──►  el SERVICIO "aquí va mi TGS" → valida → entras
```
> `klist` del lab mostró el resultado del login: el **TGT** (`Server: krbtgt/NORDWIND.LOCAL`, flag `initial`/`pre_authent`).

## TGT vs TGS
| | **TGT** | **TGS** |
|---|---|---|
| Qué es | La **pulsera**: "soy válido" | El **ticket**: "entro a ESTE servicio" |
| Cuándo | Al **loguearte** (una vez) | Cada vez que accedes a **un servicio** |
| A quién lo enseñas | Al **KDC** (para pedir TGSs) | Al **SERVICIO** (para entrar) |
| Clave que lo cifra | la de la cuenta **krbtgt** | la de la **cuenta del servicio** |

**Por qué 2 pasos:** así metes tu contraseña **una sola vez** (para el TGT); luego el TGT pide todos los TGS sin reusar la contraseña. Menos viaja tu secreto = más seguro.

## 🔑 Cada ticket va cifrado con una clave distinta → por eso se ataca
1. **TGT cifrado con la clave de `krbtgt`** (solo el KDC) → robar ese hash = **Golden Ticket** (forjar pulseras para cualquiera).
2. **TGS cifrado con la clave de la cuenta de servicio** → pedir un TGS de una cuenta con **SPN** y llevarte su cifrado = **Kerberoasting** (crackeo offline). *(Fase 2: `svc_sql`.)*
3. **Para sacar el TGT demuestras tu contraseña (pre-autenticación).** Si una cuenta tiene la **pre-auth desactivada**, el AS-REP llega con material cifrado con el hash del user sin pedir nada = **AS-REP Roasting**. *(Fase 2: user sin preauth.)*
4. **El TGT vive en memoria** → robarlo de un PC comprometido = **Pass-the-Ticket**.

## Lo que DEBO recordar (checklist)
- [ ] TGT = pulsera (al entrar). TGS = ticket de un servicio.
- [ ] El TGT se lo enseño al **KDC**; el TGS, al **servicio**.
- [ ] Meto la contraseña **una vez** (para el TGT).
- [ ] Puertos: Kerberos = **88**. Si lo veo abierto → es un DC.
- [ ] Cada ataque Kerberos abusa de **un cifrado** del flujo (krbtgt→Golden, SPN→Kerberoast, sin-preauth→AS-REP, TGT en memoria→PtH).
