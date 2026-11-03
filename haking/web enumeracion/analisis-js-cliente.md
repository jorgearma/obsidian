# Análisis del lado cliente: JS, localStorage y controles del cliente

Relacionadas: [[enumeracion web]] · [[foothold-reconocimiento]] · [[enumer]] · [[curl]] · [[feroxbuster]]

> Aprendido el 2026-11-02/03 copiando en local el fan game *Poké Arena 2D* (Phaser + módulos ES) y leyendo su código. Mismo proceso que en una web objetivo.

---

## El porqué (la idea que lo sostiene todo)

**Todo lo que ejecuta el navegador, el navegador lo tiene que descargar.** Así que el código del cliente (HTML, JS, JSON, imágenes) es **siempre legible**: como mucho está minificado u ofuscado, pero nunca escondido.

```
Cliente (lo que baja el navegador) → copiable / legible ✅
Servidor (lo que corre en su máquina) → invisible ❌
```

- **Cliente** = quien PIDE (navegador, curl, mis scripts).
- **Servidor** = quien ENTREGA los archivos.
- **Código del cliente** = el JS que el servidor entrega y luego se ejecuta en el navegador.

Analogía: el JS del cliente es el **plano de la casa que te dan en la puerta**. No ves lo que hay en la caja fuerte (servidor), pero sí todas las puertas, pasillos y dónde están las cerraduras.

---

## Proceso (lo que hice, paso a paso)

### 1. Reconocimiento del HTML y cabeceras
```bash
curl -sSL -D headers.txt https://objetivo/ -o index.html
grep -oE '(src|href)="[^"]+"' index.html | sort -u
```
- Los `src=` dicen el **framework** (`lib/phaser.min.js`) y el **punto de entrada** (`main.js`).
- La cabecera **CSP** filtra dominios internos/APIs: `connect-src ... wss://red.objetivo.com` → descubrí el servidor de juego/API **sin escanear nada**.

### 2. `wget --mirror` se queda corto
Bajó solo ~10 archivos. **wget sigue enlaces del HTML pero NO ejecuta JS** → en apps modernas (React, Vue, Phaser) casi todo se carga desde JS. Igual que gobuster: solo encuentra lo que adivina.

### 3. Seguir el grafo de `import`
Los módulos ES se encadenan: `import {X} from "./escenas/carga.js"`. Script recursivo: baja un `.js` → busca sus `import ... from "..."` → baja esos → repite. Resultado: **83 módulos = todo el código del cliente**.

### 4. Rutas dinámicas (plantillas)
Las rutas NO estaban escritas enteras:
```js
`assets/pmd/${dex}/portrait.png`
```
→ hay que **leer el código** para saber de dónde sale `${dex}` (aquí: claves de `manifest.json`). En una app real esto es:
```js
`/api/v2/users/${id}/invoices`   ← endpoint que gobuster nunca adivinaría
```

### 5. Validar errores, no ignorarlos
73 rutas dieron 404 → las **agrupé por carpeta** → todas en `assets/vfx/` → falso positivo de mi regex. Agrupar = ver el patrón.

### 6. Probar de verdad
Servidor local + Chrome headless + captura → 0 errores 404. No fiarse de "debería funcionar".

---

## Leer JS minificado

Minificado = todo en una línea (sin espacios, para cargar rápido). Se des-minifica:

| Dónde | Cómo |
|---|---|
| Chrome DevTools | Sources → archivo → botón **`{}`** (pretty print) |
| VS Code (Linux) | `Ctrl+Shift+P` → **Format Document** (lenguaje en `JavaScript`, abajo a la derecha) |
| Terminal | `npx prettier --write "carpeta/**/*.js"` |

Moverse por código ajeno en VS Code: `Ctrl+P` abrir archivo · `Ctrl+Shift+F` buscar en todo · `F12` ir a la definición · `Shift+F12` ver dónde se usa.

**Qué buscar** (`Ctrl+Shift+F`): `fetch(`, `/api/`, `token`, `apikey`, `secret`, `admin`, `debug`, `localStorage`, `http`, dominios, `role`, `isAdmin`, `unlock`/`desbloque`...

> Hallazgo real: en `config.js` estaba el **Discord** del proyecto; en `config.js` también un **modo DEBUG** que se activa si `location.hostname` es `localhost`. En una app real → funciones de desarrollo activables con un parámetro/cabecera.

---

## Almacenamiento del navegador

`localStorage` = **base de datos clave → valor que solo guarda TEXTO**, separada por **origen** (protocolo + dominio + puerto).

| Almacén | Qué es | Dura | ¿Lo ve el servidor? |
|---|---|---|---|
| **Cookies** | textos pequeños | hasta caducar | **Sí** (van en cada petición) |
| **localStorage** | clave→texto, ~5 MB | para siempre | No, solo el JS |
| **sessionStorage** | igual | hasta cerrar pestaña | No |
| **IndexedDB** | BD con objetos | para siempre | No |

