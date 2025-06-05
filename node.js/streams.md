```js
const fs = require('fs');

// Crear un Readable Stream para leer el archivo 'archivo.txt' en formato UTF-8
const readableStream = fs.createReadStream('archivo.txt', 'utf-8');

// Evento 'data' se activa cuando hay nuevos datos disponibles para leer
readableStream.on('data', (chunk) => {
    console.log('Chunk recibido:', chunk);
});

// Evento 'end' se activa cuando se completa la lectura del archivo
readableStream.on('end', () => {
    console.log('Lectura del archivo finalizada.');
});

// Evento 'error' se activa si ocurre un error durante la lectura
readableStream.on('error', (err) => {
    console.error('Error en la lectura del archivo:', err);
});


```