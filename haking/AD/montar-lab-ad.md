# Montar Lab AD — Nordwind Logistics

> **Qué es esto:** bitácora de construcción de mi propio AD, desde cero y entendiendo cada paso.
> **Base:** repo de Maciej Stawowy (`maciej-stawowy/active-directory-lab`, MIT) — crédito en mi repo.
> **Objetivo doble:** cerrar el gap AD (OSCP) + pieza de portfolio (sysadmin/SOC + pentester).

**Regla de oro:** construir → **inspeccionar** → explicar aquí con mis palabras → solo entonces avanzar.
Nada que no pueda defender en una entrevista. Si no lo entiendo, no sigo.

---

## El plano (lo que vamos a montar)

**Las 3 fases:**
1. **Construir** (admin, sano) ← estamos aquí
2. **Sabotear** (plantar yo los agujeros: SPN, AS-REP, ACL) → entender los ataques
3. **Atacar** (Kerberoasting, AS-REP, PtH, BloodHound → Domain Admin) → write-up

### Red
- Red interna VirtualBox: **`NordwindLAN`** (aislada — nada toca mi LAN de casa)
- Subred: `192.168.10.0/24` · Gateway `.1`
- **DC es el DNS del dominio** (concepto clave: AD vive del DNS)

| Rango | Uso |
|---|---|
| `.10–.19` | Domain Controllers |
| `.20–.49` | Servidores (file, app) |
| `.100–.200` | DHCP clientes |

### Máquinas
| Host | Rol | OS | IP | RAM/vCPU/disco |
|---|---|---|---|---|
| **DC01** | DC (AD DS + DNS + DHCP) | Windows Server 2022 Std (Desktop Exp.) | `192.168.10.10` estática | 4 GB / 2 / 60 GB |
| **CL01** | Cliente de dominio | **Windows 11 Enterprise eval** *(desvío del repo, que usa Win10 Pro — Win10 está EOL oct-2025)* | DHCP | 4 GB / 2 / 40 GB |

> Tengo 30 GB RAM → voy sobradísimo con las dos encendidas.

### Dominio
- Forest root: **`nordwind.local`** · NetBIOS **`NORDWIND`**
- Nivel funcional forest/dominio: **Windows Server 2016**

### Convenciones de nombres
- Host: `[ROL][NN]` → `DC01`, `CL01`, `FS01` (futuro)
- Login (sAMAccountName): `nombre.apellido` → `jan.kowalski`
- UPN: `nombre.apellido@nordwind.local`
- Cuentas privilegiadas: prefijo `adm.` → `adm.jan.kowalski`
- OU de admins: `_Admins` (guion bajo = ordena primero + marca sensible)

### Estructura de OUs
```
nordwind.local
└── Nordwind
    ├── _Admins
    ├── Users
    │   ├── Management / IT / Accounting / Sales / Logistics / Warehouse / HR
    ├── Computers
    │   ├── Workstations
    │   └── Servers
    ├── Groups
    │   ├── Security
    │   └── Distribution
    └── ServiceAccounts
```

### AGDLP (el concepto que más vale)
**A**ccounts → **G**lobal groups → **D**omain **L**ocal groups → **P**ermissions
1. Usuarios → grupo **Global** por rol (`G_Sales_Users`)
2. Grupo global → anidado en grupo **Domain Local** por recurso (`DL_FileServer_Sales_RW`)
3. Permisos SOLO en el Domain Local
→ Un alta nueva = 1 membresía, sin tocar ACLs carpeta a carpeta. *Esto es lo que hace que las rutas de BloodHound tengan sentido luego.*

---

## Orden de montaje (checklist)

### Preparación
- [ ] Descargar ISO Windows Server 2022 (evalcenter, 180 días) — **activar por internet en los 1os 10 días**
- [ ] Descargar ISO Windows 11 Enterprise eval
- [ ] Confirmar VirtualBox 7 instalado
- [ ] Bajar `data/employees.csv` del repo de Maciej
- [ ] Leer su `docs/01-design.md` (ya resumido arriba)

