## Atributos de un DataFrame

Existen varias propiedades o métodos para ver las características de un DataFrame `df`:

### Información General

- **`df.info()`**: Devuelve información sobre el DataFrame, incluyendo el número de filas, columnas, índices, tipo de las columnas y memoria usada.

- **`df.shape`**: Devuelve una tupla con el número de filas y columnas del DataFrame.

- **`df.size`**: Devuelve el número total de elementos en el DataFrame.

### Nombres y Tipos

- **`df.columns`**: Devuelve una lista con los nombres de las columnas del DataFrame.

- **`df.index`**: Devuelve una lista con los nombres de las filas del DataFrame.

- **`df.dtypes`**: Devuelve una serie con los tipos de datos de las columnas del DataFrame.

### Visualización de Datos

- **`df.head(n)`**: Devuelve las primeras `n` filas del DataFrame.

- **`df.tail(n)`**: Devuelve las últimas `n` filas del DataFrame.


## Accesos Mediante Posiciones

En un DataFrame `df`, puedes acceder a los elementos y subconjuntos de datos utilizando la indexación basada en posiciones con `iloc`:

- **`df.iloc[i, j]`**: Devuelve el elemento que se encuentra en la fila `i` y la columna `j` del DataFrame. También puedes usar secuencias de índices para obtener partes del DataFrame.

- **`df.iloc[filas, columnas]`**: Devuelve un DataFrame con los elementos de las filas especificadas en la lista `filas` y de las columnas especificadas en la lista `columnas`.

- **`df.iloc[i]`**: Devuelve una serie con los elementos de la fila `i` del DataFrame.


## Funciones Estadísticas y de Resumen para un DataFrame

Estas funciones permiten obtener diversos resúmenes y estadísticas sobre un DataFrame `df`:

- **`df.count()`**: Devuelve una serie con el número de elementos que no son nulos ni NaN en cada columna del DataFrame.

- **`df.sum()`**: Devuelve una serie con la suma de los datos en las columnas del DataFrame. Si los datos son numéricos, devuelve la suma; si son cadenas `str`, devuelve la concatenación de los valores.

- **`df.cumsum()`**: Devuelve un DataFrame con la suma acumulada de los datos en las columnas del DataFrame cuando los datos son numéricos.

- **`df.min()`**: Devuelve una serie con los menores valores en cada columna del DataFrame.

- **`df.max()`**: Devuelve una serie con los mayores valores en cada columna del DataFrame.

- **`df.mean()`**: Devuelve una serie con las medias de los datos en las columnas numéricas del DataFrame.

- **`df.var()`**: Devuelve una serie con las varianzas de los datos en las columnas numéricas del DataFrame.

- **`df.std()`**: Devuelve una serie con las desviaciones típicas de los datos en las columnas numéricas del DataFrame.

- **`df.cov()`**: Devuelve un DataFrame con las covarianzas de los datos en las columnas numéricas del DataFrame.

- **`df.corr()`**: Devuelve un DataFrame con los coeficientes de correlación de Pearson de los datos en las columnas numéricas del DataFrame.

- **`df.describe(include=tipo)`**: Devuelve un DataFrame con un resumen estadístico de las columnas del DataFrame. El parámetro `tipo` puede ser:
  - `'number'`: Calcula la media, desviación típica, mínimo, máximo y cuartiles para datos numéricos.
  - `'object'`: Calcula el número de valores, el número de valores distintos, la moda y su frecuencia para datos no numéricos.
  
  Si no se especifica el tipo, solo se consideran las columnas numéricas.
