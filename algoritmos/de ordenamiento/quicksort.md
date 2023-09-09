```js
const quick = (array) => {
  if (array.length <= 1) { // Si el array tiene longitud menor o igual a 1, no es necesario ordenarlo
    return array;
  }
  
  var pivote = array[0]; 
  var izquierda = []; 
  var derecha = []; 
  
  for (var i = 1; i < array.length; i++) {
    if (array[i] < pivote) {
      izquierda.push(array[i]); // Si el elemento es menor al pivote, lo agregamos a la parte izquierda
    } else {
      derecha.push(array[i]); // Si el elemento es mayor o igual al pivote, lo agregamos a la parte derecha
    }
  }
  
  // Llamamos recursivamente a la función quick en los subarrays izquierdo y derecho, y combinamos los resultados con el pivote
  return [...quick(izquierda), pivote, ...quick(derecha)];
}

const numerosss = [5, 5, 5, 2, 8, 1, 5, 1, 1, 10, 50, 3, 30, 7, 9];
console.log(quick(numerosss));

```