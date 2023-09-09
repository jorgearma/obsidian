
```js
const http = require('http');

// Crear un servidor HTTP
const server = http.createServer((req, res) => {
    // Configurar encabezados de respuesta
    res.writeHead(200, {'Content-Type': 'text/plain'});
    
    // Manejar diferentes rutas
    if (req.url === '/') {
        res.write('¡Bienvenido a mi servidor web!');
    } else if (req.url === '/about') {
        res.write('Acerca de nosotros');
    } else {
        res.write('Ruta no encontrada');
    }

    // Finalizar la respuesta
    res.end();
});

// Escuchar en el puerto 3000
const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Servidor corriendo en el puerto ${PORT}`);
});

```

1. **Creación del Servidor:**
    
    - Utiliza `http.createServer()` para crear un servidor HTTP.
    - Define una función de callback que maneje las solicitudes entrantes.
2. **Manejo de Solicitudes y Respuestas:**
    
    - La función de callback recibe dos objetos: `req` (request) y `res` (response).
    - `req` contiene información sobre la solicitud, como URL, encabezados y datos del cuerpo.
    - `res` se utiliza para enviar respuestas, configurando encabezados y escribiendo el contenido de la respuesta.
3. **Configuración de Encabezados:**
    
    - Usa `res.writeHead()` para establecer encabezados de respuesta, como el código de estado HTTP y otros encabezados.
4. **Envío de Contenido:**
    
    - Utiliza `res.write()` para escribir contenido en la respuesta.
    - Finaliza la respuesta con `res.end()`.
5. **Escucha en un Puerto:**
    
    - Usa `server.listen(PORT, callback)` para iniciar el servidor en un puerto específico.
    - El callback se ejecuta cuando el servidor está listo para recibir conexiones.
6. **Consideraciones:**
    
    - El ejemplo básico incluye la creación de un servidor que responde con "helloooooo" y muestra la URL de la solicitud.
    - Para aplicaciones más complejas, considera usar frameworks como Express para manejar enrutamiento, manejo de parámetros y otros aspectos de manera más sencilla.