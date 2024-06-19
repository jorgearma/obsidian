Módulos de Python para ejecutar servicios para transferir archivos:

- `python2 -m SimpleHTTPServer 80`Activa un servidor web en el directorio en el que se encuentra ubicado en el puerto 80.
- 
- `python3 -m http.server 80`Activa un servidor web Python versión 3.X en el directorio donde se encuentra en el puerto 80.
- 
- `python2 -m pyftpdlib -p 21 -w`activa un servidor FTP en el directorio en el que se encuentra ubicado en el puerto 21 y permite el acceso de inicio de sesión anónimo.
- 
- `python3 -m pyftpdlib -p 21 -w`activa un servidor FTP Python 3.X en el directorio donde se encuentra en el puerto 21 y permite el acceso de inicio de sesión anónimo.
    



1. `wget http://127.0.0.1/file.exe`: Este comando descarga el archivo `file.exe` desde el servidor web que se encuentra en la dirección IP local `127.0.0.1`.
    
2. `wget -O msi-install.exe http://127.0.0.1/file.exe`: Con este comando, estás descargando el mismo archivo `file.exe` desde el servidor web en `127.0.0.1`, pero estás renombrándolo como `msi-install.exe` en tu sistema local. La opción `-O` te permite especificar el nombre del archivo de salida.
    
3. `wget -b http://127.0.0.1/file.exe`: Aquí, estás descargando el archivo `file.exe` en segundo plano. Esto significa que la descarga se ejecutará en segundo plano, lo que te permitirá seguir utilizando la terminal para otras tareas mientras se descarga el archivo.
    
4. `wget --ftp-user=User --ftp-password=ftp://127.0.0.1/file.exe -o msi-install.exe`: Este comando parece incorrecto. La opción `--ftp-user` se utiliza para especificar el nombre de usuario para la autenticación FTP, mientras que `--ftp-password` se usa para especificar la contraseña. Sin embargo, parece que has incluido la URL FTP (`ftp://127.0.0.1/file.exe`) dentro de la opción `--ftp-password`, lo cual no es correcto. La opción `-o` se utiliza para especificar el nombre del archivo de salida, pero en este caso, parece que también está mal utilizado.