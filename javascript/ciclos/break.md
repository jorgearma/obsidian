**Break**: La instrucción `break` se utiliza para salir inmediatamente de un ciclo, sin importar si la condición del ciclo todavía es verdadera. Cuando se encuentra la instrucción `break` dentro de un ciclo, el flujo del programa salta inmediatamente fuera del ciclo y continúa con la próxima instrucción después del ciclo.

```js ejemplo
for (let i = 1; i <= 10; i++) {
  if (i === 5) {
    break; // Sale del ciclo cuando i es igual a 5
  }
  console.log(i);
}

```
En este ejemplo, cuando `i` es igual a 5, se encuentra la instrucción `break` y se sale del ciclo `for` sin imprimir los números restantes. La salida será: `1 2 3 4`.


```js
const nombres = ['Arturo', 'Andres', 'Alejandro', 'Roberto', 'Adrian', 'Antonio', 'Angel'];

 for (let i = 0; i < nombres.length; i++) {
 	if (nombres[i][0] !== 'A') {
 		console.log('ALTO! Hay un nombre que no empieza por la letra A');
 		console.log(nombres[i] + ' no empieza por la letra A');
 		break;
 	}

 	console.log(nombres[i]);
 }
```