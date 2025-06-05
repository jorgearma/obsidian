El bucle "while" en JavaScript es una estructura de control que se utiliza para repetir un bloque de código mientras se cumpla una condición específica. A diferencia del ciclo "for", el ciclo "while" no requiere una inicialización ni una actualización explícita de una variable de control. Su sintaxis básica es la siguiente:

```js
let i = 1;

while (numero <= 5) {
  console.log(numero);
  i++;
}
```

En este caso, se inicializa la variable `numero` en 1 antes del ciclo "while". La condición `numero <= 5` se evalúa antes de cada iteración. Si la condición es verdadera, se ejecuta el bloque de código, que en este caso imprime el valor de `numero` y luego incrementa `numero` en 1. El ciclo continúa hasta que la condición sea falsa (es decir, cuando `numero` es 6), momento en el que el ciclo se detiene. Como resultado, se imprimirán los números del 1 al 5 en la consola.

# do while

Es similar al ciclo while, con la diferencia de que ejecuta el bloque de código al menos una vez
```js
let i = 100;
do {
	console.log(i);
	i++;
} while (i <= 10);
```