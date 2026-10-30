# 🗺️ MOC — Active Directory

> Mapa de contenido (índice) de toda la carpeta AD. **Empieza por aquí.**
> Orden pensado como ruta de aprendizaje: entender → enumerar → atacar → practicar en lab.
> Gap principal de mi OSCP → aquí voy a máxima profundidad.

---

## 0 · Fundamentos — entender antes de atacar

Empieza por el índice conceptual y baja:

- 🥇 [[los-5-pilares-de-ad]] — **el mapa mental.** Qué entender de verdad y en qué orden
- [[kerberos-kdc]] — el rey: TGT → TGS, por qué cada ticket se puede atacar
- [[ntlm]] — autenticación reto-respuesta, el hash NT, Pass-the-Hash
- [[ldap]] — la "guía telefónica" de AD (árbol, DN, enumeración) · 🌳 visual: `lab-nordwind/ldap-arbol.html`
- [[dns-en-ad]] — por qué AD depende del DNS, registros SRV, AXFR
- [[agdlp-y-bloodhound]] — cómo se anidan los grupos y por qué importa al atacante
- [[trusts]] — confianza entre dominios/bosques
- [[fundamentos-del-dc]] — NT hash · ACL/ACE/DACL · NTDS.dit · Golden Ticket · DCSync

## 1 · Enumeración

- [[sacar-nombre-de-dominio]] — dominio / FQDN / hostname (netexec, nmap, ldap, rpcclient)
- [[enumeracion-ad-sin-credenciales]] — ⭐ sacar usuarios sin login (rpcclient null, RIDs, kerbrute)

## 2 · Ataques

- [[asrep-roasting]] — cuentas sin pre-auth → hash crackeable **sin credenciales**
- [[kerberoasting]] — cuentas de servicio con SPN (necesita credenciales)
- [[bloodhound]] — recolectar el AD y dibujar el camino a Domain Admin
- [[acl-abuse]] — encadenar permisos (ACL/ACE) hasta Domain Admin

## 🧰 Tools de AD (`AD/tools/`)

- [[rpcclient]] — enumeración (y abuso) de AD por MS-RPC · sesión nula · `setuserinfo2`
- [[impacket]] — suite de ataque AD en Python (GetNPUsers, GetUserSPNs, secretsdump, psexec...)
- [[netexec]] — barrido y validación de credenciales en AD/SMB (el `(Pwn3d!)`)
- [[evil-winrm]] — shell remota por WinRM (5985) · upload/download · Pass-the-Hash (`-H`)
- Cracking → [[hashcat]] vive en `tools/` general (es transversal: AD + Linux + web)

## 🧪 Lab Nordwind Logistics

- [[montar-lab-ad]] — construir el lab desde cero (build → sabotear → atacar)
- Visualizaciones interactivas (abrir con doble clic en navegador, funcionan sin conexión):
  - `lab-nordwind/explorador-ad.html` — explorador del dominio Nordwind
  - `lab-nordwind/ldap-arbol.html` — árbol LDAP navegable
  - `lab-nordwind/permisos-corp.html` — permisos de la corp

---

## 🎯 Ruta rápida para el examen (mínimo vital)

```
Es DC → sacar-nombre-de-dominio → enumeracion-ad-sin-credenciales (users.txt)
     → asrep-roasting (gratis, sin creds)
     → con creds: kerberoasting + bloodhound → acl-abuse → Domain Admin
```

## ⏳ Pendientes (notas por crear)

- [ ] `sharphound-y-edges` — detalle de los edges de BloodHound (referenciada en [[agdlp-y-bloodhound]])
- [ ] Windows privesc (WinPEAS, SeImpersonate, servicios escriturables) — aún no cubierto
- [ ] Pass-the-Hash / Pass-the-Ticket — nota propia
- [ ] DCSync como nota independiente (hoy vive dentro de [[fundamentos-del-dc]])
