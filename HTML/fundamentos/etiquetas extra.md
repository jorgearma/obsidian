con la etiqueta picture puedo elejir que mostrar dependiendo del
tamano de la pantalla
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Etiquetas extra</title>
    <style>
        img{
            width: 200px;
        }
    </style>
</head>
<body>

    <picture>
        <source srcset="./assets/naruto3.png" media="(min-width:900px)">
        <source srcset="./assets/naruto2.png" media="(min-width:500px)">

        <img src="./assets/naruto1.png" alt="">
    </picture>


    <!-- <figure>
        <img src="./assets/naruto1.png" alt="">
        <figcaption>Naturo Modo Base</figcaption>
    </figure>

    <figure>
        <img src="./assets/naruto2.png" alt="">
    </figure>
   
    <figure>
        <img src="./assets/naruto3.png" alt="">
    </figure> -->
    
    
    
</body>
</html>
```