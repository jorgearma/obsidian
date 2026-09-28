# Xbox 360 — Liberación por software (BadUpdate / ABadAvatar)

**Fecha:** 2026-09-25
**Consola:** Xbox 360 S — placa **Corona**, NAND 16 MB, **con disco duro interno**
**Dashboard:** 2.0.17559.0
**Pack usado:** BadRepack 20250915 (MobCat) → exploit ABadAvatar + XeUnshackle + Aurora 0.7b.2
**Backup:** `~/xbox360-backup/2026-09-25/` (NAND + CPU key)

Tags: #hardware #xbox360 #exploit #homebrew

---

## Cómo funciona (el porqué)

- **BadUpdate** (Grimdoomer, 2024-25): exploit del **hypervisor** de la 360 por software → permite ejecutar código sin firmar en el dashboard 17559.
- **ABadAvatar** (shutterbug2000): punto de entrada nuevo → se lanza solo en la **pantalla de selección de perfil** (renderizado de avatar). Ya no hace falta Rock Band Blitz ni ningún juego.
- Es una **race condition** → no siempre gana a la primera. Reintentar es normal.
- **No es permanente:** vive en RAM. Al apagar se pierde → en cada arranque se relanza (automático si el USB está puesto).
- Permanente de verdad = **RGH3** (fault injection por hardware, 1-2 cables soldados). Corona es compatible.

---

## ABadAvatar (lo que tengo) vs RGH3 (soldar)

### La diferencia de fondo: en qué punto del arranque entras

```
Encender → Bootloaders → Kernel → Hypervisor → Dashboard → Pantalla de perfiles
            ▲                                                    ▲
         RGH3 entra AQUÍ                               ABadAvatar entra AQUÍ
      (antes de que arranque nada)                 (con el sistema ya arrancado)
```

- **ABadAvatar:** arranca el sistema **original** de Microsoft → el exploit se cuela después aprovechando un fallo → vive en **RAM** → al apagar, desaparece.
- **RGH3:** un pulso eléctrico en el reset del CPU engaña la **comprobación de firma del bootloader** en el primer instante → arranca un sistema **modificado guardado en la NAND** → permanente porque lo modificado está en la NAND, no en RAM. (= **fault injection / glitch attack** por hardware)

### Día a día

| | ABadAvatar (USB) | RGH3 (soldado) |
|---|---|---|
| Arranque | Esperar en perfiles, a veces minutos | Directo a Aurora en segundos |
| Fiabilidad | Race condition → a veces falla y hay que reiniciar | Arranca siempre (si la soldadura está bien) |
| USB | Siempre metido | No hace falta |
| Control | Parcial: parchea un sistema ya arrancado | Total desde el boot (dash modificado, plugins, parches kernel, Linux) |
| Depende de | Dashboard 17559 | Nada — la NAND es mía |
| Riesgo al hacerlo | Casi nulo | Medio (soldar mal puede dañar la placa) |
| Reversible | Total (quitas el USB = Xbox normal) | Sí, con el backup de la NAND |
| Para revender | Poco atractivo | ✅ Es el producto que la gente compra |

### Mi situación para un RGH3
1. Placa **Corona, NAND 16 MB** → compatible con RGH3 ✅
2. **Backup de NAND + CPU key ya hechos** = la mitad del trabajo ✅ (con BadUpdate se puede incluso flashear la imagen RGH3 por software, sin lector de NAND — confirmar en ConsoleMods antes)
3. Falta solo: **soldar 1-2 cables** en puntos concretos de la placa

### Decisión / recomendación
- **Para jugar yo:** lo que tengo ya sirve. RGH3 = comodidad, no necesidad.
- **Para aprender / revender / CV** ("fault injection por hardware"): RGH3 merece la pena.
- **Si nunca he soldado → NO empezar con esta consola.** Practicar antes en una placa rota (consolas rotas en DBA/Wallapop por 8-25 €).

---

## Parte 1 — Setup inicial (una sola vez) ✅ hecho

### 1. USB
- **FAT32** + tabla de particiones **MBR**
- Contenido del pack **en la RAÍZ** del USB (no en subcarpeta):
  ```
  USB/
  ├── Apps/  BadUpdatePayload/  Content/  Dash/
  ├── launch.ini  name.txt  ...
  ```
