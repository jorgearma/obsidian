```
ftp anonymous@10.10.100.44
```

Cuando se le solicite una contraseña, simplemente presione la `Enter`tecla y vea si le permitirá iniciar sesión. Si es así, intente lo siguiente:

- `ls`para listar archivos en el servidor
- `get`para recuperar archivos en el servidor
- `less`o `more`para leer archivos desde el shell FTP
- `cd`para cambiar a cualquier directorio potencial
- `put`para probar los permisos de escritura como una forma de encadenar un exploit con otro servicio

Estamos intentando descubrir:

- Nombres de usuario
- Contraseñas
- Archivos de configuración
- Código fuente
- Copias de seguridad
- Cualquier cosa interesante

Si hay muchos archivos y carpetas, puede realizar una descarga **_recursiva_** y analizar los archivos localmente.