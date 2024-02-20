**setTimeout()**:

- Permite programar la ejecución de una función después de un cierto período de tiempo.
- Sintaxis: `setTimeout(callback, tiempoEnMilisegundos)`.
- Ejemplo:
```js
setTimeout(() => {
  console.log("¡Han pasado 3 segundos!");
}, 3000); // Ejecuta el callback después de 3 segundos

```

**setInterval()**:

- Programa la ejecución repetida de una función en intervalos regulares.
- Sintaxis: `setInterval(callback, intervaloEnMilisegundos)`.
- Ejemplo:
```js
let contador = 0;
const intervalo = setInterval(() => {
  console.log("Contador:", contador);
  contador++;
  if (contador === 5) {
    clearInterval(intervalo); // Detiene el intervalo después de 5 repeticiones
  }
}, 1000); // Ejecuta cada 1 segundo

```