- ⚠️ Error que tuve: todo dentro de `BadRepack-20250915/` → la Xbox no veía nada.

### 2. Consola
- Dashboard **17559** → *Configuración → Sistema → Información de la consola*
- **Desactivar auto sign-in** del perfil
- **Cable de red desconectado**

### 3. Backup (seguro de vida)
- En XeUnshackle → **X** → guarda CPU key / info consola
- Aurora → `Usb0:\Apps\Simple 360 NAND Flasher\Default.xex` → **X** → `flashdmp.bin`
- Verificación en PC:
  - tamaño = `17301504` bytes = `0x1080000` (16 MB + ECC)
  - cabecera empieza por `FF4F` + `© 2004-2011 Microsoft Corporation`
  ```bash
  xxd -l 64 flashdmp.bin
  ```
- ⚠️ La **CPU key es única y privada** → no compartirla nunca.

---

## Parte 2 — Rutina para jugar

1. USB metido, sin red
2. Encender → **no tocar el mando** en pantalla de perfiles
3. Notificación **ABadAvatar** → el **anillo de luces se va llenando** (= barra de progreso)
4. Sale **XeUnshackle** → **Back**
5. Entrar con **mi perfil** (siempre el mismo → las partidas van ligadas al perfil)
6. **Guía** → mantener **A** en *Xbox Home* → **Aurora**
7. Elegir juego → **A**

**Si falla:** luces fijas sin avanzar ~5 min → apagar manteniendo power → esperar 10 s → reintentar (a veces 2-3 veces).

---

## Parte 3 — Añadir un juego de 360 (desde PC)

1. Extraer:
   ```bash
   7z x juego.rar        # o: unrar x juego.rar
   ```
2. Comprobar formato **GOD**: carpeta `TITLEID/00007000/<hash>` + `<hash>.data/Data0000...`
   - Si es `.iso` → convertir a GOD antes (iso2god)
   - GOD va troceado en partes de ~170 MB → evita el límite de **4 GB de FAT32**
3. (Opcional) Verificar que está completo leyendo la cabecera GOD:
   ```bash
   python3 - "ruta/al/archivo_cabecera" <<'EOF'
   import struct,sys
   d=open(sys.argv[1],'rb').read()
   print('magic', d[:4])                                   # LIVE
   print('title id', d[0x360:0x364].hex().upper())
   print('trozos esperados', struct.unpack('>I', d[0x39D:0x3A1])[0])
   print('tamaño esperado', struct.unpack('>Q', d[0x3A1:0x3A9])[0])
   EOF
   ls ruta/<hash>.data | wc -l    # tiene que coincidir
   ```
4. Copiar a la ruta estándar:
   ```bash
   rsync -rt --info=progress2 ~/Downloads/JUEGO-GOD/TITLEID "/media/siemprearmando/UBUNTU 22_0/Content/0000000000000000/" && sync
   ```
   - Sin `/` al final de `TITLEID` → copia la carpeta entera
   - `sync` → fuerza a escribir la caché de RAM al USB (si no, la copia puede quedar a medias al sacarlo)
5. Verificar copia por checksum (si no sale nada = idéntica):
   ```bash
   rsync -rcn --out-format='DIFF %n' ~/Downloads/JUEGO-GOD/TITLEID/ "/media/siemprearmando/UBUNTU 22_0/Content/0000000000000000/TITLEID/"
   ```
6. Expulsar bien:
   ```bash
   udisksctl unmount -b /dev/sdb1
   ```
   - `target is busy` → algo tiene el USB abierto:
     ```bash
     lsof +f -- "/media/siemprearmando/UBUNTU 22_0"
     ```
     (en mi caso, Nautilus → cerrar la ventana)

### En Aurora
- **Back → Settings → Content → Scan Locations**
  - Path: `Usb0:\Content\0000000000000000` (16 ceros)
  - Depth: **3**
  - Script Data: **None**
  - Tipo: juegos (**no** `Applications`)
- **Rescan** → esperar (el primer escaneo tarda; también encuentra lo que había en `Hdd1`)
- "No Title Found" en la pantalla principal → filtro/categoría vacía → cambiar categoría
- Guardar partidas → **Disco duro** (no en "ABadAvatar" = el USB)

