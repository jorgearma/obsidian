## 🔤 STRINGS EN PYTHON (CADENAS DE TEXTO)

### 📌 ¿Qué es un string?

Un string es una **secuencia inmutable** de caracteres. Se usa para representar texto.

python

CopiarEditar

```python
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



```

## Métodos útiles de strings

```python
s = "  Hola Mundo  "

s.lower()         # '  hola mundo  '
s.upper()         # '  HOLA MUNDO  '
s.strip()         # 'Hola Mundo' (quita espacios extremos)
s.replace("o", "0")  # '  H0la Mund0  '
s.startswith("H")    # False (espacio al inicio)
s.strip().startswith("H")  # True
s.split()         # ['Hola', 'Mundo']
"::".join(["A", "B", "C"])  # 'A::B::C'
' '.join(s.split()[::-1])

```


```
```


```
```