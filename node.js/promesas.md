```js
// Importamos el módulo `readFile` de la biblioteca 'fs' para leer archivos.
const { readFile } = require('fs');

// Definimos una función llamada `gettext` que acepta una ruta de archivo como argumento.
const gettext = (pathfile) => {
    // Creamos y devolvemos una nueva promesa.
    return new Promise((resolve, reject) => {
        // Usamos la función `readFile` para leer el archivo en la ruta proporcionada.
        // Pasamos 'utf-8' como codificación para que los datos se interpreten como texto.
        readFile(pathfile, 'utf-8', (err, data) => {
            // Si ocurre un error al leer el archivo, rechazamos la promesa con el error.
            if (err) {
                reject(err);
            } else {
                // Si la lectura es exitosa, resolvemos la promesa con los datos del archivo.
                resolve(data);
            }
        });
    });
};

// Llamamos a la función `gettext` con la ruta del archivo y encadenamos el manejo de promesas.
gettext('../data/texto.txt')
    .then((result) => {
        // Si la promesa se resuelve correctamente, imprimimos los datos del archivo.
        console.log(result);
    })
    .catch((err) => {
        // Si la promesa se rechaza (error), imprimimos el mensaje de error.
        console.log(err);
    });

```