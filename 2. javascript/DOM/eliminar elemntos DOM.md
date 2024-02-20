removeChild():  se utiliza para eliminar un nodo hijo específico de su nodo padre. 

```js
var element = document.getElementById("miElemento");
var parent = element.parentNode;
parent.removeChild(element);

```

remove() :  permite eliminar directamente un elemento sin necesidad de acceder a su nodo padre. 

```js
var element = document.getElementById("miElemento");
element.remove();

```

innerHTML: Esta forma no elimina el elemento directamente, pero te permite eliminar todo el contenido HTML dentro del elemento.
```js
var element = document.getElementById("miElemento");
element.innerHTML = "";

```