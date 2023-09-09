**Métodos de Arrays en Pilas:**

1. `push(item)`: Agrega un elemento al final del array, simulando la operación de agregar a la cima de la pila.
2. `pop()`: Elimina y devuelve el último elemento del array, simulando la operación de quitar de la cima de la pila.
3. `length`: Proporciona la cantidad de elementos en el array, que equivale al tamaño de la pila.

```js
class Stack {
  constructor() {
    this.items = []; // Usamos un array para almacenar los elementos de la pila
  }

  push(item) {
    this.items.push(item); // Agregar un elemento al final del array
  }

  pop() {
    if (!this.isEmpty()) {
      return this.items.pop(); // Eliminar y devolver el último elemento del array
    }
  }

  peek() {
    if (!this.isEmpty()) {
      return this.items[this.items.length - 1]; // Obtener el último elemento sin eliminarlo
    }
  }

  isEmpty() {
    return this.items.length === 0; // Verificar si la pila está vacía
  }

  size() {
    return this.items.length; // Obtener el número de elementos en la pila
  }
}

// Ejemplo de uso
const stack = new Stack();

stack.push(10);
stack.push(20);
stack.push(30);

console.log("Elemento en la cima:", stack.peek()); // Debería imprimir 30

stack.pop();
console.log("Elemento en la cima después de pop:", stack.peek()); // Debería imprimir 20

console.log("¿La pila está vacía?", stack.isEmpty()); // Debería imprimir false
console.log("Tamaño de la pila:", stack.size()); // Debería imprimir 2

```