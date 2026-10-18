# VirtualBox — Configuración perfecta de VMs para labs

> **Qué es esto:** chuleta de referencia para montar máquinas virtuales de laboratorio en VirtualBox sin fricción. Todo lo aprendido montando el lab AD [[montar-lab-ad]] (DC01 + CL01). Reutilizable en cualquier lab (AD, HTB local, Kali, etc.).

**Idea madre:** una VM de lab tiene que tener **identidad de red fija y coherente** y estar **aislada** del resto de mi casa. La mayoría de los fallos vienen de (1) red mal puesta y (2) Windows poniendo pegas en la instalación. Esta nota mata ambos.

---

## 0. Requisito del host (Linux) — el módulo `vboxdrv`

VirtualBox necesita compilar su módulo de kernel `vboxdrv`. Si no arranca ninguna VM:

```bash
sudo /sbin/vboxconfig          # recompila los módulos
sudo modprobe vboxdrv          # cárgalo
lsmod | grep vboxdrv           # confirma que está cargado
```

⚠️ **Lección aprendida (oct 2026):** `vboxdrv` **no compilaba en el kernel 7.0.0-38** (símbolos `cr4_*` / `__flush_tlb_all` restringidos al namespace `module:kvm`). En el **kernel 6.17.0-40 sí compila** (esos símbolos están libres). → Si falla, **arrancar con el kernel que funciona** (elegirlo en GRUB) y, a futuro, fijarlo por defecto.

```bash
uname -r                       # ver en qué kernel estoy
```

---

## 1. Modos de red (lo que más importa)

| Modo | Qué hace | Cuándo usarlo |
|---|---|---|
| **Internal Network** | Red privada **solo entre VMs**. Sin salida a internet, sin tocar mi LAN. | ✅ **Labs aislados (AD, ataques).** Mi `NordwindLAN`. |
| **NAT** | La VM sale a internet, pero está sola (no ve a otras VMs). | Bajar actualizaciones/herramientas puntuales. |
| **Bridged** | La VM es una más de mi red de casa (coge IP del router). | Casi nunca en labs ofensivos (expone la VM). |
| **Host-Only** | VMs + host se ven entre sí, sin internet. | Si quiero que Kali (host-only) ataque y a la vez el host administre. |

> **Para un lab de AD → Internal Network.** Todas las VMs del lab en la **misma** red interna con el **mismo nombre** (`NordwindLAN`), si no, no se ven.

### ⚠️ Internal Network NO tiene DHCP
Una red interna **no reparte IPs sola**. Si dejo las VMs en "IP automática" se auto-asignan `169.254.x.x` (APIPA) y **no se ven**. → **IP estática a mano en cada VM** (o montar el rol DHCP en el DC, que es un paso aparte).

---

## 2. Crear la VM (asistente New)

- **Name:** el rol + número → `DC01`, `CL01`, `FS01`.
- **ISO Image:** se puede dejar vacío y montar luego (ver §3).
- ✅ **Marcar "Skip Unattended Installation".** Si no, VirtualBox instala Windows "a su manera" y pierdo el control (cuentas, red, idioma). **Quiero instalar a mano** (entender > automatismo).
- **RAM / CPU / Disco:** ver tabla §6.
- El disco déjalo **dinámico** (VDI): crece según se llena, no reserva todo de golpe.

---

## 3. Montar la ISO después de crear la VM

Normal no ponerla al crear. Con la VM **apagada** → **Settings → Storage**:
1. Clic en el lector óptico que pone `Empty` bajo el controlador (SATA/IDE).
2. Icono del **disco azul** 🔵 → **"Choose a disk file..."** → elegir la ISO.
3. Si no hay lector óptico: clic en el controlador → **"Add optical drive"** (CD con `+`) → luego monta la ISO.

Al arrancar: cuando salga `Press any key to boot from CD...` → **pulsar una tecla** (si no, reinicia y repite).

---

## 4. Settings "perfectos" antes de arrancar

**Settings → System → Motherboard:**
- ✅ **Enable EFI** — *obligatorio para Windows 11* (y recomendable en general).
- ✅ **TPM = 2.0** — *obligatorio para Windows 11*. Sin EFI+TPM2.0 → *"This PC can't run Windows 11"*.

**Settings → System → Processor:**
- 2 vCPU (mínimo cómodo), ✅ Enable PAE/NX.

**Settings → Display:**
- Video Memory 128 MB (resolución más cómoda).

**Settings → Network → Adapter 1:**
- Attached to: **Internal Network** → Name: `NordwindLAN` (el mismo en todas las VMs del lab).

---

## 5. Instalación de Windows — las trampas

