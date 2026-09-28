# Auditoría OSINT personal (auto-auditoría)

> Metodología para auditar la huella digital de un objetivo. Aplicada a mí mismo como ejercicio de calibración (tengo la verdad de base → mido la fiabilidad de cada fuente). Reutilizable para el proyecto de divulgación.

## Concepto clave — Pasivo vs Activo

```
Pasivo   → consultas fuentes de terceros, NO tocas al objetivo. Cero rastro.
Activo   → interactúas con la infra del objetivo (DNS, puertos, web). Dejas logs.
```

Siempre pasivo primero, activo después. En una investigación real, lo pasivo lo hace todo antes de arriesgar exposición.

---

## Paso 0 — Scoping e inventario de selectores (LO PRIMERO)

**Por qué:** un "selector" es cualquier dato que sirve de pivote para encontrar más datos. Si empiezas a buscar sin inventario, no sabes qué has cubierto ni por dónde vas. Primero defines la superficie, luego la atacas de forma sistemática.

**Regla de oro:** cada dato encontrado es un selector nuevo. El OSINT es un grafo que se expande (username viejo → otras plataformas → email antiguo → brechas → teléfono → ...).

### Hoja de recolección (rellenar con lo que YA sé — ground truth)

| Categoría                          | Valores conocidos |
| ---------------------------------- | ----------------- |
| Nombres / alias reales             |                   |
| Usernames                          |                   |
| Emails (actuales e históricos)     |                   |
| Teléfonos                          |                   |
| Dominios / IPs / VPS               |                   |
| Avatares / fotos reutilizadas      |                   |
| Físico (ciudad, trabajo, estudios) |                   |

> Mantener un `hallazgos.md` aparte donde se vuelca TODO lo encontrado con: dato · fuente · fecha · confianza (alta/media/baja). Sin esto no es auditoría, es cotilleo.

---

## Las 5 áreas de una auditoría completa

```
1. Identidad      → nombres y usernames cruzados entre plataformas
2. Credenciales   → emails/passwords en brechas de datos (data breaches)
3. Técnica        → dominios, DNS, subdominios, puertos, certificados
4. Social         → redes, geolocalización de posts, relaciones
5. Documental     → PDFs, metadatos EXIF, registros públicos
```

---

## Área 1 — Identidad (username cruzado)

**Por qué:** la gente reutiliza el mismo alias en decenas de plataformas. Un solo username puede destapar cuentas olvidadas de hace años.

| Herramienta | Qué hace | Nota |
|---|---|---|
| `sherlock <user>` | Busca un username en 300+ webs | El estándar. Falsos positivos → verificar a mano |
| `maigret <user>` | Como sherlock pero más fuentes + reporte | Más completo, más lento |
| whatsmyname.app | Versión web, sin instalar nada | Pasivo puro |
| Google dorking | `"username"` entre comillas, `site:` | Manual pero preciso |

```bash
sherlock jorgearma siemprearmando
maigret siemprearmando --html
```

Cada cuenta encontrada → mirar bio, fotos, seguidores, fechas → nuevos selectores.

---

## Área 2 — Credenciales (brechas de datos)

**Por qué:** es lo más revelador. Si un email tuyo salió en una brecha, un atacante puede tener tu contraseña real o el patrón que usas. Aquí se ve el riesgo de verdad.

| Fuente | Qué da | Coste |
|---|---|---|
| haveibeenpwned.com | En qué brechas apareció el email/teléfono | Gratis (email propio se verifica) |
| dehashed.com | Emails, passwords, hashes, direcciones | De pago (potente) |
| intelx.io | Brechas, pastes, documentos filtrados | Freemium |
| Google: `"email" password` | Pastes indexados en claro | Gratis |

**Acción tras hallazgo:** si un password real aparece → cambiarlo en todo sitio donde lo reuses + activar 2FA. Ese es el entregable de esta área.

---

## Área 3 — Técnica (tu propia infra: VPS, dominios)

**Por qué:** aquí es donde tu perfil pentester te da ventaja. Auditas lo que expones a internet sin querer. Enlaza con [[web enumeracion/DNS/reconocimiento-dns-pentesting]].

### Pasivo
| Fuente | Qué encuentras |
|---|---|
| crt.sh/?q=%.midominio.com | Subdominios vía certificados SSL |
| shodan.io/host/MI_IP | Puertos, servicios, banners de mis VPS |
| virustotal.com/gui/ip-address/MI_IP | Historial DNS, dominios en esa IP |
| dnsdumpster.com | Mapa DNS del dominio |

### Activo (sobre MI infra, autorizado)
```bash
# DNS
dig midominio.com ANY
subfinder -d midominio.com
amass enum -passive -d midominio.com

# Puertos (mis VPS)
nmap -p- --min-rate 5000 MI_IP
nmap -sV -sC -p<puertos> MI_IP
```

> Enlaza con [[1. nmap]]. Pregunta clave: ¿qué tengo abierto que NO debería? (paneles admin, SSH con password, servicios viejos).

---

## Área 4 — Social

**Por qué:** las redes filtran ubicación, rutina, relaciones y cara. La geolocalización de fotos/posts es el vector clásico de doxing.

- Buscar el username (Área 1) en cada red → revisar publicaciones públicas
- Fotos: ¿fondos reconocibles, matrículas, carteles de calle, reflejos?
- **Reverse image search** del avatar: images.google.com, yandex.com/images (Yandex es el mejor para caras), tineye.com
- Metadatos de geolocalización en posts (algunas plataformas los conservan)

---

## Área 5 — Documental (metadatos)

**Por qué:** un PDF o una foto que subiste hace años puede llevar tu nombre real, software usado, coordenadas GPS o rutas internas de tu equipo.

```bash
exiftool archivo.pdf        # autor, software, fechas
exiftool foto.jpg           # GPS, cámara, fecha
```

- Google dork: `site:midominio.com filetype:pdf`
- Buscar documentos con mi nombre: `"Jorge Escobar" filetype:pdf`

Enlaza con [[tools/exiftool]].

---

## Flujo resumido (el pivote continuo)

```
Paso 0: inventario de selectores conocidos
   ↓
Área 1: usernames → cuentas nuevas → + selectores
   ↓
Área 2: emails → brechas → passwords/teléfonos → + selectores
   ↓
Área 3: dominios/IPs → subdominios/puertos → superficie técnica
   ↓
Área 4 y 5: fotos y documentos → ubicación, identidad real
   ↓
Volcar TODO en hallazgos.md (dato · fuente · fecha · confianza)
```

---

## Entregable final de la auditoría

1. **Mapa de exposición:** qué se puede encontrar de mí y desde qué fuente
2. **Riesgos priorizados:** credenciales filtradas > infra expuesta > geoloc > resto
3. **Plan de remediación:** cambiar passwords, cerrar puertos, borrar/privatizar cuentas viejas, limpiar metadatos

---

## Notas OSCP / legal

- OSINT es **pasivo por definición** en su mayoría → ideal para la fase de recon sin tocar el objetivo.
- Auto-auditoría = 100% autorizado. Sobre terceros: solo fuentes públicas y sin acceso no autorizado.
- Herramientas a instalar: `sherlock`, `maigret`, `subfinder`, `amass`, `theHarvester`, `exiftool` (ya lo tengo).