### Fase 1 — Construir (sano)
- [ ] Crear red interna `NordwindLAN` en VirtualBox
- [ ] Crear VM DC01 (4GB/2/60GB) en NordwindLAN
- [x] Instalar Windows Server 2022 (teclado EN-US en el setup para no bloquearse) — **Standard (Desktop Experience)**, Custom install
- [x] IP estática `192.168.10.10`, DNS **`192.168.10.10`** (alineado al doc de Maciej; loopback habría sido equivalente), hostname `DC01` → verificado con `ipconfig /all`
- [x] Instalar rol AD DS → promover a nuevo forest `nordwind.local` (NetBIOS `NORDWIND`) — **HECHO (16 oct)**
- [x] Verificar salud: `Get-ADDomain` / `Get-ADForest` / SRV `_ldap._tcp` resuelve
- [ ] **INSPECCIONAR:** abrir la zona DNS creada + explorar ADUC (objetos/grupos por defecto)  ← *pendiente (verifiqué por PowerShell, falta la GUI)*
- [x] Estructura de OUs creada **a mano** (entendiendo DN + `New-ADOrganizationalUnit`, no por script) → verificado con `Get-ADOrganizationalUnit`
- [x] Copiar `employees.csv` a `C:\LabFiles\` → usuarios creados (1 a mano + bucle) → 10 usuarios bajo `OU=Users`
- [x] Grupos AGDLP: 7 Global (`G_*`) + 7 Domain Local (`DL_FS01_*`) creados → verificado SID/RID
- [x] Anidar G_→DL_ + meter usuarios en su G_ → verificado con `Get-ADPrincipalGroupMembership`
- [x] Crear VM CL01 (Win11 Enterprise, 4GB/2/40GB, EFI+TPM2.0) en NordwindLAN → **instalado, cuenta local `localadmin`**
- [x] Unir CL01 al dominio (`Add-Computer`) + login de usuario de dominio + `klist` (TGT visto) → **FASE 1 CERRADA**
- [ ] Reset de pass de un user (`Set-ADAccountPassword`) → login en CL01
- [ ] **INSPECCIONAR (momento clave):** `klist` en CL01 → ver el ticket Kerberos emitido
- [ ] GPO `GPO-Nordwind-Password-Policy` en raíz → `gpresult /r`
- [ ] Permisos SMB+NTFS en `\\DC01\Sales` → probar como Sales vs HR

### Fase 2 — Sabotear (plantar los agujeros) — LUEGO
- [ ] Crear `svc_sql` + registrar SPN → `setspn -L` (semilla Kerberoasting)
- [ ] Marcar un user "no requiere preauth Kerberos" (semilla AS-REP)
- [ ] Dar a un user raso control (GenericAll/WriteDacl) sobre un grupo (ruta BloodHound)

### Fase 3 — Atacar — CRTP/después

---

## Bitácora (lo que va pasando)

> Aquí apunto: qué hice, qué vi al inspeccionar, qué falló y cómo lo arreglé, qué entendí.

### 2026-10-15
- Decidido el proyecto. Plano montado. Pendiente: lanzar descargas de ISOs.
- DC01 instalado (Win Server 2022 **Standard Desktop Experience**, Custom install, teclado EN-US).
- **Tropiezos de VirtualBox resueltos:**
  - `Ctrl+Alt+Del` no funciona con teclado físico → lo captura el host Linux. Se manda con **Input → Keyboard → Insert Ctrl-Alt-Del**, o con **Host Key (Ctrl derecho) + Supr**. Es la *Secure Attention Sequence* de Windows (antirrobo de credenciales), por eso necesita canal especial.
  - Copy-paste host↔VM: requiere **Shared Clipboard: Bidirectional** (Input → Shared Clipboard) **+ instalar Guest Additions** (Devices → Insert Guest Additions CD → `VBoxWindowsAdditions.exe` → reiniciar). Sin Guest Additions no pega aunque esté en Bidirectional.
  - *Decisión metodológica:* los comandos los TECLEO, no los pego. Entender > automatismo ciego (regla de oro + CLAUDE.md). Guest Additions sí, pero por resolución/ratón, no como muleta de copy-paste.

#### La "trinidad" de red (hostname + IP + DNS) — ENTENDIDA, pendiente de ejecutar/verificar

> Idea global: dar a DC01 una **identidad de red fija y coherente ANTES** de promoverlo a DC. Un DC no puede tener identidad cambiante (ni IP, ni nombre, ni a quién pregunta por DNS).

```powershell
# 1) Confirmar el nombre de la tarjeta (NO cambia nada, solo mira). Ojo a la columna Name.
Get-NetAdapter

