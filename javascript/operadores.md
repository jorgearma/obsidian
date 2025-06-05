
```java
// Los operadores nos permiten asignar elementos, hacer cálculos básicos y comparaciones.

/* 📌 Operadores Aritmeticos
	=	Operador de asignación. Se usa para asignar valores a 
una variable
	+	Suma
	-	Resta
	*	Multiplicación
	/	Division
	%	Modulo     es el resto de la division no el resul
	++	Aumento
	--	Disminución
*/

 const resultado1 = 10 + 10; // 20
 const resultado2 = 10 - 10; // 0
 const resultado3 = 10 % 3; // 1 (Resto de una división)

 let numero = 1;
 numero++; // Aumentamos el numero en una unidad.
 console.log(numero);
 numero--; // Disminuimos el numero en una unidad.
 console.log(numero);

/*📌 Operadores de Asignación
	+=	Suma un numero al valor de una variable.
	-=	Resta un numero al valor de una variable.
	*=	Resta un numero al valor de una va riable.
	/=	Resta un numero al valor de una variable.
	%=	Obtiene el sobrante de una division y lo asigna a la variable.
*/
 let numero = 10;
 numero = numero + 5; // 15
 numero += 5;
 console.log(numero);

/* 📌 Operadores de Comparación:
Nos permiten comparar valores
	==		Igual que
	===		Igual en valor y typo de valor
	!=		Diferente
	!==		Diferente en valor y diferente en typo
	>		Mayor que
	<		Menor que
	>=		Mayor o igual que
	<=		Menor o igual que
	?		Operador ternario
*/

 const resultado = 5 > 1; // true
 const resultado = 20 <= 20; // true
 const resultado = 10 == 10;
 const resultado = 10 == '10'; // True (Solo compara el valor)
 const resultado = 10 === '10'; // false (compara si el valor es igual y si el tipo es igual)
 const resultado = 7 > 1 ? 'El primer valor es mayor que el segundo' : 'El segundo valor es mayor que el primero';

/* 📌 Operadores Lógicos 
	&& 	And
	||	OR
	! 	NOT
*/

const nombre = 'Carlos';
const edad = 17;
const tieneEntrada = true;
const tienePermiso = false;

// Ejemplo #1
 const permitirAcceso = edad > 18 && tieneEntrada; // true
 console.log('Acceso permitido al concierto: ' + permitirAcceso);

// Ejemplo #2 - OR
 const permitirAcceso = (edad > 18 && tieneEntrada) || (tieneEntrada && tienePermiso);
// console.log('Acceso permitido al concierto: ' + permitirAcceso);

// Ejemplo #3 - !
// Retorna true si un valor es negativo
const variable = true;
console.log(!variable); // false
```

## operadores ternarios => <mark style="background: #BBFABBA6;"> ?</mark>

poner la condicion despues del igual 

 -funciona como un: esto, si no es verda, esto otro

```js  
condición ? expresión_si_verdadero : expresión_si_falso
```

```js
/*El operador ternario nos permite hacer condicionales abarcando menos codigo que si utilizaramos un condicional if.
*/

 Ejemplo de condicional sin operador ternario.
 const boleto = 'vip';
 let codigoDeAcceso;

 if (boleto === vip) {
 	codigoDeAcceso = 'VIP-123-456-789';
 } else {
 	codigoDeAcceso = 'Regular-123-456-789';
 }

// Ejemplo con operador ternario
const boleto = 'vip';
const codigoDeAcceso = boleto === 'VIP' ? 'VIP-123-456-789' : 'Regular-123-456-789';

// Ejemplo 2 - No siempre es necsario guardar el valor en una variable
boleto === 'VIP' ? console.log('Tu boleto es VIP-123-456-789') : console.log('Tu boleto es Regular-123-456-789');
```

## operador spread

funciona colocando tres puntos ... + nombre 
  
  
```java
/* 📌 Operador Spread
	Permite tomar los elementos de un arreglo u objeto y expandirlos en otro sitio.
*/
 const frutas = ['Manzana', 'Pera', 'Piña', 'Melon'];
 const comidaFavorita = ['Pizza', 'Sushi', ...frutas];
 console.log(comidaFavorita);

 const datosLogin = {
 	nombre: 'Arturo',
 	correo: 'correo@correo.com',
 	password: '123',
 };

 const usuario = {
 	...datosLogin,
 	nombre: 'Carlos',
 	edad: 27,
 };

 console.log(usuario);

/*
	📌 Parametro Rest
	Permite que una funcion contenga un numero indefinido de argumentos.
	Los argumentos extra que encuentre los convertira en un arreglo.
*/
 const registrarUsuario = (nombre, correo, ...datosAdicionales) => {
 	console.log(nombre, correo, datosAdicionales);
 };

 registrarUsuario('Carlos', 'correo@correo.com');
 registrarUsuario('Alejandro', 'alex@correo.com', 28, 'España');

/*
	📌 Destructuración de objetos
	Nos permite obtener elementos o propiedades de un arreglo u objeto y guardarlos en una variable.
*/
const amigos = ['Alejandro', 'Cesar', 'Manuel'];
const primerAmigo = amigos[0];
const segundoAmigo = amigos[1];
const [primerAmigo, segundoAmigo, tercerAmigo] = amigos;
console.log(segundoAmigo);

const persona = {
	nombre: 'Carlos',
	edad: 27,
	pais: 'México',
};

const { nombre, pais, edad } = persona;
console.log(nombre, pais);

const mostrarEdad = ({ nombre, edad }) => {
	console.log(`${nombre} tiene ${edad} años`);
};
mostrarEdad(persona);
```