```js
function insertionSort(array) {
    const length = array.length;

    // Empezamos desde el segundo elemento porque el primer elemento se considera "ordenado".
    for (let i = 1; i < length; i++) {
        const currentValue = array[i];
        let j = i - 1;

        // Comparamos el elemento actual con los elementos anteriores en el subarray "ordenado".
        while (j >= 0 && array[j] > currentValue) {
            // Si el elemento anterior es mayor, lo desplazamos una posición hacia adelante.
            array[j + 1] = array[j];
            j--;
        }

        // Encontramos la posición correcta para el elemento actual e insertamos.
        array[j + 1] = currentValue;
    }

    return array;
}

const unsortedArray = [5, 2, 9, 3, 1, 6];
const sortedArray = insertionSort(unsortedArray);
console.log(sortedArray);

```