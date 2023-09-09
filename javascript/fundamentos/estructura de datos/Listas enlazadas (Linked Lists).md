2. Listas enlazadas (Linked Lists):
    
    - Uso: Las listas enlazadas son adecuadas cuando necesitas una estructura de datos dinámica en la que se realicen inserciones y eliminaciones frecuentes en cualquier posición.
    - Métodos comunes:
        - `insert()`: Inserta un elemento en una posición específica de la lista.
        - `remove()`: Elimina un elemento de la lista.
        - `get()`: Obtiene el valor de un elemento en una posición dada.
        - `isEmpty()`: Verifica si la lista está vacía.
```js
// Definir un nodo de la lista enlazada
class Nodo {
  constructor(valor) {
    this.valor = valor;
    this.siguiente = null;
  }
}

// Crear una lista enlazada y realizar operaciones
class ListaEnlazada {
  constructor() {
    this.cabeza = null;
  }

  insertar(valor) {
    let nuevoNodo = new Nodo(valor);

    if (!this.cabeza) {
      this.cabeza = nuevoNodo;
    } else {
      let nodoActual = this.cabeza;
      while (nodoActual.siguiente) {
        nodoActual = nodoActual.siguiente;
      }
      nodoActual.siguiente = nuevoNodo;
    }
  }

  imprimir() {
    let nodoActual = this.cabeza;
    while (nodoActual) {
      console.log(nodoActual.valor);
      nodoActual = nodoActual.siguiente;
    }
  }
}

// Crear una instancia de la lista enlazada y realizar operaciones
let lista = new ListaEnlazada();
lista.insertar(1);
lista.insertar(2);
lista.insertar(3);
lista.imprimir();

```


# play list

lista enlazada para play list
```js
class Song {
    constructor(title, artist) {
        this.title = title;
        this.artist = artist;
        this.next = null;
    }
}

class Playlist {
    constructor() {
        this.head = null;
        this.nowPlaying = null;
    }

    addSong(title, artist) {
        const newSong = new Song(title, artist);
        if (!this.head) {
            this.head = newSong;
            this.nowPlaying = newSong;
        } else {
            let current = this.head;
            while (current.next) {
                current = current.next;
            }
            current.next = newSong;
        }
    }

    playNext() {
        if (this.nowPlaying && this.nowPlaying.next) {
            this.nowPlaying = this.nowPlaying.next;
            console.log(`Now playing: ${this.nowPlaying.title} by ${this.nowPlaying.artist}`);
        } else {
            console.log("No more songs to play.");
        }
    }
}

// Ejemplo de uso
const playlist = new Playlist();
playlist.addSong("Song 1", "Artist 1");
playlist.addSong("Song 2", "Artist 2");
playlist.addSong("Song 3", "Artist 3");

playlist.playNext(); // Now playing: Song 2 by Artist 2
playlist.playNext(); // Now playing: Song 3 by Artist 3
playlist.playNext(); // No more songs to play.

```