
```java
/*
	📌 Named Exports
	
	Podemos exportar variables y funciones utilizando named exports o default exports.
	Cuando trabajamos con named exports podemos exportar multiples cosas.
	Podemos exportar de dos formas:
	- Agregando la palabra export antes de la variable.
	- Al final de documento
*/

// Forma 1 - Palabra export
export const nombre = 'Carlos Arturo';

export const obtenerPosts = () => {
	return ['Post1', 'Post2', 'Post3'];
};

// Forma 2 - Final del documento
 const nombre = 'Carlos Arturo';

 const obtenerPosts = () => {
 	return ['Post1', 'Post2', 'Post3'];
 };

 export { nombre, obtenerPosts };
```

## defauls exports

```java
/*
	📌 Default Exports
	Cuando trabajamos con default exports solo podemos exportar una cosa del archivo.
	Con la ventaja de que podemos importarlo con el nombre que queramos
	
	Podemos exportar de dos formas:
	- Mediante las palabras export default antes de la variable. (No podemos usar var, const, let)
	- Al final de documento mediante las palabras export default <nombre_variable>
*/

// Forma 1 - mediante palabras export default
// export default () => {
// 	return {
// 		nombre: 'Carlos',
// 		correo: 'correo@correo.com',
// 	};
// };

// Forma 2 - Final del documento
const obtenerUsuario = () => {
	return {
		nombre: 'Carlos',
		correo: 'correo@correo.com',
	};
};

export default obtenerUsuario;
```

## empty exports

```java
console.log('Soy codigo que se ejecuta desde el archivo emptyExport.js');

export const correo = 'correo@correo.com';
```