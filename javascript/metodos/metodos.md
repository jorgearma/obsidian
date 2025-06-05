
```js
// Los siguientes 40 (ordenados alfabéticamente):
// 21. Concatenar arrays.
var array1 = [1, 2, 3];
var array2 = [4, 5];
var resultado = array1.concat(array2);

// 22. Verificar si todos los elementos de un array cumplen un criterio.
var miArray = [2, 4, 6];
var todosPares = miArray.every(function(elemento) {
  return elemento % 2 === 0;
});

// 23. Encontrar el primer elemento que cumple un criterio.
var miArray = [10, 20, 30];
var encontrado = miArray.find(function(elemento) {
  return elemento > 15;
});

// 24. Encontrar el índice del primer elemento que cumple un criterio.
var miArray = [10, 20, 30];
var indice = miArray.findIndex(function(elemento) {
  return elemento > 15;
});

// 25. Unir todos los elementos de un array en una cadena.
var miArray = ['Hola', ' ', 'mundo'];
var resultado = miArray.join('');

// 26. Encontrar el último índice de un elemento en un array.
var miArray = [1, 2, 3, 4, 2];
var ultimoIndice = miArray.lastIndexOf(2);

// 27. Crear una copia superficial de una parte de un array.
var miArray = [1, 2, 3, 4, 5];
var copia = miArray.slice(1, 4);

// 28. Verificar si al menos un elemento de un array cumple un criterio.
var miArray = [2, 4, 7];
var algunPar = miArray.some(function(elemento) {
  return elemento % 2 === 0;
});

// 29. Ordenar los elementos de un array.
var miArray = [3, 1, 2];
miArray.sort();

// 30. Verificar si un valor es un array.
var miArray = [1, 2, 3];
var esArray = Array.isArray(miArray);

// 31. Obtener la hora actual en milisegundos.
var milisegundos = Date.now();

// 32. Obtener el día del mes de una fecha.
var fecha = new Date();
var dia = fecha.getDate();

// 33. Obtener el mes de una fecha (0 = enero).
var fecha = new Date();
var mes = fecha.getMonth();

// 34. Obtener el año de una fecha.
var fecha = new Date();
var año = fecha.getFullYear();

// 35. Obtener las horas de una fecha (0-23).
var fecha = new Date();
var horas = fecha.getHours();

// 36. Obtener los minutos de una fecha (0-59).
var fecha = new Date();
var minutos = fecha.getMinutes();

// 37. Obtener los segundos de una fecha (0-59).
var fecha = new Date();
var segundos = fecha.getSeconds();

// 38. Convertir una fecha a su representación en formato ISO.
var fecha = new Date();
var isoString = fecha.toISOString();

// 39. Crear un nuevo elemento HTML.
var nuevoElemento = document.createElement('div');

// 40. Seleccionar elementos del DOM usando selectores CSS.
var elementos = document.querySelectorAll('.miClase');


// Los 20 más utilizados:
// 1. Obtener un elemento del DOM por su ID.
document.getElementById('miElemento');

// 2. Seleccionar elementos del DOM usando selectores CSS.
document.querySelector('.miClase');

// 3. Agregar oyentes de eventos a elementos del DOM.
document.addEventListener('click', function(event) {
  // Tu código aquí
});

// 4. Acceder y modificar el contenido HTML de un elemento.
var elemento = document.getElementById('miElemento');
elemento.innerHTML = 'Nuevo contenido';

// 5. Acceder y modificar el contenido de texto de un elemento.
var elemento = document.getElementById('miElemento');
elemento.textContent = 'Nuevo texto';

// 6. Agregar un elemento como hijo de otro.
var nuevoElemento = document.createElement('div');
var contenedor = document.getElementById('contenedor');
contenedor.appendChild(nuevoElemento);

// 7. Eliminar un hijo de un elemento.
var hijo = document.getElementById('hijo');
var padre = hijo.parentNode;
padre.removeChild(hijo);

// 8. Crear un nuevo elemento HTML.
var nuevoElemento = document.createElement('div');

// 9. Establecer atributos en un elemento.
var elemento = document.getElementById('miElemento');
elemento.setAttribute('data-color', 'rojo');

// 10. Obtener el valor de un atributo de un elemento.
var elemento = document.getElementById('miElemento');
var valor = elemento.getAttribute('data-color');

// 11. Trabajar con las clases CSS de un elemento.
var elemento = document.getElementById('miElemento');
elemento.classList.add('nuevaClase');

// 12. Agregar elementos a un array.
var miArray = [1, 2, 3];
miArray.push(4);

// 13. Eliminar y devolver el último elemento de un array.
var miArray = [1, 2, 3];
var ultimoElemento = miArray.pop();

// 14. Eliminar y devolver el primer elemento de un array.
var miArray = [1, 2, 3];
var primerElemento = miArray.shift();

// 15. Agregar elementos al principio de un array.
var miArray = [2, 3];
miArray.unshift(1);

// 16. Iterar sobre los elementos de un array.
var miArray = [1, 2, 3];
miArray.forEach(function(elemento) {
  console.log(elemento);
});

// 17. Crear un nuevo array a partir de un array existente.
var miArray = [1, 2, 3];
var nuevoArray = miArray.map(function(elemento) {
  return elemento * 2;
});

// 18. Crear un nuevo array con elementos que cumplan cierto criterio.
var miArray = [1, 2, 3, 4, 5];
var nuevoArray = miArray.filter(function(elemento) {
  return elemento % 2 === 0;
});

// 19. Reducir un array a un solo valor mediante una función acumuladora.
var miArray = [1, 2, 3, 4];
var resultado = miArray.reduce(function(acumulador, elemento) {
  return acumulador + elemento;
}, 0);

// 20. Verificar si un elemento está presente en un array.
var miArray = [1, 2, 3];
var estaPresente = miArray.includes(2);

```