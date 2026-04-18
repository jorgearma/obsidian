# ✅ Todo lo que necesito saber para ser Junior Medio Competente en Python

Ver mapa completo: [[Python/MOC-Python|MOC Python]]

## 🧠 1. Fundamentos del lenguaje
- [[Python/Generico/Conceptos basicos/Variables|Variables]] y tipos de datos: `int`, `float`, `str`, `bool`
- Conversión entre tipos: `str()`, `int()`, `float()`
- Operadores: aritméticos, lógicos, de comparación
- Condicionales: `if`, `elif`, `else`
- [[Python/Generico/Conceptos basicos/Bucle FOR|Bucles]]: `for`, `while`, `break`, `continue`
- List comprehensions: `[x for x in lista if ...]`
- [[Python/Generico/Conceptos basicos/Funciones|Funciones]]: `def`, argumentos, valores por defecto
- Alcance de variables: `global`, `local`
- Operador ternario: `a if cond else b`
- Funciones útiles: `enumerate()`, `zip()`, `range()`, `len()`

---

## 🗂️ 2. Estructuras de datos básicas
- [[Python/data structure/list|Listas]] (`list`): acceso, modificación, métodos (`append`, `remove`)
- [[Python/data structure/dict|Diccionarios]] (`dict`): claves, valores, `.get()`, `.items()`
- [[Python/data structure/set|Conjuntos]] (`set`): elementos únicos, operaciones de conjuntos
- [[Python/data structure/tuples|Tuplas]] (`tuple`): inmutables, desempaquetado
- [[Python/data structure/strings|Strings]]: métodos, slicing, formateo
- Verificación con `in`, estructuras anidadas

---

## 🧰 3. Manejo de errores
- Bloques `try`, `except`, `else`, `finally`
- Tipos comunes de errores: `ValueError`, `TypeError`, `KeyError`
- Uso de `Exception` genérico con precaución
- Buenas prácticas: capturar solo lo necesario

---

## 📁 4. Módulos y organización del código
- Importar módulos (`import`, `from`)
- Crear tus propios módulos y reutilizar código
- Uso de `if __name__ == "__main__"`
- [[Python/entorno virtual|`venv`]]: entornos virtuales para aislar dependencias
- Crear paquetes básicos con `__init__.py`

---

## 🧪 5. Testing básico
- [[Python/pruebas unitarias/teoria|Teoría de testing]]
- [[Python/pruebas unitarias/setUp|setUp]] — preparar el entorno de tests
- [[Python/pruebas unitarias/mocks|Mocks]] — simular dependencias externas
- [[Python/pruebas unitarias/patch|patch]] — parchear objetos en tests

---

## 📦 6. Librerías estándar útiles
- `os`, `pathlib` → [[Python/Gestión de Ficheros/With open()|archivos y directorios]]
- `datetime` → fechas y horas
- `json`, `csv` → manejo de datos estructurados
- `random`, `math` → utilidades matemáticas
- `requests` → consumir APIs externas

---

## 🌐 7. Flask y backend básico
- Crear rutas con `@app.route`
- Métodos HTTP: `GET`, `POST`
- Acceso a datos de entrada: `request.args`, `request.form`, `request.json`
- Envío de respuesta: `jsonify`, códigos HTTP (`200`, `404`, `500`)
- Estructura básica de un proyecto Flask
- Variables de entorno con `.env`

---

## 💾 8. Bases de datos con SQLAlchemy
- Definición de modelos
- Consultas: `query().filter_by().first()`
- Crear y guardar registros: `add()`, `commit()`, `rollback()`
- Manejo de errores con `SQLAlchemyError`
- Relaciones uno-a-muchos (opcional)
- [[bases de datos/sql/teoria sql|Teoría SQL]]
- [[bases de datos/sql/comandos sql|Comandos SQL]]

---

## 🧠 9. Buenas prácticas
- Nombres de variables y funciones claros
- Código limpio y DRY (Don't Repeat Yourself)
- Comentarios útiles y no obvios
- Separación de lógica en funciones
- Código legible y mantenible

---

## 📢 10. Bonus para destacar
- Validación de datos con `pydantic`
- Decoradores útiles: `@retry`, `@app.route`
- Uso básico de `Redis` para caché o bloqueo de usuarios
- `logging` en lugar de `print()`
- Uso básico de Git: `init`, `add`, `commit`, `push`, `pull` → [[git/fundamentos/instalacion|Git instalación]]

---

## 🧪 Proyectos recomendados para practicar
- [[panchi-bot/MOC-panchi-bot|Bot de WhatsApp para pedidos]] (¡ya lo tienes!)
- CRUD de tareas con Flask y SQLite
- API que devuelve frases, recetas o datos de Pokémon
- Registro de usuarios con validación y guardado en BBDD

---
