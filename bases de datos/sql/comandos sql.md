
```sql
Seleccionar consulta para una columna específica

SELECT column, another_column, … 
FROM mytable;

Consulta de selección para todas las columnas

SELECT * 
FROM mytable;

```

Para filtrar determinados resultados y evitar que se devuelvan, debemos utilizar una `WHERE`cláusula en la consulta.

```sql
SELECT column, another_column, … 
FROM mytable 
WHERE _condition_ 
		AND/OR _another_condition_ 
		AND/OR …;
```

Para ayudar con esto, SQL proporciona una manera de ordenar los resultados por una columna determinada en orden ascendente o descendente utilizando la `ORDER BY`cláusula .

```sql
SELECT column, another_column, … 
FROM mytable 
WHERE _condition(s)_ 
ORDER BY column ASC/DESC;


SELECT DISTINCT column, another_column, … 
FROM mytable 
WHERE _condition(s)_ 
ORDER BY column ASC/DESC 
LIMIT num_limit OFFSET num_offset;
```

DISTINCT = proporciona una forma conveniente de descartar filas que tienen un valor de columna duplicado

### INNER JOIN

```sql

--Consulta de selección con INNER JOIN en varias tablas

SELECT column, another_table_column, … 
FROM mytable 
	JOIN another_table 
	ON mytable.id = another_table.id
WHERE _condition(s)_ 
ORDER BY column, … ASC/DESC
LIMIT num_limit OFFSET num_offset;`
```

Al unir la tabla A con la tabla B, a `LEFT JOIN`simplemente incluye filas de A independientemente de si se encuentra una fila coincidente en B. Es `RIGHT JOIN`lo mismo, pero al revés, manteniendo las filas en B independientemente de si se encuentra una coincidencia en A. Por último, a `FULL JOIN`simplemente significa que se mantienen las filas de ambas tablas, independientemente de si existe una fila coincidente en la otra tabla.

```sql
Consulta de selección con uniones IZQUIERDA/DERECHA/COMPLETAS en varias tablas

SELECT column, another_column, … 
FROM mytable INNER/LEFT/RIGHT/FULL 
JOIN another_table 
	ON mytable.id = another_table.matching_id 
WHERE _condition(s)_ 
ORDER BY column, … ASC/DESC 
LIMIT num_limit OFFSET num_offset;`
```


A veces, tampoco es posible evitar `NULL`valores, como vimos en la última lección al realizar uniones externas entre dos tablas con datos asimétricos. En estos casos, puede probar una columna para ver si contiene `NULL`valores en una `WHERE` cláusula utilizando la restricción `IS NULL`o `IS NOT NULL`. 

```sql 
Select query with constraints on NULL values

`SELECT column, another_column, … 
FROM mytable 
WHERE column IS/IS NOT NULL 
	AND/OR _another_condition_ 
	AND/OR …;
```