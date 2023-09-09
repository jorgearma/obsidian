1. **Express (`express`)**:
    
    - Descripción: Express.js es un framework web para Node.js que simplifica la creación de aplicaciones web y APIs.
    - Uso Común: Manejo de rutas, middleware, creación de endpoints, manejo de solicitudes y respuestas HTTP, construcción de APIs.
```js 
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('¡Hola, mundo!');
});

app.listen(3000, () => {
  console.log('La aplicación está corriendo en http://localhost:3000');
});

```
1. **Bcrypt.js (`bcryptjs`)**:
    
    - Descripción: Bcrypt.js es una biblioteca para cifrar contraseñas y realizar hashing de manera segura.
    - Uso Común: Hashing de contraseñas antes de almacenarlas en la base de datos para mayor seguridad.
```js
const bcrypt = require('bcryptjs');

const password = 'miContraseñaSecreta';
const hashedPassword = bcrypt.hashSync(password, 10);

console.log('Contraseña cifrada:', hashedPassword);

```
1. **CORS (`cors`)**:
    
    - Descripción: CORS (Cross-Origin Resource Sharing) es un middleware que permite controlar las políticas de seguridad relacionadas con las solicitudes HTTP entre diferentes dominios.
    - Uso Común: Habilitar comunicación entre dominios diferentes en aplicaciones web y APIs.
```js
const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors()); // Habilitar CORS para todas las rutas

// Rutas y lógica de la aplicación
// ...

app.listen(3000, () => {
  console.log('La aplicación está corriendo en http://localhost:3000');
});

```
1. **dotenv (`dotenv`)**:
    
    - Descripción: Dotenv es una biblioteca que permite cargar variables de entorno desde archivos `.env` en el proceso de Node.js.
    - Uso Común: Almacenar configuraciones sensibles (como claves API, contraseñas de bases de datos) de manera segura en archivos `.env`.
```js
require('dotenv').config();

const apiKey = process.env.API_KEY;
const dbPassword = process.env.DB_PASSWORD;

console.log('API Key:', apiKey);
console.log('Contraseña de la base de datos:', dbPassword);

```
1. **JSON Web Token (`jsonwebtoken`)**:
    
    - Descripción: JSON Web Token (JWT) es un estándar abierto que define una forma compacta y segura de transmitir información entre dos partes en forma de objetos JSON.
    - Uso Común: Crear tokens de autenticación para usuarios, transmitir información segura en la solicitud entre cliente y servidor.
```js
const jwt = require('jsonwebtoken');

const secretKey = 'miClaveSecreta';
const payload = { userId: 123 };

const token = jwt.sign(payload, secretKey, { expiresIn: '1h' });
console.log('Token JWT:', token);

const decodedToken = jwt.verify(token, secretKey);
console.log('Decodificado:', decodedToken);

```
1. **Mongoose (`mongoose`)**:
    
    - Descripción: Mongoose es una biblioteca de modelado de objetos para MongoDB en Node.js. Simplifica la interacción con la base de datos y proporciona una estructura para definir modelos y esquemas.
    - Uso Común: Conectar y comunicarse con bases de datos MongoDB, definir esquemas y modelos, realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

```js
const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/mydb', { useNewUrlParser: true, useUnifiedTopology: true });

const userSchema = new mongoose.Schema({
  username: String,
  email: String,
  password: String
});

const User = mongoose.model('User', userSchema);

// Crear un nuevo usuario
const newUser = new User({ username: 'usuario1', email: 'usuario@example.com', password: 'contraseña' });
newUser.save().then(user => console.log('Usuario guardado:', user));

// Consultar usuarios
User.find().then(users => console.log('Usuarios:', users));

```
1. **Morgan (`morgan`)**:
    
    - Descripción: Morgan es un middleware de registro de solicitudes HTTP para Express. Genera registros detallados de las solicitudes entrantes.
    - Uso Común: Registrar información sobre las solicitudes HTTP entrantes, como métodos, rutas, códigos de estado y tiempos de respuesta.
```js
const express = require('express');
const morgan = require('morgan');

const app = express();

app.use(morgan('dev')); // Registro de solicitudes en formato 'dev'

// Rutas y lógica de la aplicación
// ...

app.listen(3000, () => {
  console.log('La aplicación está corriendo en http://localhost:3000');
});

```
1. **Helmet (`helmet`)**:
    
    - Descripción: Helmet es un conjunto de middleware que ayuda a proteger las aplicaciones Express configurando encabezados HTTP relacionados con la seguridad.
    - Uso Común: Configurar encabezados HTTP para mitigar ataques comunes, como XSS (Cross-Site Scripting) y secuestro de clics.
```js
const express = require('express');
const helmet = require('helmet');

const app = express();

app.use(helmet()); // Configurar encabezados de seguridad

// Rutas y lógica de la aplicación
// ...

app.listen(3000, () => {
  console.log('La aplicación está corriendo en http://localhost:3000');
});

```