2. **Configuración de la Conexión con Promesas:**

En tu archivo principal (por ejemplo, `app.js`), importa el paquete `mysql2/promise` y configura la conexión a tu base de datos MySQL:

```js
const mysql = require('mysql2/promise');

const connection = await mysql.createConnection({
  host: 'nombre_del_host',
  user: 'nombre_de_usuario',
  password: 'contraseña',
  database: 'nombre_de_la_base_de_datos'
});

console.log('Conexión exitosa a la base de datos');

```

3. **Ejecución de Consultas con Promesas:**

Puedes ejecutar consultas SQL utilizando el objeto `connection` y trabajar con promesas para manejar los resultados:

```js
try {
  const [rows, fields] = await connection.execute('SELECT * FROM tabla');
  console.log('Resultados:', rows);
} catch (err) {
  console.error('Error al ejecutar la consulta:', err);
}

```

Puedes ejecutar consultas SQL utilizando el objeto `connection` y trabajar con promesas para manejar los resultados:

```js
try {
  const [rows, fields] = await connection.execute('SELECT * FROM tabla');
  console.log('Resultados:', rows);
} catch (err) {
  console.error('Error al ejecutar la consulta:', err);
}

```