### Mover un juego del USB al disco duro (desde Aurora, sin apps extra)
1. Aurora → **Back → File Manager**
2. Ir a `Usb0:\Content\0000000000000000\` → ponerse encima de la carpeta del juego (ej. `454107D9`) → **Copy**
3. Ir a `Hdd1:\Content\0000000000000000\` (**entrar dentro** de la de 16 ceros) → **Paste**
4. Esperar (7 GB ≈ 10-15 min), no apagar ni sacar el USB
5. **Rescan** → si sale duplicado es normal → probar que arranca desde el HDD → luego borrar la copia del USB

### Tipos de contenido en `Hdd1:\Content\0000000000000000\<TitleID>\`

| Subcarpeta | Tipo | ¿Va sin disco? |
|---|---|---|
| `000D0000` | Arcade (XBLA) | ✅ |
| `00007000` | Games on Demand (como NFS) | ✅ |
| `00080000` | Demo | ✅ |
| `00004000` | Juego **instalado** desde disco | ❌ necesita el disco (la instalación solo acelera la carga) |

- Juegos de disco → hacer backup completo de **mi disco original** a GOD/extraído en el HDD → ya van sin disco.
- Apps (Netflix, YouTube…) salen en la lista porque viven en la **misma carpeta** que los juegos → Aurora lista todo lo ejecutable. Mejor **ocultarlas** que borrarlas. Muchas ya no funcionan (servicios retirados).
- Tras el primer escaneo, Aurora procesa todo (en mi caso 88 items) y **extrae los iconos internos** de cada título → funciona sin internet (iconos pequeños, no carátulas grandes).

### Carátulas
- Se descargan de internet → lanzar el exploit **sin red** y **conectar el cable después** (el pack bloquea Xbox Live pero deja descargar artwork)
- ❌ Nunca reactivar Xbox Live → ban

---

## Emuladores

- **PS1 → PCSXR-360** — https://github.com/Wolf3s/pcsxr-360/releases
  - Carpeta: `USB/Apps/PCSXR360/default.xex`
  - Juegos (bin+cue juntos): `USB/PSX/`
  - Menú en juego: LB + RB + ABXY
- Juegos de 360 **no necesitan emulador**.
- Imagen de un disco propio de PS1 (necesita lector CD):
  ```bash
  cdrdao read-cd --read-raw --datafile juego.bin --device /dev/sr0 --driver generic-mmc-raw juego.toc
  toc2cue juego.toc juego.cue
  ```

---

## Lecciones aprendidas

| Problema | Causa | Lección |
|---|---|---|
| Xbox no veía el USB | Archivos en subcarpeta | Estructura de carpetas: raíz = raíz |
| Exploit se atascaba | Race condition | Reintentar es parte del proceso |
| Juego no funcionaba | Copia cortada (13/42 trozos) | **Verificar siempre**: leer cabecera binaria + checksum |
| `target is busy` | Nautilus con el USB abierto | `lsof` para ver qué proceso tiene archivos abiertos |
| Resultado absurdo al parsear | Offset equivocado (0x3A0 vs 0x39D) | Si el dato es absurdo, el error suele estar en tu lectura |

**Conexión con pentesting:** parsear formatos binarios por offsets, verificar integridad, `lsof`, race conditions, fault injection (RGH) → mismo músculo.

---

## Pendiente

- [ ] Subir `~/xbox360-backup/` a la nube
- [ ] Segundo dump de NAND y comparar hash (opcional)
- [ ] Mover juegos del USB al disco duro (`Hdd1:\Content\0000000000000000\`) — en curso con NFS (ver sección abajo)
- [x] ~~Probar ABadAvatarHDD~~ → **Decisión (25 sep): me quedo con el USB.** Mismo exploit, pero fork de terceros menos conocido, trae menos apps y un plugin (Proto) sin revisar. El USB funciona y es el paquete conocido. Ref por si cambio de idea: https://github.com/Flo562/badavatarHDD (usar ≥ v1.01)
- [ ] Borrar carpeta duplicada `BadRepack-20250915/` del USB
- [ ] (Futuro) RGH3 si quiero algo permanente / revender

## Fuentes

- BadUpdate — https://github.com/grimdoomer/Xbox360BadUpdate
- ConsoleMods Wiki — https://consolemods.org/wiki/Xbox_360:RGH
- README del pack BadRepack (en el propio USB)
