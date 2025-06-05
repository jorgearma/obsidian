```sh 
npm install ejs
```

**Configuración de Express para usar EJS**: En tu archivo principal (por ejemplo, `app.js`), configura Express para utilizar EJS como motor de plantillas:

```js
const express = require('express');
const app = express();

// Configura EJS como motor de plantillas
app.set('view engine', 'ejs');

```

**Creación de vistas EJS**: Crea una carpeta llamada "views" en tu directorio del proyecto. Dentro de esta carpeta, coloca tus archivos de plantillas EJS con extensión `.ejs`. Estos archivos contendrán tu HTML con incrustaciones de código JavaScript:

Por ejemplo, crea un archivo `index.ejs` en la carpeta "views":

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mi Aplicación</title>
</head>
<body>
    <h1><%= title %></h1>
    <p>Bienvenido a <%= message %></p>
</body>
</html>

```

**Manejo de rutas en Express**: Define rutas en tu archivo principal (`app.js`) y utiliza el método `res.render()` para renderizar tus vistas EJS y pasar datos a ellas:

```js
app.get('/', (req, res) => {
    const data = {
        title: 'Mi Página',
        message: 'Esta es una página generada dinámicamente'
    };
    res.render('index', data);
});

```

1. **istas dinámicas**: Cuando un usuario acceda a la ruta `/`, Express utilizará EJS para renderizar el archivo `views/index.ejs` y reemplazar las variables entre `<%= %>` con los valores proporcionados en el objeto `data`.
    

Eso es básicamente cómo usar un motor de plantillas como EJS en conjunto con Express.js. Puedes seguir expandiendo esto para crear vistas más complejas y dinámicas en tu aplicación web. Recuerda que hay otros motores de plantillas disponibles como Handlebars, Pug, etc., que siguen un proceso similar.