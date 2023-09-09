
1 ejemplo de manejo de peticiones

```js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('¡Hola, mundo!');
});

app.listen(3000, () => {
  console.log('Servidor escuchando en el puerto 3000');
});

```

## post 

```js
app.post('/crear', (req, res) => {
  // Aquí puedes manejar la creación de un recurso en la base de datos
  res.status(201).send('Recurso creado exitosamente');
});

```

## put
```js
app.put('/actualizar/:id', (req, res) => {
  const resourceId = req.params.id;
  // Aquí puedes manejar la actualización del recurso con el ID proporcionado
  res.send(`Recurso ${resourceId} actualizado`);
});

```

## delete
```js
app.delete('/eliminar/:id', (req, res) => {
  const resourceId = req.params.id;
  // Aquí puedes manejar la eliminación del recurso con el ID proporcionado
  res.send(`Recurso ${resourceId} eliminado`);
});

```

. **Enviar Códigos de Estado:**

Puedes enviar códigos de estado personalizados en Express utilizando el método `res.status()` antes de enviar la respuesta:

```js
app.get('/no-encontrado', (req, res) => {
  res.status(404).send('Recurso no encontrado');
});

app.get('/error-interno', (req, res) => {
  res.status(500).send('Error interno del servidor');
});

```