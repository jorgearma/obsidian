

```js
const busquedaBinaria = (lista, valorBuscado) => {
  let inicio = 0;
  let fin = lista.length - 1;

  while (inicio <= fin) {
    let mitad = Math.floor((inicio + fin) / 2);

    if (lista[mitad] === valorBuscado) {
      return mitad; // Se encontró el valor en la posición     mitad
    } else if (lista[mitad] < valorBuscado) {
      inicio = mitad + 1; // El valor buscado está en la mitad superior
    } else {
      fin = mitad - 1; // El valor buscado está en la mitad inferior
    }
  }

  return -1; // No se encontró el valor en la lista
};

// Ejemplo de uso
const lista = [2, 4, 7, 10, 14, 18, 21];
const valor = 10;

const resultado = busquedaBinaria(lista, valor);
if (resultado === -1) {
  console.log("El valor no se encontró en la lista.");
} else {
  console.log(`El valor se encontró en la posición ${resultado}.`);
}

```