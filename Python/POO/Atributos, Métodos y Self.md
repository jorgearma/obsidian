## ATRIBUTOS

Se pueden definir como algo similar a una variable pero que sólo existen dentro de un objeto. Un ejemplo de atributos:
```python
class Galleta:
    chocolate = False # Este es el atributo.

galleta = Galleta()

if galleta.chocolate:
    print("La galleta tiene chocolate")
else:
    print("La galleta no tiene chocolate")
```
En este caso vemos que creamos una clase galleta y dicha clase la guardamos dentro de la variable galleta. Luego como el atributo chocolate es False pues la galleta en un principio saldrá que no tiene chocolate:
![[Pasted image 20230112220905.png]]
Le podemos cambiar el atributo a True y entonces se habrá cambiado el estado de la galleta a todo lo demas:
```python
class Galleta:
    chocolate = False # Este es el atributo.

galleta = Galleta()

if galleta.chocolate:
    print("La galleta tiene chocolate")
else:
    print("La galleta no tiene chocolate")
```
![[Pasted image 20230112221239.png]]
## MÉTODOS (Las funciones que están dentro de la clase)

Los métodos nos permiten definir funcionalidades para llamarlas desde las instancias. Es algo similar a una función, donde para llamar a uno de los métodos, por ejemplo al método saludar, hacemos uso de la instancia galleta y luego ponemos el nombre del método, por ejemplo Galleta.saludar():
```python
class Galleta: # Primero se llama a la galleta.
    chocolate = False

    def saludar():
        print("Hola, soy una galleta muy sabrosa") # Luego se llama a la función.

Galleta.saludar()
```
![[Pasted image 20230112222002.png]]

Por ejemplo ahora vamos a crear otra clase que se llame gestion_archivos, y tenga dos métodos, uno de crear una carpeta y luego otro de listar archivos; y haremos la llamada a uno u otro método:

```python
import os

class gestion_archivos:
    pass

    def carpeta():
        os.mkdir("Carpeta_nueva")

    def listar():
        print(os.listdir())

gestion_archivos.listar()
```
![[Pasted image 20230112222840.png]]
## SELF

Con self podemos cambiar atributos dentro de un objeto (cambiar atributos dentro de todas las funcione), de tal forma que veamos la diferencia:

PROBLEMA -> Veremos cómo SIN utilizar self, el método no cambia:
```python
class Galleta:
    chocolate = False

    def chocolatear(self):
        chocolate = True # ESTO NO SE VA A EJECUTAR SIN SELF


galleta = Galleta()
galleta.chocolatear()
print(galleta.chocolate)
```
![[Pasted image 20230112223531.png]]
SOLUCION -> Si incluimos el self, veremos cómo el código que está dentro del método sí se aplicará:
```python
class Galleta:
    chocolate = False

    def chocolatear(self):
        self.chocolate = True # ESTO NO SE VA A EJECUTAR SIN SELF


galleta = Galleta()
galleta.chocolatear()
print(galleta.chocolate)
```
![[Pasted image 20230112223706.png]]
