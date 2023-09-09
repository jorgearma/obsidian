La sintáxis de css es la siguiente:

Para cambiar el atributo de alguna parte de HTML se escriben las carácteristicas dentro de los corchetes:
```css
	h1 {
		font-size: 32px; 
		font-family: Palatino, 'Palatino Linotype', serif; 
		color: rgb(46,105,163);
	}
```

Para seleccionar un elemento global
```css
	h1 {
	}
	
	body {
	}
	
	p {
	}
```

Para seleccionar una clase
```css
	.hero{
	}
	
	.main{
	}
```

Para seleccionar una id
```css
	#hero{
	}
	
	#main{
	}
```

### Fuente
Se usa una principal y otras de respaldo en caso de que el navegador del usuario no soporte la fuente principal
```css
	font-family: Palatino, 'Palatino Linotype', serif;
```
	
### Color
Se pueden utilizar alguno de los 3 tipos
```css
	color: rgb(46,105,163); ó color: red; ó #RRGGBB
```
	
### Tamaño
Se puede usar px(pixel), rem(tamaño default aprox=16px) y em(relativo al comando padre)
```css
	h1 {
		font-size: 60px; 
	}
```

### Fondo
Para añadir una imagen de fondo desde un link, y si está muy acercada usar la propiedad cover
```css
	.hero {
		background-image: url("https://s3.amazonaws.com/codecademy-content/projects/make-a-website/lesson-2/bg.jpg") ;
		background-size: cover;
	}
```

