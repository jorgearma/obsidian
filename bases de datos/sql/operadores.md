

| Operator            | Condition                                            | SQL Example                     |
| ------------------- | ---------------------------------------------------- | ------------------------------- |
| =, !=, <, <=, >, >= | Standard numerical operators                         | `col_name != 4`                 |
| BETWEEN … AND …     | Number is within range of two values (inclusive)     | `col_name BETWEEN 1.5 AND 10.5` |
| NOT BETWEEN … AND … | Number is not within range of two values (inclusive) | `col_name NOT BETWEEN 1 AND 10` |
| IN (…)              | Number exists in a list                              | `col_name IN (2, 4, 6)`         |
| NOT IN (…)          | Number does not exist in a list                      | `col_name NOT IN (1, 3, 5)`     |
```sql
ejm
SELECT * FROM movies
where year BETWEEN 2000 and 2010

```

## operadores para texto 
Todas las cadenas deben estar entre comillas para que el analizador de consultas pueda distinguir las palabras de la cadena de las palabras clave de SQL.

| Operator   | Condition                                                                                                                    | Example                                                                     |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| =          | Comparación exacta de cadenas sensibles a mayúsculas y minúsculas (nótese el uso de un solo igual)                           | `col_name = "abc"`                                                          |
| != or <>   | Comparación exacta de desigualdad de cadenas sensibles a mayúsculas y minúsculas                                             | `col_name != "abcd"`                                                        |
| LIKE       | Comparación exacta de cadenas insensible a mayúsculas y minúsculas                                                           | `col_name LIKE "ABC"`                                                       |
| NOT LIKE   | Comparación de desigualdad de cadenas insensible a mayúsculas y minúsculas                                                   | `col_name NOT LIKE "ABCD"`                                                  |
| %          | Se usa en cualquier lugar de una cadena para coincidir con una secuencia de cero o más caracteres (solo con LIKE o NOT LIKE) | `col_name LIKE "%AT%"` (coincide con "AT", "ATTIC", "CAT" o incluso "BATS") |
| _          | Se usa en cualquier lugar de una cadena para coincidir con un solo carácter (solo con LIKE o NOT LIKE)                       | `col_name LIKE "AN_"` (coincide con "AND", pero no con "AN")                |
| IN (…)     | La cadena existe en una lista                                                                                                | `col_name IN ("A", "B", "C")`                                               |
| NOT IN (…) | La cadena no existe en una lista                                                                                             | `col_name NOT IN ("D", "E", "F")`                                           |

```sql
SELECT * 
FROM movies
WHERE title LIKE "%toy story%";
```