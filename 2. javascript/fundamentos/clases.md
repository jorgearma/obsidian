las class son  una plantilla para crear objetos
la variables se llaman propiedades
y las funciones 

Estructura de una clase:

- Propiedades: La clase puede contener variables. Dentro de una clase se llaman propiedades.

 Constructor: Es un metodo especial para inicializar un objeto creado a partir de una clase.

Métodos: La clase puede contener funciones. Dentro de una clase se llaman metodos.
```java
/*

*/

class Usuario {
	tipo = 'usuario';

	constructor(nombre, apellido) {
		this.nombre = nombre;
		this.apellido = apellido;

		console.log('Nuevo usuario registrado!');
	}

	obtenerNombreCompleto() {
		console.log('Obteniendo datos...');
		return `${this.nombre} ${this.apellido}`;
	}
}

const usuario = new Usuario('Carlos Arturo', 'Esparza');
console.log(usuario.obtenerNombreCompleto());

const usuario2 = new Usuario('Alejandro', 'Garcia');
console.log(usuario2.obtenerNombreCompleto());
```

## herencia

```java
/*
	📌 Herencia
	La herencia nos permite crear clases tomando las propiedades y metodos de otras clases.
*/

class Usuario {
	constructor(usuario, password) {
		this.usuario = usuario;
		this.password = password;
	}

	obtenerPosts() {
		const posts = ['post1', 'post2'];
		return posts;
	}
}

class Moderador extends Usuario {
	constructor(usuario, password, permisos) {
		// Super nos permite copair todos los metodos y propiedades de la clase original.
		// Incluyendo el constructor, por eso le pasamos los parametros usuario y password.
		super(usuario, password);
		this.permisos = permisos;
	}

	borrarPost(id) {
		if (this.permisos.includes('borrar')) {
			console.log(`El post con el ${id} ha sido borrado`);
		} else {
			console.log('No tienes los suficientes permisos para borrar posts');
		}
	}
}

const usuario1 = new Usuario('carlos', '123');
console.log(usuario1.permisos);
console.log(usuario1.obtenerPosts());

// El usuario 2 es un moderador
const usuario2 = new Moderador('arturo', '123', ['borrar', 'editar']);
// Tambien puede acceder a los metodos y propiedades de la clase Usuario.
console.log(usuario2.tipo);
console.log(usuario2.obtenerPosts());
usuario2.borrarPost(1);```



## metodos estaticos


```java
/*
	📌 Propiedades y Métodos Estaticos
	Para poder acceder a las propiedades y metodos de una clase, 
	primero tenemos que crear un nuevo objeto apartir de una clase.

	Esto lo podemos cambiar utilizando propiedades y métodos estaticos.
*/
class Usuario {
	constructor(nombre, correo) {
		this.nombre = nombre;
		this.correo = correo;

		console.log('Se ha creado un usuario en la base de datos');
	}

	static borrar(id_usuario) {
		console.log(`El usuario con el id: ${id_usuario} ha sido borrado de la base de datos`);

		/* Si usamos metodos estaticos, no vamos a poder acceder al nombre y correo, 
		porque para eso necesitabamos el constructor */
		 console.log(this.nombre);
	}

	// Tambien funciona con propiedades
	static registrados = 1000;
}

// Para poder borrar al usuario teniamos que crear un objeto primero:
 const usuario = new Usuario('carlos', 'correo@correo.com');

// Si tenemos una propiedad o metodo estatico podemos acceder sin crear el objeto.
Usuario.borrar(1);
console.log(Usuario.registrados);
```