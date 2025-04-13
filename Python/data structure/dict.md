# Diccionarios en Python

## 🧱 1. ¿Qué es un diccionario?
Un diccionario (`dict`) es una estructura de datos en Python que almacena pares clave-valor.  
Es como un diccionario real: buscas una palabra (clave) y obtienes su definición (valor).

```python
persona = {
    "nombre": "Lara",
    "edad": 27,
    "profesion": "Desarrolladora"
}
```

## 🧩 2. Características clave
- Las claves deben ser únicas y **inmutables** (strings, números, tuplas…).
- Los valores pueden ser de **cualquier tipo** (string, lista, otro `dict`...).
- Son **mutables** (se pueden modificar).
- Son **desordenados** (antes de Python 3.7), aunque desde entonces **preservan el orden de inserción**.

## 🛠️ 3. Operaciones básicas

### Acceder a un valor
```python
print(persona["nombre"])  # Lara
```

### Modificar un valor
```python
persona["edad"] = 28
```

### Añadir un nuevo par
```python
persona["pais"] = "Dinamarca"
```

### Eliminar un par
```python
del persona["profesion"]
```

### Usar `.get()` para evitar errores si la clave no existe
```python
print(persona.get("altura", "No especificada"))  # Devuelve valor por defecto si no existe
```

## 🔁 4. Iterar sobre diccionarios

### Claves
```python
for clave in persona:
    print(clave)
```

### Claves y valores
```python
for clave, valor in persona.items():
    print(clave, valor)
```

## 📦 5. Métodos útiles
```python
persona.keys()      # Devuelve solo las claves
persona.values()    # Devuelve solo los valores
persona.items()     # Devuelve tuplas (clave, valor)
persona.pop("edad") # Elimina la clave y devuelve su valor
persona.clear()     # Vacía el diccionario
```

## 🧱 6. Diccionarios anidados
Puedes tener diccionarios dentro de diccionarios:

```python
usuarios = {
    "lara": {
        "edad": 27,
        "rol": "admin"
    },
    "jorge": {
        "edad": 32,
        "rol": "cliente"
    }
}
print(usuarios["lara"]["rol"])  # admin
```

## 🛠️ 7. Diccionario por comprensión (dict comprehension)
Parecido a las listas por comprensión, pero con pares clave:valor:

```python
cuadrados = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## 🧠 8. Cosas avanzadas e interesantes

### Usar tuplas como claves
```python
coords = {(0, 0): "origen", (1, 2): "destino"}
```

### Contar elementos fácilmente con `collections.Counter`
```python
from collections import Counter
frecuencias = Counter("abracadabra")
# {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
```

### Unir diccionarios con el operador `|` (desde Python 3.9)
```python
a = {"x": 1}
b = {"y": 2}
c = a | b  # {'x': 1, 'y': 2}
```

## ✅ En resumen
Los diccionarios son clave en Python para representar información estructurada, configurar parámetros, representar objetos, manejar datos en APIs, etc.  
**Te conviene dominarlos muy bien porque los vas a usar todo el rato.**