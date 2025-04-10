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

## 🔹 Listas dentro de listas (matrices)

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matriz[1][2])    # → 6
```

---

## 🔹 Eliminar duplicados

```python
sin_duplicados = list(set([1, 2, 2, 3, 4, 4]))  # → [1, 2, 3, 4]
```