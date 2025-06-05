```js
for (inicialización; condición; actualización) {
   // bloque de código a repetir
}

```

- **Inicialización:** Se utiliza para declarar y asignar un valor inicial a una variable de control. Por lo general, se establece una variable utilizando la palabra clave "let" o "var". Esta parte del ciclo se ejecuta solo una vez al comienzo.
    
- **Condición:** Es una expresión lógica que se evalúa antes de cada iteración del ciclo. Si la condición es verdadera, el bloque de código dentro del ciclo se ejecuta. Si la condición es falsa, el ciclo se detiene y la ejecución continúa con la siguiente instrucción después del ciclo "for".
    
- **Actualización:** Se utiliza para modificar el valor de la variable de control después de cada iteración. Por lo general, se incrementa o decrementa el valor de la variable. Esta parte del ciclo se ejecuta al final de cada iteración, justo antes de evaluar la condición nuevamente

```js ejemplo
const nombres = ['Carlos', 'Christian', 'Christoher', 'Estefania', 'Erika', 'Manuel', 'Diego'];

for (let i = 0; numero < nombres.length; numero++) {
	console.log(nombres[i]);
}
```

