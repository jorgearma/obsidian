@media funiciona como una condicional
```css
/* Estilos generales que se aplican en cualquier tamaño de pantalla */
.elemento {
  width: 200px;
  height: 200px;
  background-color: blue;
}

/* Estilos específicos para pantallas con un ancho máximo de 600px */
@media (max-width: 600px) {
  .elemento {
    width: 150px;
    height: 150px;
    background-color: red;
  }
}

/* Estilos específicos para pantallas con un ancho mínimo de 1200px */
@media (min-width: 1200px) {
  .elemento {
    width: 250px;
    height: 250px;
    background-color: green;
  }
}


```