```js
const { readFile } = require('fs');

// Definición de una función promisificada para leer un archivo
const gettext = (pathfile) => {
    return new Promise((resolve, reject) => {
        // Usar la función 'readFile' del módulo 'fs' 
        readFile(pathfile, 'utf-8', (err, data) => {
            if (err) {
                reject(err); // Rechazar  si hay un error
                return; // Asegurarse de salir 
            }
            resolve(data); 
        });
    });
};

// Función principal asincrónica para leer y mostrar el contenido del archivo
async function read() {
    try {
        // Usar 'await' para esperar a que se resuelva
        const result = await gettext("../data/adios.txt");
        console.log(result); // Mostrar el contenido 
    } catch (err) {
        console.log("Error:", err); // Manejar el error 
    }
}

// Llamar a la función '
read();

```


# `promisify` del módulo `util`

```js
const { promisify } = require('util');
const readwintpromise = promisify(readFile);

```

Luego, puedes usar `readwintpromise` de manera similar a como lo harías con `readFile`:

```js
async function read() {
    try {
        const result = await    readwintpromise("../data/adios.txt");
        console.log(result);
    } catch (err) {
        console.log("Error:", err);
    }
}

read();

```


-------------------------------------------------------

```js
const { readFile } = require('fs/promises');

```

ermite que `readFile` sea una función promisificada y puedas usarla directamente en un estilo de programación asíncrona utilizando `async/await`. Tu función `read` también funcionará sin necesidad de crear una función `promisify` o definir manualmente `gettext`