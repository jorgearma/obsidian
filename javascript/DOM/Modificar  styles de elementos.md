## modificar con clases
```java
/*
	📌 Podemos modificar los estilos CSS de un elemento de dos formas:
	- Agregando y quitando clases CSS
	- Modificando los estilos "inline" de cada elemento.
*/

/*
	📌 Modificar estilos CSS mediante clases
*/
const primeraCaja = document.querySelector('#contenedor1 .caja');

// classList - Nos permite obtener una lista de las clases del elemento
console.log(primeraCaja.classList);

// classList.add() - Nos permite agregar clases a un elemento.
const agregarClase = () => {
	primeraCaja.classList.add('activa');
};

// classList.remove() - Nos permite eliminar clases de un elemento
const eliminarClase = () => {
	primeraCaja.classList.remove('activa');
};

// classList.toggle() - Nos permite alternar clases de un elemento
const toggleClase = () => {
	primeraCaja.classList.toggle('activa');
};

// classList.contains() - Nos permite comprobar si el elemento contiene una clase
const comprobarClase = () => {
	if (primeraCaja.classList.contains('activa')) {
		console.log('La caja tiene la clase "activa"');
	} else {
		console.log('La caja no tiene la clase "activa"');
	}

	console.log('y contiene las siguientes clases:');
	// classList.forEach() - Nos permite iterar sobre cada clase
	primeraCaja.classList.forEach((clase) => {
		console.log(clase);
	});
};
```



## modicar con javacript
```java
/*
	📌 Podemos modificar los estilos CSS de un elemento de dos formas:
	- Agregando y quitando clases CSS
	- Modificando los estilos "inline" de cada elemento.
*/

/*
	📌 Modificar estilos CSS mediante "inline styles".
*/
/*
	Los estilos inline se aplican arriba de los estilos que podamos tener en archivos CSS.
	Estos estilos se agregan en el atributo style del elemento.
*/
const ultimaCaja = document.querySelector('#contenedor2 .caja:last-child');

ultimaCaja.style.background = '#000';
ultimaCaja.style.color = '#fff';

/*
	📌 La ventaja de trabajar con estilos inline es que podemos modificar los estilos de forma dinamica.
*/
const cajas = document.querySelectorAll('.caja');
let tamaño = 24;
const incrementarFuente = () => {
	cajas.forEach((caja) => {
		caja.style.fontSize = `${tamaño + 1}px`;
		tamaño++;
	});
};

const disminuirFuente = () => {
	cajas.forEach((caja) => {
		if (tamaño > 8) {
			caja.style.fontSize = `${tamaño - 1}px`;
			tamaño--;
		}
	});
};
```