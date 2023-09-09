Con esta función podremos abrir ficheros y trabajar sobre ellos; así sería su funcionamiento por ejemplo para leer el contenido de un documento de texto con Python:

```python
with open('documento.txt') as file:

   leer = file.read()
   print(leer)
```

![[Pasted image 20230108162759.png]]

Para escribir dentro de un fichero lo haríamos de esta forma, aunque esto eliminará todo el contenido del documento:

```python
with open('documento.txt', 'w') as file:

    file.write('Escribimos este texto en el documento')
```

![[Pasted image 20230108163037.png]]

Para escribir varias líneas en un documento y que haga un salto a cada línea:
```python
with open('documento.txt', 'w') as file:

    file.write('Escribimos este texto en el documento\n')
    file.write('Hola que tal\n')
    file.write('Otro texto\n')
    file.write('Final\n')
```

![[Pasted image 20230108163320.png]]


