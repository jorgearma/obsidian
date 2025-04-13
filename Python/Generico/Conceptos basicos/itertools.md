```PYTHON

product(a, b)                 # Todas las combinaciones 
permutations(iterable, r)     # Ordenaciones sin repetición
combinations(iterable, r)     # Subconjuntos sin orden
combinations_with_replacement(iterable, r) # Sub con repetición
accumulate(iterable)           # Suma acumulativa progresiva
accumulate(iterable, func)     # Acumulación con función
groupby(iterable)              # Agrupa consecutivos iguales
```
# 🧰 tertools

Los módulos `itertools` en Python contienen funciones súper poderosas para trabajar con iteradores. Son esenciales  porque permiten resolver problemas de combinatoria, lógica, búsqueda y generación de datos de forma elegante y eficiente.

---

## ✅ 1. `itertools.product()`

### Qué hace:
Devuelve el **producto cartesiano** de los elementos. Es como hacer todos los pares posibles.

```python
from itertools import product

a = [1, 2]
b = [3, 4]
print(list(product(a, b)))
# [(1, 3), (1, 4), (2, 3), (2, 4)]
```

---

## ✅ 2. `itertools.permutations()`

### Qué hace:
Devuelve **todas las permutaciones posibles** (orden importa).

```python
from itertools import permutations

print(list(permutations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

---

## ✅ 3. `itertools.combinations()`

### Qué hace:
Devuelve todas las **combinaciones únicas** de longitud `r` (orden NO importa).

```python
from itertools import combinations

print(list(combinations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
```

---

## ✅ 4. `itertools.combinations_with_replacement()`

### Qué hace:
Como `combinations()`, pero permite **repeticiones**.

```python
from itertools import combinations_with_replacement

print(list(combinations_with_replacement('AB', 2)))
# [('A', 'A'), ('A', 'B'), ('B', 'B')]
```

---

## ✅ 5. `itertools.accumulate()`

### Qué hace:
Devuelve acumulaciones (por defecto, suma progresiva).

```python
from itertools import accumulate

import operator
print(list(accumulate([1, 2, 3, 4])))
# [1, 3, 6, 10]
print(list(accumulate([1, 2, 3, 4], operator.mul)))
# [1, 2, 6, 24]
```

---

## ✅ 6. `itertools.groupby()`

### Qué hace:
Agrupa elementos consecutivos iguales.

```python
from itertools import groupby

data = 'aaabbccaaa'
agrupado = [(k, list(g)) for k, g in groupby(data)]
print(agrupado)
# [('a', ['a', 'a', 'a']), ('b', ['b', 'b']), ('c', ['c', 'c']), ('a', ['a', 'a', 'a'])]
```

---

## 🧠 Consejos para entrevistas:
- Siempre que veas un problema de **combinatoria**, piensa en `itertools`.
- Aprende a identificar si el problema requiere:
  - Todas las combinaciones → `combinations`
  - Todas las permutaciones → `permutations`
  - Todas las posibles parejas ordenadas → `product`
- Usa `list(...)` para forzar la evaluación del iterador y ver los resultados en pruebas.

---

## 🎓 ¿Por qué usar itertools?
- Son **más rápidos** y eficientes que escribir bucles anidados.
- Son parte de la **librería estándar** de Python.
