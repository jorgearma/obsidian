El bucle "for...in" en JavaScript es una estructura de control utilizada para iterar sobre las propiedades enumerables de un objeto

base
```js
for (variable in objeto) {
  // bloque de código a ejecutar
}
```

ejm
```js
 const persona = {
 	nombre: 'Carlos',
 	edad: 27,
 	correo: 'correo@correo.com',
 };

 for (propiedad in persona) {
 	persona[propiedad] = '';
 }
 console.log(persona);
```