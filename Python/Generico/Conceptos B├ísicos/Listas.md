```python
# Puedo guardar varios strings en una variable, de la siguiente forma:

datos = [4,"Una cadena",15,3,14,"Otra cadena"]

# Y luego puedo sacar cada una de las cadenas tal y como hacíamos antes con el slicing:

datos[1]

# Voy a sacar la cadena número 5

------------------------
Una cadena
------------------------
```
```python
# Para ver el úiltimo ítem de esta lista, puego hacerlo con números negativos, como antes:

datos[-1]

------------------------
Otra cadena
------------------------
```
```python
# O también puedo referirme desde la penúltima cadena hasta el final, por ejemplo:

datos[-2:]

# Lo de los 2 puntos es similar al excel, se hace para abarcar más
```

![[Pasted image 20230104155828.png]]

```
# También puedo concatenar unos números con más números dentro de una variable, es decir, concatenar listas con listas:
# Primero definimos la lista de números:

numeros = [1,2,3,4]

numeros + [5,6,7,8,9,10]

# De esta manera se va a sumar la lista dentro de la variable números, con los números de 5,6,7,8,9,10 que puse antes.
```

![[Pasted image 20230104155848.png]]

```
# Como modificar una lista, de la siguiente manera:

pares = [0,2,4,5,8,10]

pares

# Esta lista es errónea por el número 5 es impar.
```

![[Pasted image 20230104155907.png]]

```
# Ahora voy a corregir lo anterior:

pares[3]= 6

pares

# Al poner el número 3, me estoy refiriendo a ese caracter que quiero modificar.
```

![[Pasted image 20230104155926.png]]

```
# También puedo hacer una modificación a la lista anterior de añadir algo:

pares.append(12)

pares
```

![[Pasted image 20230104155943.png]]

```
# Puedo modificar varios caracteres de una lista a la vez:
# Primero voy a crear una lista de ejemplo:

letras = ["a","b","c","d","e","f"]

letras[:3]

# Se me van a mostrar las 3 primeras letras.
```

![[Pasted image 20230104160004.png]]

```
# Y ahora puedo cambiar estas tres primera a mayúsculas así:

letras[:3] = ["A","B","C"]

# Vamos a mostrarlo:

letras
```

![[Pasted image 20230104160023.png]]

```
# También puedo vaciar el contenido de una lista, por ejemplo voy a vaciar los tres primeros elementos de la lista:

letras[:3] = []

# Ahora veremos como se borraron esos primeros 3 elementos:

letras
```

![[Pasted image 20230104160040.png]]

```
# Y para borrar TODO el contenido:

letras = []

# Lo mostramos:

letras
```

![[Pasted image 20230104160058.png]]

```
# LISTAS ANIDADAS, de esta forma puedo juntar varias listas a la vez

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

# Dentro de r, guardo de contenido de las tres listas de arriba

r = [a,b,c]
```

```
# Dentro de la lista r, también puedo seleccionar una de las tres listas que tiene en su interior:
# Para referirme a la lista a, dentro de r, hago lo siguiente:

r[0]

# Va a sacar solo el contenido de a
```

![[Pasted image 20230104160202.png]]

```
# Vamos a acceder a la lista 3, aunque también podía poner r[-1]

r[2]
```

![[Pasted image 20230104160222.png]]

```
# Podemos también referirnos a un número concreto dentro de una de las listas dentro de r:

r[1][1]

# Esto es la lista b, el segundo elemento.
```

![[Pasted image 20230104160550.png]]

```
# Y esto el último número de la última lista:

r[-1][-1]
```

![[Pasted image 20230104160837.png]]

```
# Lista c, segundo número de la lista, ya que el primero será 0

r[2][1]
```

![[Pasted image 20230104160856.png]]

```
# Para dividir cada uno de los strings de mi variable, así puedo operar con ellos más tarde:

elementos = "Thu Mar 17 19:24:25 2022"
        
print(elementos)
```

![[Pasted image 20230104160913.png]]

```
# Para separar cada uno de estos elementos en comas lo hago con split()

listabien = elementos.split()
print(listabien)
```

![[Pasted image 20230104160929.png]]

```
# Para meter en una lista el contenido de por ejemplo un directorio inspeccionado con el bucle for:

import os

lista = []

for i in os.listdir("/Users/mario/Desktop/Python/"):
    lista.append(i)

print(lista)
```

![[Pasted image 20230104160946.png]]

```
# Incluso puedo recorrer archivos de un directorio e ir guardandolos en una lista y luego dentro de un bucle for hacer que se vayan copiando a otra ubicación (aunque con directorios da error):

import os
import shutil

lista = []

for i in os.listdir("/Users/mario/Desktop/Python/"):
    lista.append(i)

print(lista)

for i in lista:
    shutil.copy(i, "/Users/mario/Desktop/prueba/")
```

