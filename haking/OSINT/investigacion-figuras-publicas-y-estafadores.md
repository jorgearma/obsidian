# Investigación OSINT: figuras públicas y estafadores (patrimonial / corporativo)

> Disciplina distinta a la [[OSINT/auditoria-osint-personal|auditoría de huella personal]]. Aquí no busco "qué expone sin querer" un usuario, sino **reconstruir la red de poder, dinero y propiedad** de un objetivo a partir de registros públicos. Es investigación periodística/patrimonial. Núcleo del proyecto de divulgación.

## Cambio de mentalidad

```
Auditoría de huella   → objetivo = persona privada como usuario de internet
                        pregunta = "¿qué filtra sin querer?"

Investigación         → objetivo = figura pública / entidad / estafa
                        pregunta = "¿de dónde sale el dinero y quién controla qué?"
```

La huella digital (usernames, redes, brechas) sigue siendo útil como **capa de entrada**, pero el peso cae en **registros oficiales y análisis de entidades**.

---

## Paso 0 — La pregunta de investigación (hipótesis)

**Por qué:** sin una hipótesis concreta, acumulas datos sin dirección y te ahogas. Toda investigación arranca con una pregunta falsable.

- Malo: "investigar al político X"
- Bueno: "¿el patrimonio declarado de X es coherente con sus ingresos conocidos?"
- Bueno: "¿la empresa Y que ganó este contrato tiene relación con el cargo que lo adjudicó?"
- Bueno (scam): "¿esta web de inversión es la misma red que otras 20 estafas?"

La hipótesis define qué fuentes tocas primero. El resto es seguir el hilo.

---

# BLOQUE A — Investigar figuras públicas (patrimonio y corporativo)

## A1 — Declaraciones de bienes y actividades

**Por qué:** los cargos públicos están obligados por ley a declarar bienes, rentas y actividades. Es tu **línea base**: contra esto contrastas todo lo demás. Si el patrimonio real que encuentras no cuadra con lo declarado, ahí hay historia.

| Fuente (España) | Qué da |
|---|---|
| Congreso de los Diputados — declaraciones de bienes y rentas | Patrimonio e ingresos de cada diputado (público en su web) |
| Senado — igual | Senadores |
| Portal de Transparencia (`transparencia.gob.es`) | Altos cargos, agendas, retribuciones |
| Portales de transparencia autonómicos y municipales | Cargos regionales/locales |

> Verifica siempre la **fecha** de la declaración y busca versiones de años distintos → la evolución del patrimonio es la señal más potente.

## A2 — Empresas y cargos societarios (corporate OSINT)

**Por qué:** el dinero y el poder se mueven a través de sociedades. Saber en qué empresas figura alguien como administrador, socio o apoderado destapa conflictos de interés y flujos de dinero.

| Fuente (España) | Qué da |
|---|---|
| BORME (`boe.es/diario_borme`) | Nombramientos, ceses, constituciones, disoluciones. **Gratis y buscable** |
| Registro Mercantil Central (`registradores.org`) | Datos societarios, cuentas depositadas. De pago |
| Insight/OpenCorporates | Grafo de empresas y personas a nivel internacional |
| Axesor / Infocif / eInforma | Fichas de empresa: socios, administradores, cuentas. Freemium |

