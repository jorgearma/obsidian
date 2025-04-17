
| Método de lista | ¿Funciona con tuplas adentro? | Ejemplo                          |
| --------------- | ----------------------------- | -------------------------------- |
| `append()`      | ✅ Sí                          | `lista.append((nuevo, dato))`    |
| `remove()`      | ✅ Sí                          | `lista.remove(("Ana", 25))`      |
| `sort()`        | ✅ Sí                          | `lista.sort(key=lambda x: x[1])` |
| `reverse()`     | ✅ Sí                          | `lista.reverse()`                |
| `count()`       | ✅ Sí                          | `lista.count((1, 2))`            |
# 🧠 Todo lo que necesitas saber sobre Tuplas en Python

## ✅ ¿Qué es una tupla?
Una **tupla** es una estructura de datos en Python que permite almacenar múltiples elementos. Es **inmutable**, lo que significa que no se puede modificar una vez creada.

```python
mi_tupla = (1, 2, 3)
```

---

## ✅ ¿Cómo se crea una tupla?
```python
vacia = ()
una_sola = (1,)  # Importante: la coma es necesaria
mixta = ("texto", 3.14, True)
```

---

## ✅ Acceder a elementos
```python
t = (10, 20, 30)
print(t[0])  # 10
```

---

## ✅ Tuplas dentro de listas y listas de tuplas
```python
lista_de_tuplas = [(1, 2), (3, 4), (5, 6)]
for x, y in lista_de_tuplas:
    print(x + y)
```

---

## ✅ Usos comunes de tuplas

- Como **clave en un diccionario**
- Para **retornar múltiples valores** de una función
- Para representar **datos agrupados** como coordenadas, combinaciones, etc.

---

## ✅ Ordenar una lista de tuplas
```python
datos = [("Ana", 25), ("Luis", 30), ("Marta", 22)]
ordenado = sorted(datos, key=lambda x: x[1])
print(ordenado)
```

---

## ✅ Filtrar una lista de tuplas
```python
mayores = [persona for persona in datos if persona[1] > 25]
```

---

## ✅ Convertir tuplas a strings legibles
```python
for nombre, edad in datos:
    print(f"{nombre} tiene {edad} años")
```

---

## ✅ Trabajar con itertools (listas de tuplas)
```python
from itertools import product, combinations, permutations

a = [1, 2]
b = [3, 4]

print(list(product(a, b)))        # Producto cartesiano
print(list(combinations(a, 2)))   # Combinaciones
print(list(permutations(a, 2)))   # Permutaciones
```

---

## ✅ Desempaquetar tuplas
```python
a, b = (5, 10)
print(a + b)
```

---

## ✅ Inmutabilidad de las tuplas
```python
t = (1, 2, 3)
# t[0] = 5  # ❌ Error: las tuplas no se pueden modificar
```

---

## ✅ Conclusión

| Característica     | Lista        | Tupla         |
|--------------------|--------------|---------------|
| Mutable            | ✅ Sí         | ❌ No          |
| Velocidad          | Más lenta     | ✅ Más rápida  |
| Se puede usar como clave en diccionario | ❌ No | ✅ Sí |
| Sintaxis           | `[1, 2]`      | `(1, 2)`       |

---

📌 **Las tuplas son fundamentales** para representar pares de datos, trabajar con estructuras inmutables, resolver problemas con `itertools`, y más. Dominar su uso te dará una ventaja real en entrevistas y desarrollo real.