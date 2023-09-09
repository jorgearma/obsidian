El módulo "path" en Node.js ofrece métodos que facilitan la manipulación de rutas, la concatenación de rutas, la normalización de rutas y la obtención de partes específicas de una ruta. Algunos de los métodos más comunes incluyen:

## mas comunes

1. `path.join()`: Combina segmentos de ruta en una sola ruta, teniendo en cuenta las diferencias de separadores de ruta entre sistemas operativos.
    
2. `path.resolve()`: Resuelve una ruta relativa a una ruta absoluta. También se encarga de la normalización de la ruta y resuelve referencias como `.` y `..`.
    
3. `path.basename()`: Obtiene el último segmento de la ruta, que suele ser el nombre del archivo o directorio.
    
4. `path.extname()`: Obtiene la extensión de archivo de una ruta, incluyendo el punto (por ejemplo, ".txt").

**`path.join()`**:


- Combina segmentos de ruta para crear una ruta completa.
- Evita problemas de separadores de ruta según el sistema operativo.
- Ejemplo:

```js
const path = require('path');
const rutaCompleta = path.join(__dirname, 'carpeta', 'archivo.txt');

```

**`path.resolve()`**:

- Crea una ruta absoluta desde segmentos de ruta proporcionados.
- Resuelve rutas relativas a la ruta actual.
- Ejemplo:

```js
const rutaAbsoluta = path.resolve('archivo.txt');

```

**`ath.basename()`**:

- Obtiene el nombre de archivo de una ruta.
- Puede aceptar una segunda argumento para especificar una extensión para eliminar.
- Ejemplo:
```js
const nombreArchivo = path.basename('/ruta/al/archivo.txt');

```

**`path.dirname()`**:

- Obtiene el directorio de una ruta.
- Ejemplo:
```js
const directorio = path.dirname('/ruta/al/archivo.txt');

```

**`path.extname()`**:

- Obtiene la extensión de archivo de una ruta.
- Ejemplo:
```js
const extension = path.extname('/ruta/al/archivo.txt');

```

**`path.parse()`**:

- Descompone una ruta en un objeto con propiedades como `root`, `dir`, `base`, `name` y `ext`.
- Útil para trabajar con diferentes partes de una ruta.
- Ejemplo:
```js
const rutaInfo = path.parse('/ruta/al/archivo.txt');

```

**`path.normalize()`**:

- Normaliza una ruta resolviendo componentes `.` y `..`.
- Ejemplo:
```js
const rutaNormalizada = path.normalize('/ruta/./a/../archivo.txt');

```

**`path.isAbsolute()`**:

- Verifica si una ruta es absoluta.
- Ejemplo:
```js
const esAbsoluta = path.isAbsolute('/ruta/al/archivo.txt');

```