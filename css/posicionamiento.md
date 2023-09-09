
1. Posicionamiento estático (`position: static;`): Es el valor predeterminado del posicionamiento. Los elementos con posicionamiento estático se colocan en el flujo normal del documento y no se ven afectados por las propiedades de posicionamiento como `top`, `bottom`, `left` y `right`.
    
2. Posicionamiento relativo (`position: relative;`): Los elementos con posicionamiento relativo se posicionan en relación con su posición normal en el flujo del documento. Puedes utilizar las propiedades `top`, `bottom`, `left` y `right` para desplazarlos en relación con su posición original.
    
3. Posicionamiento absoluto (`position: absolute;`): Los elementos con posicionamiento absoluto se posicionan con respecto al elemento padre más cercano que tenga un posicionamiento distinto de `static`. Si no hay un elemento padre posicionado, se posicionan con respecto al documento. Puedes utilizar las propiedades `top`, `bottom`, `left` y `right` para especificar la ubicación precisa del elemento.
    
4. Posicionamiento fijo (`position: fixed;`): Los elementos con posicionamiento fijo se posicionan en relación con la ventana del navegador. Mantienen su posición incluso al hacer scroll en la página. Puedes utilizar las propiedades `top`, `bottom`, `left` y `right` para establecer su ubicación en la ventana del navegador.
    
5. Posicionamiento pegajoso (`position: sticky;`): Los elementos con posicionamiento pegajoso se comportan como posicionamiento relativo hasta que alcanzan una posición específica en la página. Luego, se "adherirán" a esa posición y se comportarán como posicionamiento fijo. Puedes utilizar las propiedades `top`, `bottom`, `left` y `right` para determinar cuándo se vuelve "pegajoso".
[[box model]]


## z-index

```css
.elemento1 {
  z-index: 2; /* Este elemento se apilará por encima de otros elementos */
}

.elemento2 {
  z-index: 1; /* Este elemento se apilará debajo de otros elementos */
}

```