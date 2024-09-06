### Resumen

- **Bases de Datos**: Contienen y organizan múltiples tablas.
- **Tablas**: Estructuras dentro de las bases de datos que contienen datos organizados en filas y columnas.
- **Filas**: Representan un único registro en una tabla.
- **Columnas**: Representan un tipo específico de dato que puede almacenarse en una tabla.
- **Tipos de Datos**: Definen el tipo de información que puede almacenarse en cada columna.
- **Clave Primaria**: Un identificador único para cada registro en una tabla.
- **Clave Externa**: Un campo que crea una relación entre dos tablas.



### 1. **Bases de Datos**

Una **base de datos** es un conjunto organizado de datos que se almacenan y se gestionan de manera que se pueda acceder fácilmente a la información, consultarla, modificarla y eliminarla. La base de datos puede estar compuesta por varias **tablas**. Piensa en una base de datos como un archivo de Excel donde cada hoja representa una tabla diferente.

### 2. **Tablas**

Dentro de una base de datos, una **tabla** es como una hoja de cálculo que contiene datos organizados en filas y columnas. Cada tabla se enfoca en almacenar información sobre un tema o entidad específica. Por ejemplo, si tienes una base de datos para una escuela, podrías tener tablas como "Estudiantes", "Cursos", y "Profesores".

#### Estructura de una Tabla:

- **Filas** (Rows): También llamadas **registros**. Cada fila en una tabla representa un conjunto único de datos, o un **registro**. En el contexto de nuestra tabla "Estudiantes", cada fila podría representar a un estudiante específico.
    
- **Columnas** (Columns): También conocidas como **campos**. Las columnas definen el tipo de datos que se almacenan. Por ejemplo, en la tabla "Estudiantes", podrías tener columnas como "ID del estudiante", "Nombre", "Apellido", y "Fecha de nacimiento".
    

### 3. **Tipos de Datos**

Los **tipos de datos** definen el tipo de valor que puede almacenarse en una columna. Es importante definir correctamente los tipos de datos para asegurar que los datos se almacenen de manera eficiente y precisa. A continuación, algunos de los tipos de datos más comunes:

- **int** (Entero): Se utiliza para almacenar números enteros, tanto positivos como negativos. Ejemplo: 123, -50.
    
- **varchar** (Cadena de caracteres): Se utiliza para almacenar cadenas de texto de longitud variable. Por ejemplo, nombres, descripciones. Se debe especificar un límite de caracteres, por ejemplo, `varchar(255)` permite hasta 255 caracteres.
    
- **date** (Fecha): Este tipo de dato se utiliza para almacenar fechas. El formato suele ser `YYYY-MM-DD`. Ejemplo: `2024-09-04`.
    
- **boolean** (Booleano): Se utiliza para almacenar valores de verdadero o falso (1 o 0). Es útil para campos que representen estados binarios, como "activo" o "inactivo".
    

Otros tipos de datos comunes incluyen `decimal` (para números decimales), `datetime` (para almacenar fechas con horas), y `text` (para cadenas de texto de longitud mayor a la permitida por `varchar`).

### 4. **Claves Primarias y Claves Externas**

#### Clave Primaria (Primary Key)

- Una **clave primaria** es un campo (o combinación de campos) que se utiliza para identificar de manera única cada registro en una tabla. Este campo debe ser único para cada fila y no puede contener valores nulos. En la tabla "Estudiantes", el campo "ID del estudiante" podría ser la clave primaria, ya que cada estudiante tiene un ID único.
    
- Las características principales de una clave primaria son:
    
    - **Unicidad**: Cada valor en la columna de la clave primaria debe ser único.
    - **No Nulo**: Ningún valor en la columna de la clave primaria puede ser nulo.
    - **Inmutabilidad**: El valor de la clave primaria no debe cambiar una vez asignado.

#### Clave Externa (Foreign Key)

- Una **clave externa** es un campo (o combinación de campos) en una tabla que se utiliza para crear una relación con la clave primaria de otra tabla. La clave externa establece una conexión entre dos tablas, permitiendo que una tabla "hija" se refiera a los datos de una tabla "padre".
    
- Por ejemplo, si tienes una tabla "Inscripciones" que registra en qué cursos están inscritos los estudiantes, podrías tener una columna "ID del estudiante" en la tabla "Inscripciones" que actúa como una clave externa, apuntando a la clave primaria "ID del estudiante" en la tabla "Estudiantes".
    
- Las características principales de una clave externa son:
    
    - **Referencia**: El valor en la clave externa debe coincidir con un valor en la clave primaria de la tabla referenciada.
    - **Integridad referencial**: La base de datos puede hacer cumplir reglas para asegurar que la relación entre las tablas se mantenga consistente.

#### Relación entre Tablas

- La relación que se establece a través de claves externas puede ser de varios tipos:
    - **Uno a muchos (1
        
        )**: Una fila en la tabla A puede relacionarse con muchas filas en la tabla B, pero cada fila en la tabla B solo se relaciona con una fila en la tabla A. Ejemplo: Un curso tiene muchos estudiantes, pero cada estudiante se inscribe en un solo curso específico en la tabla "Inscripciones".
    - **Muchos a muchos (M
        
        )**: Una fila en la tabla A puede relacionarse con muchas filas en la tabla B, y viceversa. Esto usualmente se maneja creando una tabla intermedia. Ejemplo: Un estudiante puede inscribirse en muchos cursos, y cada curso puede tener muchos estudiantes. La tabla "Inscripciones" sería la tabla intermedia.