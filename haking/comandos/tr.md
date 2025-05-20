# 🌀 Comando `tr 'A-Za-z' 'N-ZA-Mn-za-m'` — ROT13

Este comando realiza una **rotación de 13 posiciones** (ROT13) sobre el alfabeto, tanto en mayúsculas como en minúsculas.

---

## 🔧 ¿Qué es `tr`?

`tr` es una herramienta de terminal en Unix/Linux que **traduce o elimina** caracteres de la entrada estándar.  
**Sintaxis:** `tr [origen] [destino]`

---

## 📥 Primer argumento: `'A-Za-z'`

Este define los **caracteres de entrada** que serán reemplazados:

- `A-Z`: Letras mayúsculas del alfabeto (`ABCDEFGHIJKLMNOPQRSTUVWXYZ`)
- `a-z`: Letras minúsculas del alfabeto (`abcdefghijklmnopqrstuvwxyz`)

---

## 📤 Segundo argumento: `'N-ZA-Mn-za-m'`

Este define los **caracteres de destino** para la sustitución, rotando el alfabeto 13 posiciones:

### 🔸 `N-Z` → Para `A-M`
- Mayúsculas desde `N` hasta `Z`: `N O P Q R S T U V W X Y Z`

### 🔸 `A-M` → Para `N-Z`
- Mayúsculas desde `A` hasta `M`: `A B C D E F G H I J K L M`

🧠 Resultado para mayúsculas: `A-Z` → `N-ZA-M`

---

### 🔸 `n-z` → Para `a-m`
- Minúsculas desde `n` hasta `z`: `n o p q r s t u v w x y z`

### 🔸 `a-m` → Para `n-z`
- Minúsculas desde `a` hasta `m`: `a b c d e f g h i j k l m`

🧠 Resultado para minúsculas: `a-z` → `n-za-m`

---

## 🔁 Ejemplo

```bash
echo "Hello World" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

**Resultado:**
```
Uryyb Jbeyq
```

### Traducción de letras:
| Letra original | Letra rotada |
|----------------|--------------|
| H              | U            |
| e              | r            |
| l              | y            |
| o              | b            |
| W              | J            |
| d              | q            |

---

## ✅ Resumen

| Entrada  | Salida  |
|----------|---------|
| A-Z      | N-ZA-M  |
| a-z      | n-za-m  |

Este comando es útil para aplicar **ROT13**, una forma sencilla de ofuscar texto.  
⚠️ **No es seguro criptográficamente**, solo es una técnica de sustitución básica.