- `http://localhost:8765` y `https://objetivo.com` son **almacenes distintos** (Same-Origin Policy).
- Físicamente: Chrome → `~/.config/google-chrome/Default/Local Storage/leveldb/` (LevelDB) · Firefox → `.../storage/default/<origen>/ls/data.sqlite`.
- Verlo: F12 → **Application → Local Storage**.

### Leer y modificar (el ciclo)
```
TEXTO ──JSON.parse──► OBJETO (lo cambias) ──JSON.stringify──► TEXTO
```
```js
location.origin                                   // ¿estoy donde creo?
const p = JSON.parse(localStorage.getItem("clave") || "{}");
localStorage.setItem("clave.backup", JSON.stringify(p));   // backup siempre
p.campo = true;
localStorage.setItem("clave", JSON.stringify(p));
// recargar la página: el código ya leyó el valor al arrancar
```
Copia de seguridad rápida: `copy(localStorage.getItem("clave"))` en la consola.

---

## Controles del lado cliente (la vulnerabilidad)

**Regla de oro: un control que solo existe en el cliente NO es un control de seguridad.** La pregunta siempre es: **¿el servidor lo vuelve a comprobar?**

### Ejemplo real (Poké Arena 2D, `liga.js`)
```js
const desbloqueado = (id) => {
  const p = progreso();                 // lee localStorage "pa-liga"
  return p.legado || LIGA.iniciales.includes(id) || !!p.vencidos[id] ...
};
```
- Offline: poner `legado: true` en `localStorage` → **todo desbloqueado** (comprobado en mi copia local).
- Online (ranked) hay **segunda comprobación**:
```js
const desbloqueadoRanked = (id) => desbloqueado(id) && (... validado.vencidos[id]);
// validado = progreso guardado EN EL SERVIDOR (tickets $liga_empieza / $liga_gana)
```
→ El autor hizo bien: lo que afecta a otros lo **re-valida el servidor**.

### Cómo aparece en un pentest
- Botón/panel "Admin" oculto por CSS pero el endpoint responde a cualquiera.
- Precio/rol en campo oculto o en `localStorage` (`"rol":"user"` → `"admin"`) que el servidor no verifica.
- Funciones "premium" bloqueadas solo en el frontend.
- **Token de sesión (JWT) en localStorage** → si hay **XSS**, `localStorage.getItem(...)` lo roba. (Cookies con `HttpOnly` NO son legibles por JS.)

**Patrón de 3 pasos:**
1. Encuentra la comprobación en el JS.
2. Mira de dónde salen sus datos (localStorage, cookie, parámetro, respuesta de API).
3. ¿El servidor lo re-comprueba? Si no → **lógica de negocio rota**.

---

## Bonus: códigos HTTP vistos

| Código | Significado | En pentesting |
|---|---|---|
| 200 | OK | existe y tienes acceso |
| 301/302 | redirección | ¿a dónde? (¿login?) |
| **304** | Not Modified: usa tu caché (respuesta a `If-Modified-Since`) | en Burp Repeater: **borra `If-Modified-Since` / `If-None-Match`** para ver el 200 completo |
| 401/403 | sin auth / prohibido | **existe** pero protegido → interesante |
| 404 | no existe | ruido |
| 500 | error del servidor | ¿qué input lo provocó? |

`Cache-Control: no-cache` ≠ "no guardes" → significa "guarda, pero **pregúntame** antes de usarlo".

---

## Lo que DEBO recordar

- El JS del cliente es un **mapa gratis** de la app: endpoints, dominios, parámetros, funciones ocultas.
- `wget`/gobuster no ven lo que se carga desde JS → **leer el código** da rutas reales (2282/2355 existían) frente al fuzzing a ciegas.
- La **CSP** también es fuente de recon.
- `localStorage` = clave→texto, por origen; se edita con `JSON.parse`/`stringify`.
- **Control solo en cliente = no es control.** Busca siempre la re-validación del servidor.
- Herramientas que automatizan parte: **LinkFinder**, **JSluice**, Burp (lista de JS). Primero a mano para entender qué buscan.

## Dónde encaja en el examen

- **Fase 2 — Web (80/443):** tras gobuster/ferox, abrir el JS de la app (DevTools `{}` o `curl` + prettier) y buscar `/api/`, `fetch(`, `admin`, credenciales hardcodeadas. Endpoints de API ocultos = vector típico de foothold.
- Apps con login: mirar qué guarda en `localStorage`/cookies tras autenticar (tokens, roles) y si el servidor confía en ello.
- OSCP-friendly: **100% manual**, sin Metasploit — DevTools, curl, grep y leer.

⚠️ **Límite ético:** descargar lo público para uso personal = lo mismo que hace el navegador. Manipular/atacar el servidor de un tercero NO. En pentest real: solo dentro del alcance autorizado.
