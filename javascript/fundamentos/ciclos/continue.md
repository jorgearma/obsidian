**Continue**: La instrucción `continue` se utiliza para saltar a la siguiente iteración del ciclo, sin ejecutar las instrucciones que le siguen dentro del ciclo. Cuando se encuentra la instrucción `continue`, se ignora el resto del bloque de código en esa iteración y se pasa a la siguiente iteración del ciclo.

```js
for (let i = 1; i <= 5; i++) {
  if (i === 3) {
    continue; // Salta la iteración cuando i es igual a 3
  }
  console.log(i);
}

```
En este ejemplo, cuando `i` es igual a 3, se encuentra la instrucción `continue` y se salta la ejecución de `console.log(i)`. El ciclo continúa con la siguiente iteración. La salida será: `1 2 4 5`.


```js
const invitados = ['Carlos', 'Christian', 'Christoher', 'Jorge', 'Estefania', 'Erika', 'Manuel'];
console.log('Lista de personas aceptadas:');

for (let i = 0; i < invitados.length; i++) {
	if (invitados[i] === 'Jorge') {
		continue;
	}
	console.log(invitados[i]);
}
```