# 2) IP estática .10/24 + gateway .1  (servidor = IP fija; si cambiara, el dominio se queda ciego)
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 192.168.10.10 -PrefixLength 24 -DefaultGateway 192.168.10.1

# 3) DNS = sí mismo (127.0.0.1). EL PASO CLAVE: DC01 VA A SER el DNS del dominio,
#    así que debe preguntarse a sí mismo. Si apunta fuera, la promoción falla por DNS.
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 127.0.0.1

# 4) Nombre definitivo ANTES de promover (renombrar un DC ya-promovido es un marrón)
Rename-Computer -NewName "DC01"

# 5) El nombre no toma efecto hasta reiniciar (IP y DNS sí son al momento)
Restart-Computer
```

**Concepto que no se me olvida:** *En AD, el DNS es la guía telefónica del dominio; sin él nadie encuentra al DC.* Los clientes resuelven **SRV records** (`_ldap`, `_kerberos`, `_gc`) para localizar al DC. Esos puertos (88/389/636/3268) son justo lo que veré con `nmap` en un DC real en el examen.

**Verificar tras el reinicio** (`ipconfig /all`): Host Name = `DC01` · IPv4 = `192.168.10.10(Preferred)` · Mask = `255.255.255.0` · Gateway = `192.168.10.1` · DNS = `127.0.0.1`. Si el DNS no sale `127.0.0.1`, **arreglar ANTES de promover**.

### 2026-10-16 — DC01 promovido + OUs + 10 usuarios

> Sesión larga de construcción: de "VM con Windows instalado" a "dominio vivo con usuarios". Todo tecleado, contrastado contra el repo de Maciej (`docs/01-design.md`, `docs/02-ad-notes.md`, `scripts/`, `data/employees.csv`).

#### 1) Trinidad de red — EJECUTADA y verificada
- Ejecutada tal cual (la del 15 oct), con **un ajuste**: el DNS lo fijé a **`192.168.10.10`** (la IP real del DC) en vez de `127.0.0.1`, para ir **fiel al `01-design.md` de Maciej**.
- **Por qué el cambio:** en un DC los dos valores son equivalentes (loopback = él mismo), pero con varios DCs los demás equipos apuntan por IP de red, no por loopback. Acostumbrarse a la IP real = buena higiene.
- `ipconfig /all` confirmó: Host=`DC01`, IPv4=`192.168.10.10`, DNS=`192.168.10.10`. ✅

#### 2) Promoción a Controlador de Dominio
```powershell
# a) Instalar el ROL (binarios + RSAT: ADUC y módulo ActiveDirectory)
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

# b) Promover creando un BOSQUE nuevo (primer DC = no hay forest, se crea)
Install-ADDSForest `
  -DomainName "nordwind.local" `
  -DomainNetbiosName "NORDWIND" `
  -ForestMode "WinThreshold" `   # "WinThreshold" = nivel funcional Windows Server 2016
  -DomainMode "WinThreshold" `
  -InstallDns `                  # instala rol DNS + crea zona nordwind.local con los SRV
  -SafeModeAdministratorPassword (Read-Host -AsSecureString "DSRM password") `
  -Force
```
**Conceptos que fijé:**
- `Install-ADDSForest` (no `Install-ADDSDomainController`) porque es el **primer** DC → hay que **crear** el bosque, no unirse.
- `-InstallDns`: el DC **es** el DNS del dominio → por eso la trinidad apuntaba el DNS a sí mismo. **AD = DNS.**
- **DSRM** = cuenta de recuperación offline del AD (Directory Services Restore Mode). Password aparte, apuntada.
- **FSMO:** `Get-ADForest` mostró `SchemaMaster : DC01.nordwind.local`. Al ser único DC, sostiene los **5 roles FSMO**.

