[[2. javascript/fundamentos/variables]]

## scope global
son accesibles desde todo el codigo 
```java
/* 📌 Global Scope o Variables Globales
	- Son las variables declaradas fuera de una funcion.
	- Podemos acceder a ellas desde cualquier parte del código.
	- Podemos usar const, let y var.
*/

var nombre = 'Carlos';
console.log(nombre);

const saludo = () => {
	console.log('Hola ' + nombre);

	nombre = 'Arturo';
	console.log('El nuevo nombre es: ' + nombre);
};
saludo();
```

## scope local
se crea para acceder a ella dentro de la funcion  con let y const

```java
/* 📌 Local Scope o Variables Locales
	- Son las variables declaradas dentro de una función.
	- Solo podemos acceder a ellas desde dentro de la función.
*/
var numero = 1;

var obtenerNumeroLetras = (nombre) => {
	var numero = nombre.length;
	console.log(`${nombre} tiene ${numero} letras`);

	var funcionAnidada = () => {
		console.log(numero);
	};
	funcionAnidada();
};
obtenerNumeroLetras('Alex');
// console.log(numero);
```

## scope bloque
solo let y const

```java
/* 📌 Block Scope / Alcance de tipo bloque
	- Pertenecen las variables declaradas con const o let dentro de un bloque { }
	- Solo podemos acceder a ellas dentro del bloque
*/

 const edad = 19;
 if (edad >= 18) {
 	const accesoPermitido = true;

 	if (true) {
 		console.log(accesoPermitido);
 	}

 	const miFuncion = () => {
 		console.log(accesoPermitido);
 	};
 	miFuncion();
 }

 const accesoPermitido = 'SI';
 console.log(accesoPermitido);

if (true) {
	let nombre = 'Carlos';
}

console.log(nombre);
```