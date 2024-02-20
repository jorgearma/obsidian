**Métodos de Arrays en Colas:**

1. `push(item)`: Agrega un elemento al final del array, simulando la operación de agregar al final de la cola.
2. `shift()`: Elimina y devuelve el primer elemento del array, simulando la operación de quitar del frente de la cola.
3. `length`: Proporciona la cantidad de elementos en el array, que equivale al tamaño de la cola.

Es importante mencionar que mientras que los métodos `push`, `pop` y `length` son comunes para pilas y colas, el método `shift` se utiliza específicamente en colas porque elimina elementos del frente. En cambio, en las pilas, se utiliza el método `pop` para eliminar elementos de la cima.


```js
class Queue {
    constructor() {
        this.items = [];
    }
    
    enqueue(item) {
        this.items.push(item);
    }
    
    dequeue() {
        if (!this.isEmpty()) {
            return this.items.shift();
        }
    }
    
    peek() {
        if (!this.isEmpty()) {
            return this.items[0];
        }
    }
    
    isEmpty() {
        return this.items.length === 0;
    }
    
    size() {
        return this.items.length;
    }
}

const cola = new Queue();

cola.enqueue(10);
cola.enqueue(20);
cola.enqueue(30);

console.log("Elemento en el frente:", cola.peek());
cola.dequeue();
console.log("Elemento en el frente después de dequeue:", cola.peek());

console.log("¿La cola está vacía?", cola.isEmpty());
console.log("Tamaño de la cola:", cola.size());

```