Pivote clave: persona → empresas donde figura → otros socios de esas empresas → sus empresas. Es un grafo (ver [[#Link analysis]]).

## A3 — Propiedad inmobiliaria

**Por qué:** los inmuebles son el activo más visible y difícil de ocultar. Contrastar propiedades con lo declarado es un clásico de la investigación patrimonial.

| Fuente (España) | Qué da |
|---|---|
| Catastro (`sedecatastro.gob.es`) | Datos de inmuebles. Sin referencia catastral los datos personales están limitados |
| Registro de la Propiedad (nota simple) | Titularidad, cargas, hipotecas. De pago + requiere interés legítimo |

> El Registro protege datos personales: no puedes hacer búsquedas masivas por nombre. Se trabaja al revés: de la finca al titular.

## A4 — Dinero público (contratos, subvenciones, sanciones)

**Por qué:** aquí se ve la relación entre cargo y beneficio. La adjudicación de contratos y subvenciones es donde aparecen los conflictos de interés.

| Fuente (España) | Qué da |
|---|---|
| Plataforma de Contratación del Sector Público (`contrataciondelestado.es`) | Quién ganó qué contrato, por cuánto, adjudicado por quién |
| BDNS — Base de Datos Nacional de Subvenciones | Subvenciones concedidas y beneficiarios |
| BOE (`boe.es`) | Nombramientos, sanciones, concursos, disposiciones |
| Tribunal de Cuentas | Financiación y contabilidad de partidos políticos |
| InfoElectoral (Min. Interior) | Resultados y financiación de campañas |

> Fuera de España el esquema es idéntico: casi todo país tiene registro mercantil, boletín oficial, portal de transparencia y plataforma de contratación. Cambia el nombre, no el método.

---

# BLOQUE B — Investigar estafadores (scam / fraude)

## B1 — Infraestructura del dominio (la huella técnica de la estafa)

**Por qué:** los estafadores reutilizan infraestructura. Un mismo dueño detrás de 30 webs de estafa deja huellas técnicas comunes. Aquí tu perfil pentester es oro.

| Técnica | Herramienta | Qué revela |
|---|---|---|
| WHOIS histórico | whoxy, securitytrails, domaintools, viewdns.info | Quién registró el dominio antes de anonimizarlo |
| ID de analytics/ads compartido | spyonweb, analyzeid, dnslytics, builtwith | Otras webs con el mismo Google Analytics/AdSense → misma red |
| Certificados SSL | crt.sh | Subdominios y dominios hermanos |
| Historial del sitio | web.archive.org, archive.today | Cómo era la web antes, textos y datos que borraron |
| Reputación | urlscan.io, virustotal, `abuse.ch` | Si ya está reportado como malicioso |

Pivote maestro: **el ID de Google Analytics/AdSense**. Si dos webs comparten el mismo `UA-xxxx`/`pub-xxxx`, casi seguro son del mismo dueño. Así se destapan redes enteras.

## B2 — ¿La empresa/identidad es real?

**Por qué:** casi toda estafa inventa una empresa "regulada" o una identidad de confianza. Verificar contra el registro real la desmonta.

- ¿La empresa existe en el registro mercantil (A2)? ¿La dirección es un coworking o un piso?
- ¿El regulador que dicen tener (CNMV, FCA, etc.) los lista de verdad? Los reguladores publican **listas de chiringuitos financieros / advertencias**.
- **Reverse image** (ver [[OSINT/auditoria-osint-personal]] Área 4) de las fotos de los "fundadores" → suelen ser stock o robadas.
- Textos legales copiados palabra por palabra de otra web → Google entre comillas.

## B3 — Rastro de dinero cripto

**Por qué:** muchas estafas cobran en cripto creyéndolo anónimo. La blockchain es pública: puedes seguir el dinero.

| Herramienta | Qué hace |
|---|---|
| etherscan.io / blockchain.com / blockchair | Explorar transacciones de una wallet |
| breadcrumbs.app / arkham | Grafo visual de flujos entre wallets |
| chainabuse / bitcoinabuse | ¿Esa wallet ya está reportada como estafa? |

---

# TÉCNICAS TRANSVERSALES (críticas para ambos bloques)

## Link analysis

**Por qué:** cuando tienes 40 personas, 30 empresas y 20 dominios, la relación entre ellos ES la historia. Necesitas verlo como grafo, no como lista.

- **Maltego** — el estándar de link analysis OSINT. Nodos (persona, empresa, dominio) y transformaciones automáticas.
- **SpiderFoot** — automatiza recolección sobre un objetivo y la correlaciona.
- Alternativa manual: Obsidian Canvas o un grafo simple. Lo importante es **ver las conexiones**.

## Verificación y cadena de custodia (INNEGOCIABLE en divulgación)

**Por qué:** si vas a publicar, cada afirmación debe ser reproducible por un tercero y sobrevivir a que el objetivo borre la fuente. Sin esto no es divulgación, es difamación.

- **Archiva TODO al momento:** `web.archive.org/save` y `archive.today` → generan una copia con fecha que el objetivo no puede borrar.
- **Captura forense:** Hunchly captura cada página que visitas con hash y timestamp automáticos.
- Guarda: URL exacta · fecha de captura · captura de pantalla · copia archivada.
- Regla de las **dos fuentes independientes** antes de afirmar algo.
- Distingue siempre **dato verificado** de **inferencia**. Nunca los mezcles en la publicación.

## OPSEC del investigador (protégete tú)

**Por qué:** investigar políticos con poder y estafadores organizados tiene riesgo real de represalia. No te quemes.

- **Sock puppet:** cuenta/identidad separada para investigar, nunca tu perfil real.
- Navegador dedicado + VPN cuando toques la infra del objetivo (visitar la web scam puede alertarles con tu IP).
- No interactúes (no comentes, no des like, no contactes) → eso te delata y contamina la investigación.
- Compartimenta: la identidad investigadora no toca jamás tus selectores reales (los de la auditoría personal).

---

## Líneas rojas (legal y ético)

```
SÍ  → registros públicos, fuentes abiertas, análisis de datos ya publicados
SÍ  → figuras públicas en lo relativo a su función y patrimonio de origen público
NO  → acceso no autorizado a sistemas (eso ya es delito, no OSINT)
NO  → ingeniería social / pretexting para sacar datos privados
NO  → datos de familiares/privados sin interés público real
NO  → publicar sin verificar (difamación) o mezclar dato con especulación
```

> Marco mental: **interés público + fuente pública + verificación + no acceso ilícito**. Si falta una pata, no se publica.

---

## Relación con las otras notas

- Entrada de identidad y huella → [[OSINT/auditoria-osint-personal]]
- Infra técnica de dominios → [[web enumeracion/DNS/reconocimiento-dns-pentesting]] y [[1. nmap]]
- Metadatos de documentos filtrados → [[tools/exiftool]]
