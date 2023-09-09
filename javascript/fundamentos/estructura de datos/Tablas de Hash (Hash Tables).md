3. Tablas de Hash (Hash Tables):
    
    - Uso: Las tablas de hash son ideales cuando necesitas realizar búsquedas, inserciones y eliminaciones eficientes basadas en claves.
    - Métodos comunes:
        - `put()`: Asocia una clave con un valor en la tabla de hash.
        - `get()`: Obtiene el valor asociado a una clave.
        - `remove()`: Elimina una clave y su valor asociado de la tabla de hash.
        - `containsKey()`: Verifica si una clave existe en la tabla de hash.
```js
// Crear una tabla de hash y realizar operaciones
let tablaHash = {};

// Agregar elementos a la tabla de hash
tablaHash['clave1'] = 'valor1';
tablaHash['clave2'] = 'valor2';

// Obtener el valor asociado a una clave
console.log(tablaHash['clave1']); // Salida: 'valor1'

// Eliminar un elemento de la tabla de hash
delete tablaHash['clave2'];

// Verificar si una clave existe en la tabla de hash
console.log('clave2' in tablaHash); // Salida: false

// Recorrer las claves y valores en la tabla de hash
for (let clave in tablaHash) {
  console.log(clave, tablaHash[clave]);
}

```