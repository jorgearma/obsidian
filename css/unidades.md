## unidades relativas
1. `%` (porcentaje): La unidad de porcentaje permite establecer valores relativos en relación con el elemento padre. Por ejemplo, si estableces `width: 50%;` en un elemento, este ocupará el 50% del ancho de su elemento padre.
.
2. `em`: La unidad `em` se basa en el tamaño de la fuente del elemento. Un valor de `1em` es igual al tamaño de fuente actual. Por ejemplo, si el tamaño de fuente es 16 píxeles en el elemento padre y estableces `font-size: 1.5em;` en un elemento hijo, su tamaño de fuente será de 24 píxeles (1.5 veces el tamaño de fuente padre).
 .   
3. `rem`: La unidad `rem` (root em) es similar a `em`, pero se basa en el tamaño de fuente del elemento raíz (normalmente el elemento `html`). A diferencia de `em`, `rem` no se ve afectado por el tamaño de fuente de los elementos padre. Esto lo hace útil para crear diseños más consistentes y predecibles.
 .   
4. `vw` (viewport width): La unidad `vw` representa el 1% del ancho del viewport (la ventana visible del navegador). Por ejemplo, `width: 50vw;` establecerá el ancho de un elemento al 50% del ancho de la ventana del navegador.
 .   
5. `vh` (viewport height): La unidad `vh` representa el 1% de la altura del viewport. Por ejemplo, `height: 75vh;` establecerá la altura de un elemento al 75% de la altura de la ventana del navegador.


## ubidades absolutas


1. `px` (píxeles): Es la unidad de medida más común y se utiliza para definir un tamaño fijo en píxeles. Por ejemplo, `width: 200px;` establece el ancho de un elemento en 200 píxeles.
   . 
2. `pt` (puntos): Es una unidad de medida que se utiliza principalmente para especificar el tamaño de fuente impreso. Un punto es igual a 1/72 de una pulgada. Por ejemplo, `font-size: 12pt;` establece el tamaño de fuente en 12 puntos.
   . 
3. `in` (pulgadas): Se utiliza para especificar tamaños en pulgadas. Por ejemplo, `width: 2in;` establece el ancho de un elemento en 2 pulgadas.
    .
4. `cm` (centímetros): Se utiliza para especificar tamaños en centímetros. Por ejemplo, `height: 5cm;` establece la altura de un elemento en 5 centímetros.
    .
5. `mm` (milímetros): Se utiliza para especificar tamaños en milímetros. Por ejemplo, `border-width: 2mm;` establece el ancho del borde en 2 milímetros.