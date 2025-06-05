
# 🛡️ OpenSSL s_client Cheat Sheet

Esta hoja de referencia rápida resume los comandos clave para usar `openssl s_client` en escenarios típicos 

---

## 📌 Conectar a un servicio SSL/TLS

```bash
openssl s_client -connect <ip>:<port>
```

**Ejemplo:**

```bash
openssl s_client -connect 10.10.10.10:443
```

---

## 🔍 Ver el certificado del servidor

```bash
openssl s_client -connect <ip>:<port> -showcerts
```

Esto muestra toda la cadena de certificados.

---

## 📤 Enviar datos manualmente (como un navegador)

```bash
openssl s_client -connect <ip>:443
```

Una vez conectado, puedes escribir una petición HTTP:

```
GET / HTTP/1.1
Host: 10.10.10.10

```

---

## 📨 SMTP sobre STARTTLS

```bash
openssl s_client -connect <ip>:587 -starttls smtp
```

---

## 📥 IMAP con SSL

```bash
openssl s_client -connect <ip>:993
```

---

## 🛑 Ignorar errores de certificado

Puedes usar `-verify_return_error` para forzar verificación, o ignorarlo si solo estás testeando.

---

## 📎 Extra: uso típico en CTF o Bandit

```bash
openssl s_client -connect localhost:30001
```

Pega la contraseña anterior como entrada. El servicio responderá si es correcta.

---

## 🧠 Consejos clave

- Revisa el **CN/SAN** del certificado → puede revelar subdominios.
- Ideal para testear servicios que **no puedes probar con `nc` o `telnet`**.
- Es útil para **automatizar conexiones cifradas** en scripts o exploit kits.

---

© Preparación OSCP – ChatGPT & tú 🧠💥