### Resumen

- **`int`** para números enteros, especialmente IDs.
- **`varchar(n)`** para cualquier tipo de texto o cadena de caracteres.
- **`datetime`** para almacenar fechas y horas completas.
- **`boolean`** para valores lógicos que solo pueden ser verdaderos o falsos.
### 1. **Tipos de Datos Numéricos**

- **`int`**: Almacena números enteros, como IDs o cantidades. Ejemplo: 123.
- **`smallint`**: Enteros con menor rango, útil para valores pequeños. Ejemplo: 1500.
- **`bigint`**: Enteros grandes, útil para identificadores en grandes volúmenes de datos. Ejemplo: 9223372036854775807.
- **`decimal(p, s)` o `numeric(p, s)`**: Almacena números decimales con precisión fija, ideal para datos financieros. Ejemplo: `DECIMAL(10, 2)` para valores como 12345.67.
- **`float`**: Números de punto flotante con precisión variable, usado en cálculos científicos. Ejemplo: 3.14159.

### 2. **Tipos de Datos de Cadena de Texto**

- **`char(n)`**: Cadena de longitud fija. Útil para códigos o valores de longitud constante. Ejemplo: `CHAR(2)` para códigos de país ("US").
- **`varchar(n)`**: Cadena de longitud variable. Ideal para textos donde la longitud varía, como nombres o descripciones. Ejemplo: `VARCHAR(100)`.
- **`text`**: Cadena de texto larga, para almacenar grandes bloques de texto. Ejemplo: descripciones o contenido de artículos.

### 3. **Tipos de Datos de Fecha y Hora**

- **`date`**: Solo almacena la fecha, sin hora. Ejemplo: `2024-09-04`.
- **`time`**: Solo almacena la hora, sin fecha. Ejemplo: `14:30:00`.
- **`datetime`**: Almacena tanto fecha como hora. Ejemplo: `2024-09-04 14:30:00`.
- **`timestamp`**: Similar a `datetime`, pero puede ser actualizado automáticamente cuando se inserta o modifica un registro.

### 4. **Tipo de Dato Booleano**

- **`boolean`**: Almacena valores `TRUE` o `FALSE`. Ideal para representar estados binarios, como "activo/inactivo".

### 5. **Otros Tipos de Datos**

- **`binary` y `varbinary`**: Almacenan datos binarios, como imágenes o archivos en formato binario. Ejemplo: `varbinary(8000)` para imágenes.
- **`enum`**: Define un conjunto de valores posibles para un campo, útil para campos con opciones limitadas. Ejemplo: `ENUM('pequeño', 'mediano', 'grande')`.