| Trampa | Solución |
|---|---|
| **`Ctrl+Alt+Del` no funciona** (lo captura el host Linux) | **Input → Keyboard → Insert Ctrl-Alt-Del**, o Host Key (Ctrl derecho) + `Supr`. Es la *Secure Attention Sequence* de Windows. |
| **Teclado se lía con símbolos** en el setup | Dejar el **teclado en inglés US** durante la instalación. |
| **Edición / clave de producto** | *"I don't have a product key"* (las eval no piden clave). Elegir la edición correcta (Server Std **Desktop Experience** / Win11 **Enterprise**). |
| **Windows 11 obliga a cuenta Microsoft (email)** | En el OOBE, `Shift+F10` → `start ms-cxh:localonly` → crea **cuenta LOCAL**. Alternativas: "Sign-in options → Domain join instead" (Pro/Enterprise), o `OOBE\BYPASSNRO`. |
| **Pide actualizar** | **"Update later"** (red aislada, sin internet; no perder tiempo). |
| **Disco** | Custom install → el disco completo → Next. |

> **Cuenta local de lab recomendada:** usuario `localadmin`, password `Nordwind2026!` (misma del lab, para no memorizar).
> **No unir la máquina al dominio durante la instalación** — eso se hace después, limpio y entendido.

---

## 6. La "config perfecta" por tipo de máquina

| Rol | OS | RAM | vCPU | Disco | EFI/TPM | Red |
|---|---|---|---|---|---|---|
| **DC (Domain Controller)** | Server 2022 Std (Desktop Exp.) | 4 GB | 2 | 60 GB din. | EFI sí | Internal `NordwindLAN`, **IP estática** |
| **Cliente Windows** | Win 11 Enterprise eval | 4 GB | 2 | 40 GB din. | **EFI + TPM 2.0** | Internal `NordwindLAN`, **IP estática** (no hay DHCP) |
| **Servidor miembro** | Server 2022 | 4 GB | 2 | 60 GB din. | EFI sí | Internal, IP estática |
| **Kali (atacante)** | Kali Linux | 4-8 GB | 2-4 | 80 GB din. | EFI sí | Internal (ataca) + opcional NAT (internet) |

> Con **30 GB de RAM** en el host voy sobrado con DC + cliente + Kali encendidos.

---

## 7. Red dentro de la VM (post-instalación)

Como la Internal Network no da DHCP → **IP estática a mano**. En Windows (PowerShell admin):

```powershell
Get-NetAdapter   # ver el nombre de la interfaz (normalmente "Ethernet")

# IP estática + máscara /24 + gateway
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 192.168.10.X -PrefixLength 24 -DefaultGateway 192.168.10.1

# DNS:
#  - En el DC:          apunta a SÍ MISMO (es el DNS del dominio)
#  - En un miembro:     apunta al DC (para resolver el dominio vía SRV)
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 192.168.10.10
```

Verificar siempre con `ipconfig /all` (hostname, IPv4, DNS correctos). **El DNS mal puesto es el fallo nº1** al unir máquinas a un dominio → ver [[montar-lab-ad]].

**Esquema de IPs del lab** (ejemplo Nordwind):
- `.1` gateway · `.10–.19` DCs · `.20–.49` servidores · `.100–.200` clientes.

---

## 8. Guest Additions + portapapeles compartido

Para **copiar en el host y pegar en la VM** (y resolución/ratón cómodos). Hacen falta **las dos cosas**:

1. **Devices → Shared Clipboard → Bidirectional** (y Drag'n'Drop si quiero).
2. **Devices → Insert Guest Additions CD image...** → dentro de Windows, abrir la unidad de CD → ejecutar **`VBoxWindowsAdditions.exe`** → instalar → **reiniciar**.

> Solo con "Bidirectional" **no pega**: el portapapeles lo gestiona el servicio de las Guest Additions. Sin ellas, nada.
>
> ⚠️ **Disciplina:** los comandos del lab se **teclean** (entender > pegar a ciegas). El copy-paste es para rutas largas, DNs y pegar outputs, no muleta.

---

## 9. Snapshots (¡antes de romper nada!)

Antes de la Fase de ataque (o de cualquier cambio arriesgado):
- **Machine → Take Snapshot** → nombre descriptivo (`lab-sano-antes-de-sabotear`).
- Si algo se rompe → **Restore** y vuelvo al estado bueno sin reinstalar.
- Clave para la metodología build→sabotear→atacar: snapshot del lab **sano** antes de plantar agujeros.

---

## 10. Troubleshooting rápido

| Síntoma | Causa probable | Fix |
|---|---|---|
| No arranca NINGUNA VM | `vboxdrv` no cargado/compilado | §0 (ojo al kernel) |
| *"This PC can't run Windows 11"* | Falta EFI o TPM 2.0 | §4 |
| Las VMs no se ven entre sí | Distinta red interna o IP 169.254.x.x | Mismo `NordwindLAN` + IP estática §7 |
| No resuelve el dominio al unir | DNS no apunta al DC | `Set-DnsClientServerAddress ... <IP del DC>` §7 |
| No puedo pegar del host | Faltan Guest Additions | §8 |
| `Ctrl+Alt+Del` no va | Lo captura el host | Input → Insert Ctrl-Alt-Del §5 |

---

**Relacionado:** [[montar-lab-ad]] (lab AD Nordwind) · [[pivoting]] (redes internas) · [[metodologia]]
