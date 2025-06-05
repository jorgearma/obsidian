1. Arreglos (Arrays):
    
    - Uso: Los arreglos son útiles cuando necesitas almacenar una colección de elementos del mismo tipo y acceder a ellos mediante un índice numérico.
    - Métodos comunes:
        - `push()`: Agrega un elemento al final del arreglo.
        - `pop()`: Elimina y devuelve el último elemento del arreglo.
        - `splice()`: Permite agregar, eliminar o reemplazar elementos en posiciones específicas del arreglo.
        - `forEach()`: Ejecuta una función para cada elemento del arreglo.
        - `filter()`: Retorna un nuevo arreglo con los elementos que cumplen una condición dada.
```js 
// Crear un arreglo y acceder a elementos por índice
let arreglo = [1, 2, 3, 4, 5];
console.log(arreglo[2]); // Salida: 3

// Agregar un elemento al final del arreglo
arreglo.push(6);
console.log(arreglo); // Salida: [1, 2, 3, 4, 5, 6]

// Eliminar el último elemento del arreglo
arreglo.pop();
console.log(arreglo); // Salida: [1, 2, 3, 4, 5]

// Reemplazar un elemento en una posición específica del arreglo
arreglo.splice(2, 1, 'nuevo elemento');
console.log(arreglo); // Salida: [1, 2, 'nuevo elemento', 4, 5]

// Iterar sobre cada elemento del arreglo
arreglo.forEach((elemento) => {
  console.log(elemento);
});

```





```js
const colores = ['Rojo', 'Verde', 'Azul'];

/* 
	📌 .length 
	(propiedad) - Nos permite conocer la cantidad de elementos de un arreglo.
*/
console.log(colores.length);

/*
	📌 .toString() 
	Nos permite transformar un arreglo a una cadena de texto.
	Por ejemplo para poder mostrarlo en el navegador.
*/
 document.body.innerHTML = colores.toString();

/*
	📌 .join()
	Nos permite transformar un arreglo a una cadena de texto y separar cada elemento. 
*/
console.log(colores.join('- -'));

/*
	📌 .sort()
	Nos permite ordenar un arreglo de cadenas de texto, de forma alfabetica.
*/
const letras = ['c', 'b', 'd', 'a'];
console.log(letras.sort());

const numeros = [3, 2, 4, 1];
console.log(numeros.sort());

/*
	📌 .reverse()
	Nos permite ordenar un arreglo de forma descendente. 
*/
console.log(letras.reverse());
console.log(numeros.reverse());

/*
	📌 .concat()
	Nos permite juntar dos arreglos en uno solo. 
*/
const arreglo1 = [1, 2, 3];
const arreglo2 = ['A', 'B', 'C'];
const arreglo3 = arreglo1.concat(arreglo2);

console.log(arreglo3);

/* 
	📌 .push()
	Nos permite agregar un elemento al final de un arreglo.
*/
colores.push('Amarillo');
console.log(colores);

/*
	📌 .pop()
	Nos permite eliminar el ultimo elemento de un arrreglo. 
*/
colores.pop();
console.log(colores);

/* 
	📌 .shift()
	Elimina el primer elemento de un arreglo y recorre los elementos.
*/
const dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];
 const diaEliminado = dias.shift();
 console.log(diaEliminado);
console.log(dias[0]);

/*
	📌 .unshift()
	Agrega un elemento al inicio del arreglo y empuja los elementos.
*/
dias.unshift('Carlos');
console.log(dias);
/* 
	📌 .splice()
	Nos permite insertar elementos a un arreglo donde le especifiquemos.
	- 1er parametro - Posición donde queremos comenzar a insertar los elementos.
	- 2do parametro - Si queremos eliminar elementos del arreglo desde la posición indicada.
	- Resto de parametros - Los elementos a insertar.
*/
const amigos = ['Alejandro', 'Cesar', 'Manuel'];
amigos.splice(0, 0, 'Rafael', 'Roberto');
console.log(amigos);

/* 📌 .slice()
	Nos permite copiar una parte de un arreglo a otro.
	- 1er parametro - Posición desde donde queremos copiar.
	- 2do parametro - Hasta antes de que elemento copiar.
*/
const frutas = ['Fresa', 'Manzana', 'Uva', 'Piña', 'Mango', 'Naranja', 'Melon'];
const frutasFavoritas = frutas.slice(1, 5);
console.log(frutasFavoritas);

/* 📌 .indexOf()
	Obtenemos el primer index de un elemento.
	Si no hay elemento nos retorna -1
*/
const nombres = ['Carlos', 'Rafael', 'Estefania', 'Rodrigo', 'Rafael', 'Gema', 'Diana', 'Sara'];
// console.log(nombres.indexOf('Sergio'));

/* 
	📌 .lastIndexOf() 
	Obtenemos el último index de un elemento.
*/
// console.log(nombres.lastIndexOf('Rafael'));

/* 	
	📌 .forEach()
	Nos permite ejecutar una funcion por cada elemento
*/
 nombres.forEach((nombre, index) => {
 	console.log(`Hola ${nombre} (${index})`);
 });

/* 
	📌 .find()
	Nos permite recorrer un arreglo y devuelve el PRIMER elemento que retornemos.
*/
 const resultado = nombres.find((nombre) => {
 	if (nombre[0] === 'E') {
 		return nombre;
 	}
 });
 console.log(resultado);

/* 
	📌 .map()
	Nos permite ejecutar una función por cada elemento y crear un nuevo arreglo
	en base a los resultados de esa función.
*/
 const nombresMayusculas = nombres.map((nombre) => nombre.toUpperCase());
 console.log(nombresMayusculas);

/* 📌 .filter()
	Nos permite ejecutar una función por cada elemento 
	y luego crear un arreglo en base a los resultados de esa función. 
*/
 const nombres4Letras = nombres.filter((nombre) => {
 	if (nombre.length === 5) {
 		return nombre;
 	}
 });
 console.log(nombres4Letras);

/* 
	📌 .includes()
	Nos permite saber si el arreglo contiene un elemento especificado 
*/
 console.log(nombres.includes('Julio'));
 console.log(nombres.includes('Carlos'));

/* 
	📌 .every()
	Nos permite ejecutar un condicional sobre cada elemento y 
	nos devuelve true si TODOS los elemento cumplieron la condición.
*/
 const nombresValidos = nombres.every((nombre) => {
 	if (typeof nombre === 'string') {
 		return true;
 	} else {
 		return false;
 	}
 });
 console.log('¿Todos los nombres son validos? ' + nombresValidos);

/* 
	📌 .some()
	Nos permite ejecutar un condicional sobre cada elemento y
	nos devuelve true si algun elemento cumplio la condición.
*/
const nombresValidos = nombres.some((nombre) => {
	if (typeof nombre !== 'string') {
		return true;
	} else {
		return false;
	}
});
console.log('¿El arreglo es invalido? ' + nombresValidos);
// true si hay algun valor invalido
// false si no hay algun valor invalido
```