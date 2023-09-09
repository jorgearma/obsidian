Podemos hacer escaneos de direcciones IP desde AbuseIP con este código, donde analizamos una dirección y obtener la respuesta en formato JSON:
```python
import requests

# Definir la URL de la API y la clave de la API
url = "https://api.abuseipdb.com/api/v2/check"
api_key = "18465da2f3a133d04f0f07af96316bedd295c2485c162e263ced344f788d6e3aee5b1f852b18ba3c"

# Definir los parámetros de la solicitud
informacion = {
    "ipAddress": "124.235.251.192",
    "maxAgeInDays": "90"
}

# Definir las cabeceras de la solicitud con la clave de la API
api = {
    "Key": api_key,
    "Accept": "application/json"
}

# Realizar la solicitud a la API
response = requests.get(url, headers=api, params=informacion)

# Mostrar la respuesta de la API
respuesta = response.json()
print(respuesta)
```
![[Pasted image 20230403232558.png]]
## DETECTAR NÚMERO DE REPORTES ABUSEIP CON PYTHON
Podemos filtrar únicamente la parte donde se muestran los reportes de una IP filtrando la información, ya que se trata de un diccionario:
```python
import requests

url = "https://api.abuseipdb.com/api/v2/check"
api_key = "18465da2f3a133d04f0f07af96316bedd295c2485c162e263ced344f788d6e3aee5b1f852b18ba3c"


informacion = {
    "ipAddress": "124.235.251.192",
    "maxAgeInDays": "90"
}

api = {
    "Key": api_key,
    "Accept": "application/json"
}

response = requests.get(url, headers=api, params=informacion)

respuesta = response.json()

# Filtramos sólo la parte de los reportes:

print(respuesta['data']['totalReports'])
```
![[Pasted image 20230403232740.png]]
## AUTOMATIZAR EL ESCANEO DE VARIAS IP EN ABUSEIP CON PYTHON
Si quiero escanear varias direcciones a la vez, podría hacer un bucle:
```python
import requests

url = "https://api.abuseipdb.com/api/v2/check"
api_key = "18465da2f3a133d04f0f07af96316bedd295c2485c162e263ced344f788d6e3aee5b1f852b18ba3c"


listado_ip = ['124.235.251.192', '177.36.187.95', '64.62.197.232', '118.201.79.222']

for cada_ip in listado_ip:
    informacion = {
        "ipAddress": cada_ip,
        "maxAgeInDays": "90"
    }
    api = {
        "Key": api_key,
        "Accept": "application/json"
    }
    
    response = requests.get(url, headers=api, params=informacion)
    respuesta = response.json()

# Filtramos sólo la parte de los reportes:

    ip = respuesta['data']['ipAddress']
    reportes = respuesta['data']['totalReports']

    print(f"Para la IP {ip}, tiene estos reportes {reportes}")
```
![[Pasted image 20230403233915.png]]
## FILTRAR AQUELLAS IP CON UN DETERMINADO NÚMERO DE REPORTES
Si quiero ver sólo aquellas direcciones con un número determinado de reportes, lo haría de esta forma:
```python
import requests

url = "https://api.abuseipdb.com/api/v2/check"
api_key = "18465da2f3a133d04f0f07af96316bedd295c2485c162e263ced344f788d6e3aee5b1f852b18ba3c"


listado_ip = ['124.235.251.192', '177.36.187.95', '64.62.197.232', '118.201.79.222']

for cada_ip in listado_ip:
    informacion = {
        "ipAddress": cada_ip,
        "maxAgeInDays": "90"
    }
    api = {
        "Key": api_key,
        "Accept": "application/json"
    }
    
    response = requests.get(url, headers=api, params=informacion)
    respuesta = response.json()

# Filtramos sólo la parte de los reportes:

    ip = respuesta['data']['ipAddress']
    reportes = respuesta['data']['totalReports']

# Aquí solo nos dice aquellas IP que tienen más de un determinado número de reportes:

    if reportes >= 400:
        print(f"La IP {ip}, tiene más de 400 reportes, con un número de {reportes}")
```
![[Pasted image 20230403234338.png]]