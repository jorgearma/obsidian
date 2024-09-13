# Medidas de Tendencia Central

### 1. **Media (promedio)**

La **media** es el promedio de un conjunto de datos. Se obtiene sumando todos los valores y dividiéndolos entre el número total de elementos. Es útil cuando los datos están distribuidos de forma más o menos uniforme.


- En Pandas: `df['columna'].mean()`

### 2. **Mediana**

La **mediana** es el valor central cuando los datos están ordenados. Si el conjunto tiene un número par de datos, la mediana es el promedio de los dos valores centrales. Es más robusta que la media cuando existen valores atípicos (outliers).

- En Pandas: `df['columna'].median()`

### 3. **Moda**

La **moda** es el valor que aparece con mayor frecuencia en un conjunto de datos. Puede haber más de una moda si varios valores tienen la misma frecuencia máxima.

- En Pandas: `df['columna'].mode()`

---

# Medidas de Dispersión

### 1. **Varianza**

La **varianza** mide la dispersión de los datos respecto a la media. Una varianza alta indica que los datos están muy dispersos, mientras que una varianza baja significa que están más concentrados alrededor de la media.

- En Pandas: `df['columna'].var()`

### 2. **Desviación Estándar**

La **desviación estándar** es la raíz cuadrada de la varianza. Proporciona una medida de la dispersión en las mismas unidades que los datos originales, lo que facilita su interpretación.

- En Pandas: `df['columna'].std()`

---

# Percentiles y Cuartiles

### 1. **Percentiles**

Los **percentiles** dividen los datos en 100 partes iguales. Por ejemplo, el percentil 25 es el valor por debajo del cual se encuentra el 25% de los datos.

- En Pandas: `df['columna'].quantile(0.25)` (para el percentil 25)

### 2. **Cuartiles**

Los **cuartiles** dividen un conjunto de datos en cuatro partes iguales:

- **Q1 (primer cuartil)**: Percentil 25
    
- **Q2 (segundo cuartil o mediana)**: Percentil 50
    
- **Q3 (tercer cuartil)**: Percentil 75
    
- En Pandas:
    
    - Primer cuartil: `df['columna'].quantile(0.25)`
    - Mediana: `df['columna'].quantile(0.50)`
    - Tercer cuartil: `df['columna'].quantile(0.75)`