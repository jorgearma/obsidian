## Estructura básica grid:

Para crear una grilla, primero debes designar un contenedor como una grilla usando la propiedad `display: grid;`
```css
.contenedor {
  display: grid;
}

```

**Definir las columnas y filas:**

```css
.contenedor {
  display: grid;
  grid-template-columns: 200px 200px 200px;
  grid-template-rows: 100px 100px;
}
/*crea un contenedor con una cuadrícula que tiene tres columnas de 200 píxeles de ancho y dos filas de 100 píxeles de altura.*/

```

**Posicionamiento de los elementos en grid**

```css
.item1 {
  grid-column: 1 / 2;
  grid-row: 1 / 2;
}

.item2 {
  grid-column: 2 / 3;
  grid-row: 1 / 2;
}

.item3 {
  grid-column: 3 / 4;
  grid-row: 1 / 2;
}
/* Span */
.item4{
	grid-column: span 3;
	grid-row: 3 / span 2;
}

```
En este ejemplo, el primer elemento de la grilla (`.item1`) se posiciona en la primera columna y la primera fila. El segundo elemento de la grilla (`.item2`) se posiciona en la segunda columna y la primera fila, y así sucesivamente.

**Fracciones (fr):**

las  puedo mesclar con px  para darle un tamano deseado
```css
.contenedor {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr;
}

```

```css
.contenedor {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  grid-gap: 10px;
}

```
En este ejemplo, hay un espacio de 10px entre las columnas y filas.