**WARNING esperado (NO es error):**
```
WARNING: A delegation for this DNS server cannot be created because
the authoritative parent zone cannot be found...
```
→ La zona padre sería `.local`, que **no existe** en ningún DNS. Como es lab aislado, "no action is required". En AD real con subdominios sí se crearía la delegación.

**Verificación post-reinicio:**
```powershell
Get-ADDomain    # DNSRoot: nordwind.local · NetBIOSName: NORDWIND · InfrastructureMaster: DC01.nordwind.local
Get-ADForest    # SchemaMaster: DC01.nordwind.local
Resolve-DnsName -Type SRV _ldap._tcp.dc._msdcs.nordwind.local   # SRV → DC01 = DNS sano
```
> **Prueba de oro:** el SRV `_ldap._tcp` resuelve a DC01 → cualquier máquina que pregunte "¿dónde está el LDAP/KDC?" encuentra al DC. Es el mecanismo que luego exploto con Kerberos. En el examen, `nmap -p 88,389,636,3268` sobre un DC saca justo estos servicios.

#### 3) Estructura de OUs — a MANO (no por script, para entender el DN)
Creada con `New-ADOrganizationalUnit` colgando cada OU de su padre vía `-Path`.
- **Concepto DN (Distinguished Name):** la "ruta LDAP" de un objeto, se lee de derecha a izquierda: `OU=IT,OU=Users,OU=Nordwind,DC=nordwind,DC=local` = IT, dentro de Users, dentro de Nordwind, en el dominio. Esto es lo que va en `ldapsearch -b "..."` al enumerar AD sin Metasploit.
- **OU ≠ Grupo:** OU = contenedor (DÓNDE está el objeto, para organizar / enlazar GPO / delegar). Grupo = membresía (QUÉ puede hacer). Un objeto vive en 1 OU pero está en N grupos.
- `Domain Controllers` aparece en la lista pero es **nativa** (viene de fábrica con el dominio), no la creé yo.
- Verificado: 18 OUs propias + la nativa, árbol correcto 1:1 con el diseño.

#### 4) Usuarios — 1 a mano + bucle (primero entiendo, luego automatizo)
- **1 a mano** (`jan.kowalski`, CEO) con `New-ADUser` para entender los parámetros.
- **9 restantes** con `Import-Csv` + `foreach` desde `C:\LabFiles\employees.csv` (10 empleados del repo).
- **Decisión de lab (desvío consciente del script de Maciej):** él genera passwords **aleatorias** y las vuelca a `lab_passwords.csv` en texto plano. Yo uso **una password de lab conocida** (`Nordwind2026!`) porque en Fase 3 me voy a loguear como estos usuarios para practicar ataques, y necesito saber las credenciales. *(En producción: jamás texto plano ni password compartida.)*
- `-ChangePasswordAtLogon $false` → si fuera `$true` me bloquearía los tests de login/PtH.
- **SamAccountName vs UPN:** `jan.kowalski` (login legacy `NORDWIND\jan.kowalski`, el que enumero con rpcclient/kerbrute/RID) vs `jan.kowalski@nordwind.local` (login moderno, el que usan GetNPUsers/GetUserSPNs).
- Verificado: `Get-ADUser -SearchBase "OU=Users,..." | Measure` → **Count = 10**. ✅

