# 🕵️ DIG Cheat Sheet - Descubrimiento de DNS Ocultos 

`dig` es una herramienta poderosa para realizar reconocimiento DNS. Esta guía se enfoca en su uso para encontrar **DNS ocultos** y **errores de configuración** que pueden revelar información crítica.

---

## 🧨 1. Transferencia de Zona DNS (AXFR)

El objetivo es replicar toda la zona DNS (si el servidor lo permite).

```bash
dig axfr targetdomain.com @<DNS_SERVER>
```

🔍 **Ejemplo real en OSCP:**

```bash
dig axfr friendzoneportal.red @10.10.10.123
```

✅ Si funciona, verás una lista completa de registros (A, CNAME, MX, etc), incluyendo subdominios ocultos y a veces hosts internos.

---

## 🔍 2. Resolución de Subdominios Manuales

Prueba con nombres comunes:

```bash
dig dev.targetdomain.com +short
dig staging.targetdomain.com +short
dig admin.targetdomain.com +short
dig internal.targetdomain.com +short
```

🔁 Puedes automatizarlo con un bucle:

```bash
for sub in www dev test mail vpn admin; do dig "$sub.target.com" +short; done
```

---

## 🧪 3. Consultas NS + Enumeración Directa

Descubre los servidores DNS que pueden ser atacados con AXFR:

```bash
dig target.com NS +short
```

Luego prueba cada uno:

```bash
dig axfr target.com @ns1.target.com
```

---

## 🧬 4. Enumerar Registros TXT (posibles claves o verificación)

```bash
dig target.com TXT +short
```

Busca configuraciones mal hechas de SPF, DKIM o mensajes ocultos.

---

## 🧱 5. Reverso de IP (Descubre dominios ocultos)

```bash
dig -x <IP> +short
```

📌 Ejemplo:

```bash
dig -x 10.10.10.123 +short
```

---

## 📡 6. Trazado de resolución (Detectar delegaciones)

```bash
dig target.com +trace
```

Puede mostrar dominios intermedios, subzonas, o DNS externos.

---

## 🧰 7. Combina dig + wordlist (con bash)

```bash
for sub in $(cat subdomains.txt); do
    dig "$sub.target.com" +short | grep -v '^$' && echo "$sub.target.com"
done
```

📁 Wordlist sugerida: `SecLists/Discovery/DNS/subdomains-top1million-5000.txt`

---

## 🛡️ Consejos

- Intenta `dig` desde diferentes servidores DNS (`@1.1.1.1`, `@8.8.8.8`) para evitar filtros.
- Si `dig` no funciona, usa `host` o `dnsrecon` como alternativa.
- Compara respuestas con `+short` y `+noall +answer` para scripting.

---

## 📂 Recursos útiles

- [SecLists DNS Wordlists](https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS)
- [AXFR Info](https://www.owasp.org/index.php/Testing_DNS)
- [HTB Writeups con dig](https://0xdf.gitlab.io/)

---

🚩 *Recuerda que `dig` silenciosamente puede revelar una infraestructura completa si se configura mal el DNS. Siempre prueba transferencia de zona y explora manualmente subdominios comunes.*