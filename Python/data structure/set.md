
```PYTHON
# ==== Creación de sets ====
s = set([1, 2, 3])
s = set()  #set vacio


# ==== Añadir elementos ====
s.add(4)                # Añade un solo elemento
s.update([5, 6, 7])     # Añade múltiples elementos desde un iterable

# ==== Eliminar elementos ====
s.remove(2)             # Elimina un elemento (lanza error)
s.discard(10)           # Elimina un elemento (NO lanza erro)
s.pop()                 # Elimina y devuelve un elemento 
s.clear()               # Vacía el set

# ==== Operaciones entre sets ====
a = {1, 2, 3}
b = {3, 4, 5}

a.union(b)              # {1, 2, 3, 4, 5}
a | b                   # Igual que union

a.intersection(b)       # {3}
a & b                   # Igual que intersection

a.difference(b)         # {1, 2}
a - b                   # Igual que difference

a.symmetric_difference(b)  # {1, 2, 4, 5}
a ^ b                      # Igual que symmetric_difference

# ==== Comparación de sets ====
a.issubset(b)           # True si todos los elementos de a están en b
a.issuperset(b)         # True si a contiene todos los elementos de b
a.isdisjoint(b)         # True si no comparten ningún elemento

```
# 🧮 Métodos más comunes de sets en Python (`set()`)

---

Los sets en Python son **colecciones no ordenadas de elementos únicos**. Son muy útiles para eliminar duplicados y hacer operaciones de conjuntos (como unión, intersección, etc.).

---

## 🔧 Crear un set

```python
s = set([1, 2, 3, 2])  # {1, 2, 3}
```

O directamente:
```python
s = {1, 2, 3}
```

> ⚠️ No confundir `s = {}` con un set. Eso crea un diccionario vacío. Usa `set()` para un set vacío.

---

## ➕ Agregar elementos

### `.add(x)`
Agrega el elemento `x` al set.
```python
s = {1, 2}
s.add(3)  # {1, 2, 3}
```

### `.update(iterable)`
Agrega múltiples elementos desde otro iterable.
```python
s = {1}
s.update([2, 3], {4, 5})  # {1, 2, 3, 4, 5}
```

---

## ➖ Eliminar elementos

### `.remove(x)`
Elimina `x`. Da error si no existe.
```python
s = {1, 2, 3}
s.remove(2)  # {1, 3}
```

### `.discard(x)`
Elimina `x`. No da error si no existe.
```python
s = {1, 2, 3}
s.discard(4)  # {1, 2, 3}
```

### `.pop()`
Elimina y devuelve un elemento aleatorio.
```python
s = {1, 2, 3}
s.pop()  # -> 1 (por ejemplo), set cambia
```

### `.clear()`
Elimina todos los elementos.
```python
s = {1, 2, 3}
s.clear()  # set()
```

---

## 🔁 Operaciones de conjuntos

### Unión: `.union()` o `|`
Combina los elementos únicos de ambos sets.
```python
a = {1, 2}
b = {2, 3}
a.union(b)     # {1, 2, 3}
a | b          # {1, 2, 3}
```

### Intersección: `.intersection()` o `&`
Elementos comunes entre ambos sets.
```python
a = {1, 2}
b = {2, 3}
a & b          # {2}
```

### Diferencia: `.difference()` o `-`
Elementos en `a` que no están en `b`.
```python
a = {1, 2}
b = {2, 3}
a - b          # {1}
```

### Diferencia simétrica: `.symmetric_difference()` o `^`
Elementos que están en uno o en otro, pero no en ambos.
```python
a = {1, 2}
b = {2, 3}
a ^ b          # {1, 3}
```

---

## ❓ Comparaciones

### `.issubset(b)` o `a <= b`
¿Todos los elementos de `a` están en `b`?
```python
{1, 2}.issubset({1, 2, 3})  # True
```

### `.issuperset(b)` o `a >= b`
¿Todos los elementos de `b` están en `a`?
```python
{1, 2, 3}.issuperset({1, 2})  # True
```

### `.isdisjoint(b)`
¿No comparten ningún elemento?
```python
{1, 2}.isdisjoint({3, 4})  # True
```

---

## ✅ Utilidades

- Eliminar duplicados de una lista:
```python
lista = [1, 2, 2, 3]
unicos = list(set(lista))  # [1, 2, 3]
```

- Comprobar existencia:
```python
2 in {1, 2, 3}  # True
```