#### 5) Grupos con modelo AGDLP (el concepto estrella de la fase)
**AGDLP** = **A**ccount → **G**lobal → **D**omain **L**ocal → **P**ermission. La regla de Microsoft para organizar permisos en AD:
1. **A** usuario → **G** grupo **Global** por **ROL/departamento** (`G_Sales_Users`) → **DL** anidado en grupo **Domain Local** por **RECURSO** (`DL_FS01_Sales_Modify`) → **P** permiso SOLO en el Domain Local, nunca en el usuario.

**Por qué esta vuelta:** un alta nueva = 1 membresía y hereda todo el acceso de su rol, sin tocar carpetas. Separa "quién es" (rol, Global) de "a qué accede" (recurso, Domain Local).

**Frase de oro (respuesta de entrevista):** *el usuario NO tiene permisos directos — los hereda por grupos anidados. Eso es exactamente lo que BloodHound "desenrolla" para construir rutas a Domain Admin.* Si entiendo cómo se MONTA la cadena, entiendo cómo BloodHound la LEE.

**Qué creé:**
- 7 grupos **Global** (`-GroupScope Global`): `G_<Depto>_Users` por cada departamento.
- 7 grupos **Domain Local** (`-GroupScope DomainLocal`): `DL_FS01_<X>_Modify/Read/FullControl`.
- Anidamiento G_→DL_ con `Add-ADGroupMember` (meto un GRUPO dentro de otro grupo, no usuarios).
- Usuarios → su G_ con un bucle por OU de departamento.
- `-GroupScope` (Global vs DomainLocal) es EL campo que distingue los dos lados de AGDLP.

> ⚠️ Los `DL_FS01_*` apuntan a shares de un `FS01` que aún **no existe** (futuro). Por ahora es la estructura; los permisos reales sobre carpetas se asignan cuando monte FS01.

**Verificación:** `Get-ADPrincipalGroupMembership jan.kowalski` → directo en `Domain Users` + `G_Management_Users` (Global). Su acceso a los DL_ es **indirecto, por anidamiento** = la esencia de AGDLP.

#### 6) SID y RID (regalo de enumeración — material de examen)
Al mirar el grupo vi: `SID: S-1-5-21-1706053521-483693045-3379821969-1113`
- `S-1-5-21-1706053521-483693045-3379821969` = **SID del dominio** (igual para TODOS los objetos de `nordwind.local`).
- `1113` = **RID** (Relative ID), lo único que cambia por objeto. Los míos empiezan en **1000+**.
- **RIDs well-known (fijos):** `500`=Administrator · `512`=Domain Admins · `513`=Domain Users · `502`=krbtgt.
- **Conexión OSCP:** el **RID cycling** (`rpcclient lookupsids` / `lookupsid.py`) coge el SID del dominio y pide RID por RID → saca usuarios **sin credenciales**. Acabo de ver en vivo (`-1113`) la pieza que ese ataque explota.

#### 7) CL01 (cliente) instalado
- VM Win11 **Enterprise eval**, 4GB/2/40GB (disco dinámico), red interna `NordwindLAN`. EFI + TPM 2.0 activados (Win11 no instala sin ellos).
- ISO montada a posteriori (Settings → Storage), como DC01.
- **Trampa cuenta Microsoft:** Win11 pide email/cuenta online. Salida → en OOBE, `Shift+F10` → `start ms-cxh:localonly` (o "Sign-in options → Domain join instead") → crea cuenta **LOCAL** `localadmin` / `Nordwind2026!`. Updates → "later" (red aislada, sin internet).
- **NO** unido al dominio aún (a propósito): solo arranque con admin local. La unión es el siguiente paso.
- Comprobado espacio antes: 121 GB libres → de sobra. (Pendiente opcional: limpiar ~16 GB de Kali duplicado en `~/Downloads`.)

#### 8) Unir CL01 al dominio — la BATALLA (5 tropiezos encadenados) → FASE 1 CERRADA

Secuencia: IP estática `.100` + DNS `→192.168.10.10` → `Add-Computer -OUPath "OU=Workstations,..."` → login de dominio → `klist`. Pero costó, y cada error enseña algo:

