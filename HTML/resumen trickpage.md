# HTML

HTML es un lenguaje de marcado que se utiliza para el desarrollo de páginas de Internet. Se trata de la sigla que corresponde a HyperText Markup Language, es decir, Lenguaje de Marcas de Hipertexto, que podría ser traducido como Lenguaje de Formato de Documentos para Hipertexto.

Estructura de un archivo html:

```html
	<!DOCTYPE html>
	<html>
		<head>

		</head>

		<body>

		</body>
	</html>
```

Para iniciar un archivo HTML antes de head:
```html
	<!DOCTYPE html>
```
Abre el código
```html
	<html>
```
Cierra el código
```html
	</html>
```

Elemento script para que corra Javascript y JQuery: 
```html
	<script> </script>
```

### Agregar link 
```html
	<a href="ejemplo.com">list</a>
```

### Imagen
```html
	<img src="https://ejemplo.com/ejemplo.png">
```

### Video
```html
	<video width="400" height="240" src="https://s3.amazonaws.com/codecademy-content/projects/make-a-website/lesson-1/ollie.mp4" type="video/mp4">
  </video>
```

### Títulos y subtitulos (desde h1 hasta h6, siendo h1 el mas grande y h6 el mas pequeño)
```html
	<h1> Ollie Bike Sharing </h1> 
	<h3> Share your Pedals With the World </h3>
```

### Párrafos
```html
	<p>
  	Need a set of wheels while you're in town? Use ollie to pair your perfect vacation with a stylish, affordable bike rental.
	</p>
```

### Listas sin ordenar
```html
	<ul>
  	<li>First item</li> 
		<li>Second item</li>
	</ul>
```

### Divisiones
```html
	<div class="container">
  	<div class="nav">  
  		<h2>Ollie</h2>
	  	<ul>
			 	<li>Sign Up</li>
    		<li>Search Bikes</li>
			   <li>Reserve a Bike</li>
			 	<li>About Us</li>
  		</ul>
  	</div>
	</div>
```

A cualquier elemento se le puede añadir una clase o una id. La clase puede ser reutilizada en otros elementos del documento. Una id es única, no puede usarse en otros elementos del mismo documento. 
Por ejemplo:
```html
	<div class="clase" ></div>
	<div id="unica-division"></div>
```
#### Nota: Se pueden añadir varias clases al mismo elemento, separándolos con un espacio.


