## metodos strings
```PYTHON
# ==== Creación de strings ====
s = "hola mundo"

# ==== Información ====
len(s)                  # Longitud del string
s.isalpha()             # True si solo contiene letras
s.isdigit()             # True si solo contiene dígitos
s.isalnum()             # True si solo letras y números
s.isspace()             # True si solo espacios
s.islower()             # True si todo en minúsculas
s.isupper()             # True si todo en mayúsculas

# ==== Transformaciones ====
s.lower()               # "hola mundo"
s.upper()               # "HOLA MUNDO"
s.capitalize()          # "Hola mundo"
s.title()               # "Hola Mundo"
s.swapcase()            # Cambia mayúsculas por minúsculas y viceversa
s.strip()               # Elimina espacios en ambos extremos
s.lstrip()              # Elimina espacios a la izquierda
s.rstrip()              # Elimina espacios a la derecha
s.replace("hola", "hey")  # Reemplaza substrings

# ==== Búsqueda ====
s.find("mundo")         # Devuelve índice de la primera aparición o -1
s.index("mundo")        # Igual que find, pero lanza error si no encuentra
s.count("o")            # Número de veces que aparece "o"
s.startswith("hola")    # True si empieza con "hola"
s.endswith("mundo")     # True si termina con "mundo"

# ==== División y unión ====
s.split()               # ['hola', 'mundo'] → por defecto separa por espacios
s.split(",")            # Divide usando coma u otro separador
s.join(["hola", "mundo"])  # Une elementos: "hola mundo"

# ==== Formateo ====
"Hola {}".format("Lara")     # "Hola Lara"
f"Hola {nombre}"             # f-strings (más moderno y legible)
s.zfill(5)                   # Rellena con ceros a la izquierda: "00042"

# ==== Otros útiles ====
" ".isspace()           # True, si solo hay espacios
"abc123".isalnum()      # True, si solo letras y números

```



## 🔤 STRINGS 

### 📌 ¿Qué es un string?

Un string es una **secuencia inmutable** de caracteres. Se usa para representar texto.

```python
vacia = ""
nombre = "Lara"
saludo = 'Hola mundo'
frase = """Esto es
		un string
		multilínea"""

```

## Indexación y slicing

Cuando veas algo como `s[a:b:c]`, piensa así:

1. **Ubico los índices**: tanto positivos como negativos si es necesario.
2. **Elijo desde dónde empiezo (`a`)**
3. **Hasta dónde llego (`b`, pero sin incluirlo)**
4. **Cómo avanzo (`c`, paso positivo o negativo)**

```python
s = "Python"
print(s[0:3])   # Pyt
print(s[:2])    # Py
print(s[3:])    # hon
print(s[::-1])  # nohytP (reversa)

s = "Python"
print(s[0])  # P
print(s[-1]) # n

h = ""
h += "Hola"
h += " "
h += "mundo"
h += "!"
print(h)  # Resultado: Hola mundo!
```


# 🧵 Métodos más comunes de strings en Python

---

## 🔠 Conversión de mayúsculas y minúsculas

### `.lower()`
Convierte el string a minúsculas.
```python
"Hola Mundo".lower()  # 'hola mundo'
```

### `.upper()`
Convierte el string a mayúsculas.
```python
"Hola Mundo".upper()  # 'HOLA MUNDO'
```

### `.capitalize()`
Primera letra en mayúscula, el resto en minúsculas.
```python
"hOLA".capitalize()  # 'Hola'
```

### `.title()`
Primera letra de cada palabra en mayúscula.
```python
"hola mundo".title()  # 'Hola Mundo'
```

---

## 🧹 Espacios y relleno

### `.strip()`
Elimina espacios al principio y al final.
```python
"  hola  ".strip()  # 'hola'
```

### `.lstrip()`
Elimina espacios al inicio.
```python
"  hola  ".lstrip()  # 'hola  '
```

### `.rstrip()`
Elimina espacios al final.
```python
"  hola  ".rstrip()  # '  hola'
```

### `.zfill(n)`
Rellena el string con ceros a la izquierda hasta tener longitud `n`.
```python
"42".zfill(5)  # '00042'
```

---

## 🔁 Reemplazo y búsqueda

### `.replace(a, b)`
Reemplaza todas las apariciones de `a` por `b`.
```python
"banana".replace("a", "x")  # 'bxnxnx'
```

### `.find(sub)`
Devuelve el índice de la primera aparición de `sub`, o `-1` si no está.
```python
"hola".find("l")  # 2
```

### `.index(sub)`
Igual que `find()`, pero lanza error si no existe.
```python
"hola".index("l")  # 2
```

### `.count(sub)`
Cuenta cuántas veces aparece `sub`.
```python
"banana".count("a")  # 3
```

---

## 🧩 División y unión

### `.split(sep)`
Divide el string por el separador.
```python
"a,b,c".split(",")  # ['a', 'b', 'c']
```

### `.join(lista)`
Une una lista de strings con el separador.
```python
" ".join(['Hola', 'mundo'])  # 'Hola mundo'
```

---

## 🔎 Verificación de contenido

### `.startswith(sub)`
¿Empieza con `sub`?
```python
"python".startswith("py")  # True
```

### `.endswith(sub)`
¿Termina con `sub`?
```python
"python".endswith("on")  # True
```

### `.isalpha()`
¿Contiene solo letras?
```python
"abc".isalpha()  # True
```

### `.isdigit()`
¿Contiene solo dígitos?
```python
"123".isdigit()  # True
```

### `.isalnum()`
¿Contiene solo letras y/o números?
```python
"abc123".isalnum()  # True
```

### `.isspace()`
¿Contiene solo espacios?
```python
"   ".isspace()  # True
```