| # | Síntoma | Causa real | Fix | Lección |
|---|---|---|---|---|
| 1 | `New-NetIPAddress: Access is denied` | PowerShell sin elevar | Abrir PowerShell **"Run as administrator"** | Config de red = requiere admin |
| 2 | `ping` y `Resolve-DnsName` → timeout, no ve al DC | **CL01 estaba en NAT, no en Internal Network** (`VBoxManage showvminfo` lo confirmó: `nic1="nat"`) | VBox → Network → Internal Network `NordwindLAN` (o `VBoxManage controlvm CL01 nic1 intnet NordwindLAN`) | **NAT aísla de otras VMs; Internal Network las conecta.** Ver [[virtualbox-labs-config]] |
| 3 | No puedo teclear `\` para `NORDWIND\user` | Teclado de la VM en **US**, el mío físico ES | Usar **UPN** `jan.kowalski@nordwind.local` (sin `\`; el `@`=Shift+2 en US) + teclado en pantalla | En login de dominio, UPN evita el `\` |
| 4 | Login falla con credenciales "correctas" | **Desfase horario** CL01↔DC (Kerberos exige ±5 min) | Igualar reloj (`Set-TimeZone "Romance Standard Time"`, `Set-Date`, `w32tm /resync`) | **Kerberos rechaza si los relojes no coinciden.** Error engañoso ("password incorrecta") |
| 5 | Sigue fallando tras igualar hora | La password de `jan.kowalski` **no era** `Nordwind2026!` → se creó **a mano** (Paso A) tecleándola con layout US = salió otra | Reset: `Set-ADAccountPassword -Identity jan.kowalski -Reset` + confirmar con `ValidateCredentials` → `True` | Password tecleada con teclado equivocado = password distinta. Setear por código o verificar |

**Herramienta de diagnóstico de oro** (sirve también en pentesting para validar credenciales encontradas, sin login interactivo):
```powershell
Add-Type -AssemblyName System.DirectoryServices.AccountManagement
$pc = New-Object System.DirectoryServices.AccountManagement.PrincipalContext('Domain','nordwind.local')
$pc.ValidateCredentials('jan.kowalski','Nordwind2026!')   # True / False
```

**El `klist` (el momento):** al loguear como `jan.kowalski` apareció el **TGT** (`Server: krbtgt/NORDWIND.LOCAL`, flags `initial`/`pre_authent`, cifrado **AES-256**, `Kdc Called: DC01`).
- `pre_authent` activo → NO vulnerable a **AS-REP Roasting** (en Fase 2 crearé una cuenta SIN preauth a propósito).
- El TGT = lo que roba **Pass-the-Ticket**; el hash de **krbtgt** = **Golden Ticket**.
- Cuando acceda a un servicio pedirá un **TGS** → en Fase 2, el Kerberoasting hará aparecer aquí un `Server: MSSQLSvc/...` crackeable offline.

Verificado desde DC01: `Get-ADComputer CL01` → existe. **✅ FASE 1 (Construir) CERRADA.**

---

#### ▶ SIGUIENTE AL VOLVER — FASE 2: Sabotear (plantar los agujeros)
Antes de nada: **Snapshot del lab SANO** en VirtualBox (DC01 + CL01) → `lab-sano-antes-de-sabotear` (para poder volver). Ver [[virtualbox-labs-config]] §9.
1. **Kerberoasting:** crear `svc_sql` en `ServiceAccounts` + registrar un SPN (`setspn` / `-ServicePrincipalNames`) → luego `GetUserSPNs.py`.
2. **AS-REP Roasting:** marcar un usuario con "no requiere preauth Kerberos" (`DoesNotRequirePreAuth`) → luego `GetNPUsers.py`.
3. **Ruta BloodHound:** dar a un usuario raso un permiso peligroso (GenericAll/WriteDacl/ForceChangePassword) sobre un grupo o usuario → ruta hacia privilegios.
4. (Pendiente aparte) abrir **ADUC** (GUI) y explorar lo creado — aún solo lo vi por PowerShell.
