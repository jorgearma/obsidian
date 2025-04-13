## 🔹 Métodos útiles

```python
lista = [3, 1, 4]

lista.append(5)        # Agrega al final → [3, 1, 4, 5]
lista.insert(1, 10)    # Inserta en índice 1 → [3, 10, 1, 4, 5]
lista.remove(4)        # Elimina el valor 4 → [3, 10, 1, 5]
lista.pop()            # Elimina el último → [3, 10, 1]
lista.sort()           # Ordena → [1, 3, 10]
lista.reverse()        # Invierte → [10, 3, 1]
```

---
## 🟢 ¿Qué es una lista en Python?

Una lista es una colección **ordenada y modificable** de elementos. Puede contener cualquier tipo de datos: números, strings, booleanos, otras listas, objetos, etc.

# 📝 Python List Cheat Sheet

## 🔹 Crear listas

```python
vacia = []                        # Lista vacía
numeros = [1, 2, 3, 4, 5]         # Lista de enteros
nombres = ["Ana", "Luis", "Sara"]# Lista de strings
mezcla = [42, "texto", False]     # Lista con tipos mezclados
```

---

## 🔹 Acceder a elementos

```python
nombres[0]     # Primer elemento → "Ana"
nombres[-1]    # Último elemento → "Sara"
```

---

## 🔹 Modificar elementos

```python
nombres[1] = "Carlos"   # Cambia "Luis" por "Carlos"
```

---




## 🔹 Recorrer listas
nombres
```python
for nombre in nombres:
    print(nombre)

# Con índices:
for i in range(len(nombres)):
    print(nombres[i])
```

---

## 🔹 Funciones útiles

```python
len(lista)       # Largo de la lista
sum(lista)       # Suma total (números)
max(lista)       # Mayor valor
min(lista)       # Menor valor
```

---


# 📚 Métodos más comunes de listas en Python

---

## ➕ Agregar elementos

### `.append(x)`
Agrega un elemento al final de la lista.
```python
lista = [1, 2, 3]
lista.append(4)  # [1, 2, 3, 4]
```

### `.insert(i, x)`
Inserta un elemento `x` en la posición `i`.
```python
lista = [1, 2, 3]
lista.insert(1, 99)  # [1, 99, 2, 3]
```

### `.extend(iterable)`
Agrega todos los elementos de un iterable (otra lista, etc.) al final.
```python
lista = [1, 2]
lista.extend([3, 4])  # [1, 2, 3, 4]
```

---

## ➖ Eliminar elementos

### `.remove(x)`
Elimina la primera aparición de `x`.
```python
lista = [1, 2, 3, 2]
lista.remove(2)  # [1, 3, 2]
```

### `.pop([i])`
Elimina y devuelve el elemento en la posición `i`. Si no se da índice, quita el último.
```python
lista = [1, 2, 3]
lista.pop()     # Devuelve 3, lista queda [1, 2]
lista.pop(0)    # Devuelve 1, lista queda [2]
```

### `.clear()`
Elimina todos los elementos de la lista.
```python
lista = [1, 2, 3]
lista.clear()  # []
```

---

## 🔄 Ordenar y modificar

### `.sort()`
Ordena la lista **en lugar**.
```python
lista = [3, 1, 2]
lista.sort()  # [1, 2, 3]
```

### `.sort(reverse=True)`
Ordena de mayor a menor.
```python
lista = [3, 1, 2]
lista.sort(reverse=True)  # [3, 2, 1]
```

### `.reverse()`
Invierte el orden de la lista **en lugar**.
```python
lista = [1, 2, 3]
lista.reverse()  # [3, 2, 1]
```

---

## 🔍 Buscar y contar

### `.index(x)`
Devuelve el índice de la primera aparición de `x`.
```python
lista = ['a', 'b', 'c']
lista.index('b')  # 1
```

### `.count(x)`
Cuenta cuántas veces aparece `x`.
```python
lista = [1, 2, 2, 3]
lista.count(2)  # 2
```

---

## 🧬 Copiar listas

### `.copy()`
Devuelve una copia superficial de la lista.
```python
lista = [1, 2, 3]
copia = lista.copy()  # copia = [1, 2, 3]
```

---

## 🧠 Otras formas útiles

### Concatenar listas
```python
a = [1, 2]
b = [3, 4]
c = a + b  # [1, 2, 3, 4]
```

### Repetir lista
```python
a = [0]
b = a * 3  # [0, 0, 0]
```

### Comprobación de existencia
```python
3 in [1, 2, 3]  # True
```