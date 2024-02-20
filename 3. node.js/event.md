```js
const EventEmitter = require('events');

// Crear una instancia de EventEmitter
const miEmitter = new EventEmitter();

// Registrar un oyente para el evento personalizado 'saludo'
miEmitter.on('saludo', (nombre) => {
    console.log(`Hola, ${nombre}!`);
});

// Emitir el evento 'saludo' con un argumento
miEmitter.emit('saludo', 'Juan');

```


1. **EventEmitter**: La base del sistema de eventos en Node.js es la clase `EventEmitter`. Esta clase permite la creación de objetos que emiten eventos y a los cuales se pueden adjuntar oyentes para manejar esos eventos.
    
2. **Emitir eventos**: Un objeto `EventEmitter` emite un evento llamando al método `emit(eventName, ...args)`, donde `eventName` es el nombre del evento y `...args` son argumentos opcionales que pueden ser pasados a los oyentes del evento.
    
3. **Registrar oyentes**: Puedes registrar oyentes (funciones) para eventos específicos utilizando el método `on(eventName, listener)` o `addListener(eventName, listener)`. El oyente se ejecutará cuando se emita el evento correspondiente.
    
4. **Desregistrar oyentes**: Para dejar de escuchar eventos, puedes usar el método `removeListener(eventName, listener)` o `off(eventName, listener)`.
    
5. **Eventos predefinidos en Node.js**: Node.js también proporciona algunos eventos predefinidos, como el evento `'error'` que se emite cuando ocurre un error en una operación asíncrona.
6. 