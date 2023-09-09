**Esto es similar a html, con input se me abre un recuadro para que el usuario pueda escribir.**
Aquí se me abriría el cuadradito para escribir.
```python
valor = input()
------------------------
Esto lo escribo yo mismo
```
```python
# Con esto puedo hacer el típico mensaje de introduce un valor:

numero = input("Introduce un numero: ")

# De esta manera al usuario le aparecerá el mensaje de Introduce un valor
------------------------
Introduce un numero: 50
------------------------
```
```python
# Si quiero hacer algo con el resultado obtenido de lo anterior, debo pasarle la opción int a la variable de antes:

numero = int(numero)

# Debo poner la variable = int(variable) y ahora ya se puede sumar o hacer lo que quiera:

numero + 50
-------------------------
100
-------------------------
```
```python
# Si el usuario pone un número decimal, tenemos que poner float, en lugar de int:

numero = input("Introduce un numero con decimales: ")

# Aquí abajo indico que el usuario va a introducir un número con decimales:

numero = float(numero)
-------------------------
Introduce un numero con decimales: 12.5
-------------------------
```
```python
# Y ya puedo operar con él sin problemas

numero + 10

# Con float puedo introducir números tanto enteros como decimales.
-------------------------
22.5
-------------------------
```
```python
# También puedo hacer todo lo anterior en una misma línea a la vez, esta vez con número entero:

numero = float( input("Introduce un número decimal o entero: "))

-------------------------
Introduce un número decimal o entero: 20
-------------------------
```
```python
numero + 40

-------------------------
60.0
-------------------------
```
```python
# Y ahora lo mismo pero con número decimal:

numero = float( input("Introduce un número decimal o entero: "))

-------------------------
Introduce un número decimal o entero: 10.5
-------------------------
```
```python
numero + 40

# Como vemos con lo anterior, tenemos la opción de usar números enteros y decimales

-------------------------
50.5
-------------------------
```
```python
# También puedo hacer esto con nombres; y la variable Mario se me guarda en nombre

nombre = input("Introduce tu nombre: ")

-------------------------
Introduce tu nombre: Mario
-------------------------
```
```python
nombre = input("Introduce tu nombre ")
apellido = input("Introduce tu apellido ")
edad = int(input("Introduce tu edad ")) # Para número entero
estatura = float(input("Introduce tu estatura ")) # Para número decimal

-------------------------
Introduce tu nombre Mario
Introduce tu apellido Álvarez
Introduce tu edad 26
Introduce tu estatura 1.77
-------------------------
```