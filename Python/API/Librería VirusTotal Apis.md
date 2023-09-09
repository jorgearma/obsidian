Hay una librería en Python que nos permite utilizar la API de virustotal, que se llama virus_total_apis. Por tanto con este código podríamos conectarnos a virustotal y obtener el reporte de un archivo:
```python
from hashlib import md5
from virus_total_apis import PublicApi

API_KEY = "974ab16a5f23d3c9997954dd01f253e2752f4a7b092a82cc3d68ecf06ff336f6" # Importamos la API de virustotal.
api = PublicApi(API_KEY)

with open("pruebas.py", "rb") as f:
    file_hash = md5(f.read()).hexdigest() # Convertimos en hash todo el contenido del archivo.
response = api.get_file_report(file_hash) # Obtenemos la respuesta de virustotal

print(response)
```
![[Pasted image 20230403141732.png]]
También podemos utilizar sentencias condicionales que evalúen los resultados en forma de diccionario que nos ofrece virustotal:
```python
import hashlib
from virus_total_apis import PublicApi

API_KEY = "974ab16a5f23d3c9997954dd01f253e2752f4a7b092a82cc3d68ecf06ff336f6" # Importamos la API de virustotal.
api = PublicApi(API_KEY)

with open("pruebas.py", "rb") as f:
    file_hash = hashlib.md5(f.read()).hexdigest()
response = api.get_file_report(file_hash) 

# Aquí evalúa los resultados del análisis.

if response["response_code"] == 200: # Entramos en este if si el escaneo fue exito.
    if response["results"]["positives"] > 0: # Detecta que no haya ningún positivo, por lo que es malicioso.
        print("Archivo malicioso.")
    else:
        print("Archivo seguro.") # Si encuentra que es positivo se imprime esto.
else:
    print("No ha podido obtenerse el análisis del archivo.")
```
## DETECTAR LOS REPORTES QUE TIENE UN ARCHIVO
También podemos hacer que el script nos diga si un archivo tiene más de 10 o 15 reportes por ejemplo, simplemente accediendo al diccionario:
```python
import hashlib
from virus_total_apis import PublicApi

API_KEY = "974ab16a5f23d3c9997954dd01f253e2752f4a7b092a82cc3d68ecf06ff336f6"
api = PublicApi(API_KEY)

with open("pruebas.py", "rb") as f:
    file_hash = hashlib.md5(f.read()).hexdigest()
response = api.get_file_report(file_hash) 

# Aquí evalúa los resultados del análisis.

if response["response_code"] == 200: 
    if response["results"]["positives"] >= 15: # Detecta que no haya ningún positivo, por lo que es malicioso.
        print("El archivo tiene 15 o más reportes.")
    else:
        print("El archivo tiene menos de 15 reportes.") 
else:
    print("No ha podido obtenerse el análisis del archivo.")
```
![[Pasted image 20230403152057.png]]
Ahora otro ejemplo con otro archivo que sí tiene más de 15 reportes:
```python
import hashlib
from virus_total_apis import PublicApi

API_KEY = "974ab16a5f23d3c9997954dd01f253e2752f4a7b092a82cc3d68ecf06ff336f6" # Importamos la API de virustotal.
api = PublicApi(API_KEY)

with open("virus.exe", "rb") as f:
    file_hash = hashlib.md5(f.read()).hexdigest()
response = api.get_file_report(file_hash) 

# Aquí evalúa los resultados del análisis.

if response["response_code"] == 200: 
    if response["results"]["positives"] >= 15: # Detecta que no haya ningún positivo, por lo que es malicioso.
        print("El archivo tiene 15 o más reportes.")
    else:
        print("El archivo tiene menos de 15 reportes.") 
else:
    print("No ha podido obtenerse el análisis del archivo.")
```
![[Pasted image 20230403152032.png]]
