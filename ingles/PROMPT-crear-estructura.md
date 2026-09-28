# ENCARGO: Crear la ESTRUCTURA DE ARCHIVOS y la LÓGICA de un sistema de práctica de inglés

Tu tarea es montar el **esqueleto (archivos con su formato) y documentar la lógica completa** de un sistema de repetición espaciada para practicar inglés.

⚠️ NO generes contenido: nada de crear las 60 estructuras, ni frases, ni ejemplos reales. Los archivos van VACÍOS, solo con su formato/plantilla. Toda la riqueza va en la documentación de la lógica, no en datos rellenos.

## ARCHIVOS A CREAR

### 1. `estructuras.md` (vacío, solo plantilla del formato)
Deja únicamente la plantilla en blanco de cómo será CADA entrada, para rellenar después:
- Nombre de la estructura
- Significado en español
- Patrón gramatical
- Apartado **"en español se diría…"** (disparadores conceptuales que activan el chunk)
- 2-3 ejemplos (huecos)
- Errores comunes (huecos)

### 2. `progreso.md` (tabla vacía)
Tabla con columnas, sin filas de datos:
`Estructura | Veces vista | Bien | Mal | Estado | Próxima revisión`

### 3. `log.md` (vacío)
Cabecera + formato de una entrada:
`fecha → frase en español → respuesta del alumno → corrección por estructura`

### 4. `logica.md` (AQUÍ va todo el detalle del método)
Documenta cómo funciona el sistema, completo:

**Perfil y objetivo**
- Alumno B2+→C1. Fluidez social alta; gap real = expresar ideas complejas (política/abstracción) y ENCADENAR estructuras con naturalidad. Motivación: pareja que solo habla inglés + interés en política/actualidad/OSINT.
- Objetivo: interiorizar ~60 estructuras no literales vía producción activa + repetición espaciada.

**Mecánica del ejercicio (Structure Loop encadenado)**
- El coach lanza una frase en español REAL y natural, construida para OBLIGAR a encadenar varias estructuras objetivo.
- Frases ancladas a la vida del alumno (pareja, reparto, política).
- El alumno traduce encadenando. SIN pistas antes de intentarlo (dificultad deseable: el esfuerzo de recordar es lo que fija).
- Se aceptan varias traducciones válidas: se evalúa "¿usó bien y natural cada estructura?", no coincidencia exacta.

**Corrección POR ESTRUCTURA (no por frase entera)**
- El coach declara qué estructuras evalúa en cada frase y puntúa cada una: ❌ mal / ⚠️ regular / ✅ bien / 🌟 perfecto.
- Muestra: original del alumno → versión nativa → explicación corta. Inglés natural, no gramática académica.

**Principios de aprendizaje**
- Producción, no reconocimiento.
- Espaciar, no amontonar (repasos repartidos en días).
- Interleaving: mezclar tipos de estructura, no agruparlas.
- Variación de contexto: misma estructura en frases/temas distintos.
- Relevancia personal: frases sobre su vida real.

**Máquina de estados (repetición espaciada)**
- ⚪ nueva → sin practicar
- 🔴 fallando → falló; vuelve pronto (misma o siguiente sesión)
- 🟡 en progreso → algún acierto; intervalos crecientes
- ✅ interiorizada → producida bien y natural en varios repasos ESPACIADOS; intervalo largo o retirada
- Intervalos: 1 → 3 → 7 → 14 → ~30 días
- Acierto sube el intervalo; fallo resetea a corto (→🔴)
- Para pasar a ✅: varios aciertos espaciados (no seguidos el mismo día = empollar)
- Una ✅ que vuelve a fallar baja de estado (el sistema es sincero)

**Cómo se arma una ronda**
- Leer `progreso.md` → seleccionar: unas pocas nuevas + las que tocan repasar hoy (próxima revisión vencida) + de vez en cuando una ✅ de control.

**Estructura de una sesión (15-20 min)**
1. Leer `progreso.md` y armar la ronda.
2. Lanzar frases (multi-estructura) una a una.
3. Corregir por estructura tras cada respuesta.
4. Evaluación final breve (naturalidad, precisión, velocidad, progreso B2→C1) + actualizar `progreso.md` y `log.md`.

## RUTA
Crea los archivos en: `/home/siemprearmando/Desktop/obsidian/ingles/`
(cámbiala si prefieres otra carpeta)

## AL TERMINAR
Confirma qué archivos creaste y que están vacíos de contenido, solo con formato y lógica documentada.
