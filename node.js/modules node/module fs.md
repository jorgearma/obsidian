**Módulo `fs` en Node.js:** El módulo `fs` (filesystem) es un módulo integrado en Node.js que proporciona una API para interactuar con el sistema de archivos del sistema operativo. Permite a los desarrolladores realizar operaciones como leer y escribir archivos, crear y eliminar directorios,


**`fs.readFile()`**:

- Lee un archivo de manera asíncrona y devuelve su contenido.
- Útil para leer datos de archivos de texto, imágenes u otros tipos de archivos.
- Ejemplo:
```js
const fs = require('fs');
fs.readFile('archivo.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});

```

**`fs.writeFile()`**:

- Escribe datos en un archivo de manera asíncrona. Crea el archivo si no existe.
- Puedes especificar la codificación y manejar errores.
- Ejemplo:
```js
const fs = require('fs');
fs.writeFile('nuevoArchivo.txt', 'Contenido del archivo', 'utf8', (err) => {
  if (err) throw err;
  console.log('Archivo guardado exitosamente.');
});

```


**`fs.readdir()`**:

- Lee el contenido de un directorio de manera asíncrona y devuelve una lista de nombres de archivos y subdirectorios.
- Útil para listar el contenido de una carpeta.
- Ejemplo:

```js 
const fs = require('fs');
fs.readdir('carpeta', (err, files) => {
  if (err) throw err;
  console.log(files);
});

```

**`fs.unlink()`**:

- Elimina un archivo de manera asíncrona.
- Útil para eliminar archivos no deseados.
- Ejemplo:
```js
const fs = require('fs');
fs.unlink('archivoAEliminar.txt', (err) => {
  if (err) throw err;
  console.log('Archivo eliminado exitosamente.');
});

```

**`fs.stat()`**:

- Obtiene información sobre un archivo o directorio, como tamaño, fecha de creación y modificaciones.
- Útil para realizar comprobaciones o informar sobre archivos.
- Ejemplo:
```js
const fs = require('fs');
fs.stat('archivo.txt', (err, stats) => {
  if (err) throw err;
  console.log('Tamaño:', stats.size);
  console.log('Es directorio:', stats.isDirectory());
});

```