faztfarz mongo1.
```sh
npm init

npm install @types/express --save-dev

```

2.
```sh
npm i express bcryptjs cors dotenv jsonwebtoken mongoose morgan helmet
```

 Babel es una herramienta fundamental en el desarrollo de JavaScript que permite convertir código moderno en versiones compatibles con navegadores y entornos más antiguos
3.
```sh
npm i @babel/core @babel/cli @babel/node @babel/preset-env nodemon -D
```

4.
```js
const express = require('express');
const app = express();
const port = 3000; // Puedes cambiar este puerto si es necesario

app.get('/', (req, res) => {
  res.send('¡Hola, mundo!');
});

app.listen(port, () => {
  console.log(`La aplicación está corriendo en http://localhost:${port}`);
});

```


# package.json

"scripts": {
    "build": "babel src --out-dir dist",
    "dev": "nodemon src/index.js --exec babel-node",
    "dev": "node build/index.js"
  },

```json
{
  "name": "api_autentificacion",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "build": "babel src --out-dir dist",
    "dev": "nodemon src/index.js --exec babel-node",
    "dev": "node build/index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "bcryptjs": "^2.4.3",
    "cors": "^2.8.5",
    "dotenv": "^16.3.1",
    "express": "^4.18.2",
    "helmet": "^7.0.0",
    "jsonwebtoken": "^9.0.1",
    "mongoose": "^7.4.5",
    "morgan": "^1.10.0"
  },
  "devDependencies": {
    "@babel/cli": "^7.22.10",
    "@babel/core": "^7.22.11",
    "@babel/node": "^7.22.10",
    "@babel/preset-env": "^7.22.10",
    "nodemon": "^3.0.1"
  }
}


```

# carpetas

```sh
 mkdir controllers libs middlewares models routes 
  touch database.js database.js
```

```sh
project-root/
├─ src/
│   ├─ controllers/
│   ├─ libs/
│   ├─ middlewares/
│   ├─ models/
│   ├─ routes/
│   ├─ views/
│   └─ app.js
├─ public/
├─ tests/
├─ config/
├─ package.json
├─ package-lock.json
└─ README.md

```