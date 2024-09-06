### Conceptos Clave:

#### 3. **Series de Pandas**

Una **Serie** es una estructura unidimensional que puede almacenar cualquier tipo de datos (números, cadenas, etc.). Piensa en ella como una columna de datos.

```python
import pandas as pd

# Crear una Serie
s = pd.Series([10, 20, 30, 40, 50])
print(s)

```
#### **DataFrames**

El **DataFrame** es la estructura de datos más importante de Pandas. Es una tabla de dos dimensiones con filas y columnas, como una hoja de cálculo o una tabla de base de datos.

```python
# Crear un DataFrame desde un diccionari
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Maria'],
    'Edad': [28, 24, 35, 42],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Bilbao']
}
df = pd.DataFrame(data)
print(df)
```

#### **Lectura de Archivos**

Pandas permite leer archivos CSV, Excel y otros formatos comunes. Aquí te muestro cómo leer un archivo CSV.
**Leer desde otros formatos**:

- Excel: `pd.read_excel()`
- SQL: `pd.read_sql()`
- JSON: `pd.read_json()`

```python
# Leer un archivo CSV
df = pd.read_csv('archivo.csv')
print(df.head())  # Muestra las primeras filas del archivo

# Seleccionar una columna
print(df['Nombre'])

# Filtrar filas donde la edad es mayor a 30
print(df[df['Edad'] > 30])



```

#### **Operaciones Básicas**

Algunas operaciones básicas incluyen la obtención de estadísticas descriptivas o el uso de funciones de agregación.

```python
# Estadísticas descriptivas
print(df.describe())

# Obtener la media de una columna
print(df['Edad'].mean())

```