```python
# Podemos usar un bucle for para recorrer toda una cadena de texto:

for x in "Hola amigos":
    print(x)
```
Ejemplo de bucle for con un correo electrónico; si el correo tiene @ es True, si no lo tiene es False:
Va a haber un momento del bucle donde i va a ser arroba; y es ahí cuando email va a pasar a ser True:
```python
email=False # En un principio el email es False

for i in input():
    if i=="@":
        email=True  # Pero si el email tiene un @, pasará a ser True

if email==True:
    print("El email es correcto") # Si es True (teniendo el @), imprimirá este mensaje.
else:
    print("El email no es correcto") # Si es False, imprimirá este otro.
    
# El bucle for va recorriendo cada uno de los caracteres uno a uno de la lista.
```

Ejemplo de un programa que verifique si una contraseña tiene determinados caracteres o no:

```python
contraseña=False

for i in input("Introduce una contraseña que tenga un arroba, un asterisco y una almohadilla: "):
    if i== "#" and "@" and "*":
        contraseña=True

if contraseña==True:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
```

![[Pasted image 20230104152624.png]]
**Lectura secuencial con for (usando enumerate)**
```python
indice = 0
numeros = [1,2,3,4,5,6,7,8,9,10]
for indice,numero in enumerate(numeros):
    numeros[indice] *= 10
numeros
```

![[Pasted image 20230104152706.png]]

```python
# También podemos crear un secuenciador para repetir un bucle for el número de veces que queramos:

for numero in range(5,10):
    print(numero)

```

![[Pasted image 20230104153322.png]]

```python
# Con lo siguiente, si el múltiplo de 2 NO es de 0, entonces que me imprima esos números. Saldrán los impares:

for n in range(10):
    if n % 2 != 0:
        print(n)
```

![[Pasted image 20230104152734.png]]

```python
# Ahora por último, un bucle for que inspeccione el contenido de una carpeta y si hay un documento con un determinado nombre, crea una carpeta:

import os

for i in os.listdir():
    print("En esta vuelta la variable i es el fichero: ", i)
    if i == "Introducción.py":
        print("Se encontró un archivo con ese nombre, creo una carpeta")
        os.mkdir("Carpetita")
    else:
        print("No se encontró el archivo...")
```

```python
# Podemos crear un bucle para ver si se repiten archivos en dos carpeta diferentes:

import os

prueba = os.listdir("/Users/mario/Desktop/prueba/")
carpetadestino = os.listdir("/Users/mario/Desktop/carpetadestino/")

for i in prueba:
   for a in carpetadestino:
       if i==a:
           print("Se repiten los archivos: ",a,i)
```

![[Pasted image 20230104152810.png]]

```python
# Ahora por ejemplo voy a hacer un DOBLE BUCLE FOR para recorrer al mismo tiempo dos carpetas y hacer comparaciones, por ejemplo para eliminar los archivos duplicados:

import os

# Guardamos en listas los archivos de estos directorios:
archivosprueba = os.listdir("/Users/mario/Desktop/prueba/")
archivoscarpetadestino = os.listdir("/Users/mario/Desktop/carpetadestino/")

# Guardamos las rutas de las dos carpeta, para luego hacer un os.chdir() sobre la carpeta donde queramos borrar los archivos duplicados.

rutaprueba = ("/Users/mario/Desktop/prueba/")
rutacarpetadestino = ("/Users/mario/Desktop/carpetadestino/")

for i in archivosprueba:
   for a in archivoscarpetadestino:
        if i==a:
           print("Se repiten los archivos: ",a,i)
           os.chdir(rutacarpetadestino)
           os.remove(a) # Se borrarán los archivos duplicados que aparecerán abajo.
```

![[Pasted image 20230104152833.png]]

```python
# Una forma más eficiente de usar un bucle for, donde todos los resultados del bucle en total se guardan en una variable:

import os


hola = [_ for _ in os.listdir()]
```

![[Pasted image 20230104153059.png]]

```python
# Ahora haremos lo mismo pero guardaremos en la variable sólo los archivos que cumplan con un determinado patrón:

extensiones = r".png",r"jpg" # Va a guardar en la variable archivospng solo los archivos que tengan esas extensiones:
archivospng = [_ for _ in os.listdir() if _.endswith(extensiones)]

print(archivospng)
```

![[Pasted image 20230104153119.png]]

```python
# Ordenar archivos según su extensión utilizando de esta forma un bucle for:

import os
import shutil

while(True):
        
        if os.path.exists("documentos") == True:
            pass
        else: 
            os.mkdir("documentos")
            continue
        
        if os.path.exists("fotos") == True:
            pass
        else:
            os.mkdir("fotos")
            continue
            
        if os.path.exists("videos") == True:
            pass
        else:
            os.mkdir("videos")
            continue
        
        if os.path.exists("otros") == True:
            pass
        else:
            os.mkdir("otros")
            continue
            
        if os.path.exists("musica") == True:
            pass
        else:
            os.mkdir("musica")
        break


extensionesdocumentos = r".pdf", r".doc", r".docx", r".txt",r".odt",r".xlsx",r".ppt",r"pptx"
documentos = [_ for _ in os.listdir() if _.endswith(extensionesdocumentos)]

for i in documentos:
    shutil.move(i, "documentos")



extensionesfotos = r".png", r".jpg", r".jpeg", r".gif",r".tiff", r".bmp"
fotos = [_ for _ in os.listdir() if _.endswith(extensionesfotos)]

for i in fotos:
    shutil.move(i, "fotos")



extensionesvideos = r".mp4", r".mkv", r".avi", r".mov",r".flv", r".divx"
videos = [_ for _ in os.listdir() if _.endswith(extensionesvideos)]

for i in videos:
    shutil.move(i, "videos")


extensionesmusica = r".mp3", r".aac", r".wav", r".aiff",r".wma",r".opus",r".ogg"
musica = [_ for _ in os.listdir() if _.endswith(extensionesmusica)]

for i in musica:
    shutil.move(i, "musica")


extensionesotros = r".py", r".rar", r".zip", r".html",r".tmp",r".dat",r".exe",r".deb",r".dmg"r".psd"
otros = [_ for _ in os.listdir() if _.endswith(extensionesotros)]

for i in otros:
    shutil.move(i, "otros")
```

