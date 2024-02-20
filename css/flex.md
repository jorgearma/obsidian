```css
/* Flexbox en CSS */

/* Flexbox, o Flexible Box Layout, es una forma de organizar elementos en tu página HTML de manera que se adapten al espacio disponible de forma flexible y eficiente. */

/* Contenedor Flex */

/* Primero, necesitas definir un contenedor flex: */

.contenedor {
    display: flex; /* Aplica el diseño flex a todos los hijos directos del contenedor */
}

/* Ahora puedes comenzar a usar muchas de las propiedades únicas de Flexbox en el contenedor y en los items flex. */

.contenedor {
    display: flex;
    flex-direction: row; /* 'flex-direction' define la dirección en la que se apilan los items flex. Puede ser 'row' (fila), 'row-reverse', 'column' (columna), o 'column-reverse'. */
    justify-content: center; /* 'justify-content' define cómo se distribuyen los items flex a lo largo de la línea principal. Puede ser 'flex-start', 'flex-end', 'center', 'space-between', 'space-around' o 'space-evenly'. */
    align-items: center; /* 'align-items' define cómo se distribuyen los items flex a lo largo de la línea cruzada. Puede ser 'flex-start', 'flex-end', 'center', 'baseline', o 'stretch'. */
}

/* Items Flex */

/* Los items flex también tienen sus propiedades: */

.item {
    flex-grow: 1;  /* 'flex-grow' define el factor de crecimiento de un item flex. Es un número que define cuánto espacio debe tomar el elemento en relación con sus hermanos. */
    flex-shrink: 2;  /* 'flex-shrink' define el factor de contracción de un item flex. Es un número que define cómo debe reducirse el tamaño del elemento cuando hay poco espacio disponible. */
    flex-basis: 200px;  /* 'flex-basis' define el tamaño base de un item flex antes de que se distribuya el espacio restante. */
    order: 2;  /* 'order' define el orden de los items flex dentro del contenedor. */
}

/* También puedes usar la propiedad 'flex' que es un atajo para establecer 'flex-grow', 'flex-shrink' y 'flex-basis' al mismo tiempo. */

.item {
    flex: 1 0 auto; /* grow: 1, shrink: 0, basis: auto */
}
/* Más propiedades de Flexbox */

.contenedor {
    /* 'flex-wrap' define si los items flex deben envolverse o no. Los valores pueden ser 'nowrap' (sin envolver), 'wrap' (envolver), y 'wrap-reverse' (envolver al revés). */
    flex-wrap: nowrap; /* Los elementos no se envuelven, pueden quedar fuera del contenedor si no caben */

    /* 'flex-flow' es una propiedad compuesta que define 'flex-direction' y 'flex-wrap' al mismo tiempo. */
    flex-flow: row wrap; /* Los elementos se colocan en filas y se envuelven cuando no hay suficiente espacio */
    
    /* 'align-content' define cómo se alinean las líneas flex cuando hay espacio extra en el eje transversal. */
    align-content: flex-start; /* Las líneas se apilan hacia el inicio del contenedor. Los valores pueden ser: 'flex-start', 'flex-end', 'center', 'space-between', 'space-around' y 'stretch' */
}

.item {
    /* 'align-self' permite anular el comportamiento de 'align-items' para un item flex específico. */
    align-self: flex-end; /* Este item se alinea al final del contenedor, sin importar lo que esté definido en 'align-items' en el contenedor. Los valores pueden ser: 'auto', 'flex-start', 'flex-end', 'center', 'baseline' y 'stretch' */

    /* 'flex' es una propiedad compuesta que define 'flex-grow', 'flex-shrink' y 'flex-basis' al mismo tiempo. */
    flex: 1 0 auto; /* grow: 1, shrink: 0, basis: auto */
}

```

