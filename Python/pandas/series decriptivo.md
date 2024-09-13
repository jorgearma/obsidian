## Resumen Descriptivo de una Serie

Las siguientes funciones permiten resumir varios aspectos de una serie `s`:

- **`s.count()`**: Devuelve el número de elementos que no son nulos ni NaN en la serie `s`.

- **`s.sum()`**: Devuelve la suma de los datos de la serie `s` cuando los datos son de un tipo numérico, o la concatenación de ellos cuando son del tipo cadena `str`.

- **`s.cumsum()`**: Devuelve una serie con la suma acumulada de los datos de la serie `s` cuando los datos son de un tipo numérico.

- **`s.value_counts()`**: Devuelve una serie con la frecuencia (número de repeticiones) de cada valor de la serie `s`.

- **`s.min()`**: Devuelve el menor de los datos de la serie `s`.

- **`s.max()`**: Devuelve el mayor de los datos de la serie `s`.

- **`s.mean()`**: Devuelve la media de los datos de la serie `s` cuando los datos son de un tipo numérico.

- **`s.var()`**: Devuelve la varianza de los datos de la serie `s` cuando los datos son de un tipo numérico.

- **`s.std()`**: Devuelve la desviación típica de los datos de la serie `s` cuando los datos son de un tipo numérico.

- **`s.describe()`**: Devuelve una serie con un resumen descriptivo que incluye el número de datos, su suma, el mínimo, el máximo, la media, la desviación típica y los cuartiles.
