# 🛠️ WPScan Cheat Sheet 

## ⭐ Scans Favoritos

```bash
# 1. Scan básico + usuarios + plugins activos
wpscan --url http://TARGET -e u,ap

# 2. Scan completo con detección agresiva
wpscan --url http://$RHOST -e ap --plugins-detection aggressive

# 3. Fuerza bruta de login (requiere API token)
wpscan --url http://TARGET --usernames admin --passwords /usr/share/wordlists/rockyou.txt

# 4. Scan con salida a fichero + sin banner
wpscan --url http://TARGET -e u,ap,at --no-banner --output reporte.txt
```

---

## 🔧 Escaneo básico

```bash
wpscan --url http://TARGET
```

- `--url`: URL del sitio WordPress
- `--force`: fuerza el escaneo aunque haya errores o bloqueos

---

## 🔍 Enumeración de usuarios

```bash
wpscan --url http://TARGET -e u
wpscan --url http://TARGET -e u --stealthy
```

- `-e u`: enumera usuarios
- `--stealthy`: modo sigiloso

---

## 🧩 Enumeración de plugins y themes

```bash
wpscan --url http://TARGET -e ap,at
wpscan --url http://TARGET -e ap,at --plugins-detection aggressive
```

- `ap`: plugins activos
- `at`: themes activos

---

## 📦 Detección de vulnerabilidades

```bash
wpscan --url http://TARGET -e vp,vt,cb,dbe
```

- `vp`: plugins vulnerables
- `vt`: themes vulnerables
- `cb`: config backups
- `dbe`: database exports

---

## 🔑 Fuerza bruta de login

```bash
wpscan --url http://TARGET --usernames admin --passwords /usr/share/wordlists/rockyou.txt
```

👉 Requiere **API token**

---

## ⚠️ Bypass de detección de plugins

```bash
wpscan --url http://TARGET --plugins-detection mixed
```

Modos:
- `passive`
- `aggressive`
- `mixed`

---

## 🛡️ API Token

```bash
export WPVULNDB_API_TOKEN='tu_token'
```

- Obtén uno en: https://wpscan.com/profile

---

## 🗂️ Salida y reporte

```bash
wpscan --url http://TARGET -e u,ap,at --output reporte.txt
```

---

## 🧠 Tips y Buenas Prácticas

| Situación                          | Opción                                |
|-----------------------------------|----------------------------------------|
| Solo detectar versión de WP       | `--url http://TARGET -e vp`           |
| Salida limpia para piping         | `--format json` o `--no-banner`       |
| Sitios con WAF / bloqueo          | `--random-user-agent`, `--stealthy`   |
| Proxy para analizar tráfico       | `--proxy http://127.0.0.1:8080`       |
| Sitios con login limitado         | `--throttle 1`                        |