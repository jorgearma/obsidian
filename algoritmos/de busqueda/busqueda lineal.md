indexof()
find()
```js
const busquedaLineal = (lista, valorBuscado) => {
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] === valorBuscado) {
      return i; // Se encontró el valor en la posición i
    }
  }
  return -1; // No se encontró el valor en la lista
};

// Ejemplo de uso
const lista = [10, 4, 7, 2, 5];
const valor = 7;

const resultado = busquedaLineal(lista, valor);
if (resultado === -1) {
  console.log("El valor no se encontró en la lista.");
} else {
  console.log(`El valor se encontró en la posición ${resultado}.`);
}

```

## uso

1. Listas pequeñas: Cuando la lista en la que se realiza la búsqueda es pequeña, la diferencia de eficiencia entre la búsqueda lineal y otros algoritmos más eficientes puede ser insignificante. En este caso, la simplicidad y facilidad de implementación de la búsqueda lineal pueden ser preferibles.
    
2. Listas no ordenadas: Si la lista no está ordenada, la búsqueda lineal es una opción viable, ya que no se puede aplicar la búsqueda binaria u otros algoritmos de búsqueda eficientes que requieren una lista ordenada.
    
3. Búsqueda de elementos no frecuentes: Si estás buscando elementos que no se repiten con frecuencia en la lista, la búsqueda lineal puede ser suficientemente rápida. En este caso, los beneficios de los algoritmos de búsqueda más eficientes podrían no ser significativos.
    
4. Búsqueda secuencial: Si necesitas buscar elementos en una secuencia específica, como encontrar la primera ocurrencia de un elemento o buscar en orden hasta encontrar una condición específica, la búsqueda lineal es apropiada, ya que garantiza un recorrido secuencial de la lista.