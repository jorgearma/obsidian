Un diccionario en Python es un tipo de dato que permite almacenar pares clave-valor. Estos pares clave-valor se pueden acceder, modificar o eliminar de manera eficiente utilizando la clave correspondiente.
```
# Creación de un diccionario
colors = {'red': 'rojo', 'green': 'verde', 'blue': 'azul'}

# Acceder a un valor utilizando su clave
print(colors['red']) # salida: 'rojo'

# Agregar un nuevo elemento al diccionario
colors['yellow'] = 'amarillo'

# Modificar un valor en el diccionario
colors['red'] = 'Rojo'

# Eliminar un elemento del diccionario
del colors['blue']

# Verificar si una clave está en el diccionario
print('red' in colors) # salida: True
print('blue' in colors) # salida: False

```
De esta forma podemos ejecutar este código y obtener el valor que queramos; por ejemplo vamos a obtener el valor rojo:
![[Pasted image 20230201140835.png]]
Y obtenemos el valor que se encuentra dentro de red:
![[Pasted image 20230201140852.png]]

En este ejemplo, creamos un diccionario llamado `colors` con tres elementos clave-valor. Luego, accedemos a un valor utilizando su clave, agregamos un nuevo elemento, modificamos un valor existente y eliminamos un elemento. Finalmente, verificamos si una clave está en el diccionario utilizando la operación `in`.
![[Pasted image 20230201141002.png]]
