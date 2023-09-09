![ima](imagenes/webp.jpg)

border-box hace que la caja mida la suma de todo 

- `width`: Define el ancho del elemento.
    
- `max-width`: Define el ancho máximo del elemento.
    
- `min-width`: Define un ancho mínimo del elemento.
    
- `height`: Define la altura del elemento.
    
- `max-height`: Define la altura máxima del elemento. 
    
- `min-height`: Define la altura mínima del elemento. 

- `overflow:hidden;`: Establece la propiedad de desbordamiento (overflow) en "hidden", lo cual oculta el contenido que se desborda del elemento.

## Valores especiales:

- `auto`: Se utiliza para centrar automáticamente el contenido dentro del elemento. Puede ser útil cuando el elemento tiene un ancho definido y `margin` establecido como `auto`.
- `inherit`: El valor `inherit` hereda el valor de relleno del elemento padre.

## border

1. Dotted: La línea del borde se mostrará por medio de puntos.
2. Dashed: La línea del borde se mostrará por medio de guiones.
3. Solid: La línea del borde será sólida sin ninguna alteración.
4. Double: Habrá dos líneas sólidas como borde.
5. Groove: Define un borde ranurado en 3D.
6. Ridge: Define un borde estriado en 3D.

```css
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

h1{
    background-color: seagreen;
    color: white;

    width: 200px;
    height: 200px;
    padding: 20px;
    border: 10px solid black;

  
} /* o width, height border*/
.padding{
    /* Usando 4 valores, el orden es en las manecillas del reloj */
    padding: top right bottom left;

    /* Usando 3 valores, el primer valor se aplica a arriba, 
    el segundo se aplica a la izquierda y derecha y el tercero se aplica a abajo */
    padding: top right-left bottom;

    /* Usando 2 valores,el primer valor se aplica a arriba-abajo, y el segundo se aplica
    a izquierda-derecha */
    padding: top-bottom right-left;

    /* Usando 1 valor, el valor se aplica a todos los lados de igual manera */
    padding: top-rigth-bottom-left;
```

