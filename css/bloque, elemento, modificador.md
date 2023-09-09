
```html
<div class="card card--highlighted">
  <h2 class="card__title">Título de la Tarjeta</h2>
  <img class="card__image" src="imagen.jpg" alt="Imagen de la Tarjeta">
  <div class="card__content">Contenido de la Tarjeta</div>
</div>

```
En este ejemplo, estamos utilizando la metodología BEM para crear un componente de tarjeta (card) destacado (highlighted). Aquí está el desglose:

- Bloque: `.card` es el bloque principal que representa la tarjeta en sí. Contiene todos los elementos y modificadores relacionados con la tarjeta.
    
- Elemento: `.card__title` es un elemento dentro del bloque de tarjeta que representa el título de la tarjeta. Es una parte individual de la tarjeta y se identifica con el doble guion bajo (`__`).
    
- Modificador: `.card--highlighted` es un modificador aplicado al bloque de tarjeta para resaltarlo visualmente. El modificador se identifica con el doble guion (`--`).
    

Esta estructura de nomenclatura clara y consistente del BEM ayuda a comprender rápidamente cómo se relacionan los diferentes elementos y modificadores dentro de un componente.

## active
```html
<button class="button button--active">Click me</button>

```
En este ejemplo, tenemos un bloque de botón (button) al que se le aplica un modificador "active" (active). Esto indica que el botón está en un estado activo. El selector de clase "button--active" se utiliza para aplicar estilos específicos al botón cuando está activo.