
# 🐉 Hydra HTTP POST Form Cheat Sheet (OSCP style)

## 🔹 Comando base:
prestas atencia a http y https
```bash
hydra <IP> http-post-form "<ruta>:<parametros>:<mensaje_error>" -l <usuario> -P <diccionario>


```

---

## 🔸 Parámetros explicados:

- `http-post-form`: indica que el objetivo es un formulario que usa el método POST.
- `<ruta>`: ruta del formulario, por ejemplo: `/login.php`.
- `<parametros>`: datos que se envían en el POST. Sustituye:
  - `^USER^` por el nombre de usuario si usas lista de usuarios.
  - `^PASS^` por las contraseñas del diccionario.
- `<mensaje_error>`: texto exacto que aparece cuando el login falla. Hydra lo usa para detectar intentos fallidos.
- `-l`: un solo usuario.
- `-L`: lista de usuarios.
- `-P`: diccionario de contraseñas.
- `-t`: número de hilos (por defecto 16).
- `-vV`: modo verbo detallado, útil para debugging.

---

## 🧪 Ejemplo adaptado:
```bash
hydra 10.10.10.43 http-post-form "/db/index.php:password=^PASS^&remember=yes&login=Log+In&proc_login=true:Incorrect password" -l 0xdf -P /usr/share/seclists/Passwords/twitter-banned.txt
```

---

## ⚠️ Consejos útiles:

- Usa `Burp` para capturar la petición exacta y copiar los parámetros tal cual.
- Asegúrate de identificar bien el mensaje de error. Si usas uno incorrecto, Hydra puede no detectar el login válido.
- Si el formulario también usa `username`, ponlo en los parámetros: `username=^USER^`.
- Si hay redirecciones, añade `-f` para parar tras encontrar la primera combinación válida.
- Si hay CSRF tokens u otros valores dinámicos, **Hydra no funcionará directamente**. En ese caso, usa `Burp Intruder` o un script con `requests`.

---

Happy hacking! ⚔️