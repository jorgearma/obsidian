
```css
/* Es un comentario, y no se visualiza en CSS */

/* Selector de tipo */

body{

    font-family: Arial;

}


h2{
    color: seagreen;
    font-style: italic;
}


/* Selector de clase */
.subtitle{
    text-align: center;
    background-color: teal;
    color: white;
}

/* Selector de ID */
#title{
    background-color: #e3104f;
    color: white;
    padding: 20px 10px;
    font-family: cursive;
}

/* selectores combinadores */

/* Combinador de descendientes */

.section h2{
    background-color: crimson;
}

ul li{
    font-size: 20px;
    list-style: square;
}

/* Combinador de hijos directos */

.section > ul{
    background-color: black;
    color: white;
    padding: 20px 40px;
}
```