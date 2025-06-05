

```js
// Obtenemos una colección HTML de las etiquetas.
const etiquetas = document.head.children;

// Las mostramos en pantalla.
for (elemento of etiquetas) {
	 console.log(elemento);
}

// Esto no funciona, porque etiquetas no tiene el metodo forEach.
// etiquetas.forEach((e) => console.log(e));

// Un truco para seguir usando forEach y no for of es transformar la colección a un arreglo


[...etiquetas].forEach((e) => console.log(e));
```