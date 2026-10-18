# 🧠 Hashcat — Cheatsheet OSCP / HTB

Hashcat es la herramienta estándar para **crackeo de hashes offline**.  
En OSCP se usa **cuando ya tienes hashes** (shadow, SAM, NTDS, dumps, apps web).

---

## 🔎 Flujo mental OSCP con Hashcat

1. ¿Qué hash tengo?
2. Identificar el **tipo de hash**
3. Elegir **modo (-m)**
4. Elegir **ataque (-a)**
5. Usar **rockyou + reglas**
6. Si falla → máscara / híbrido

---

## 1️⃣ Identificar tipo de hash

### Automático
```bash
hashcat --identify hash.txt
```

### Manual (mirar formato)
| Hash | Ejemplo |
|----|----|
| MD5 | 5f4dcc3b5aa765d61d8327deb882cf99 |
| SHA1 | 40 caracteres hex |
| NTLM | 32 caracteres hex |
| bcrypt | $2y$ |
| SHA512-crypt | $6$ |
| NetNTLMv2 | user::DOMAIN:hash |

---

## 2️⃣ Modos de hash más usados

| Hash | Modo |
|----|----|
| MD5 | -m 0 |
| SHA1 | -m 100 |
| SHA256 | -m 1400 |
| SHA512 | -m 1700 |
| NTLM | -m 1000 |
| NetNTLMv2 | -m 5600 |
| bcrypt | -m 3200 |
| SHA512-crypt | -m 1800 |
| Apache MD5 | -m 1600 |

📌 NTLM y NetNTLMv2 son clave en OSCP

---

## 3️⃣ Ataques

### Diccionario
```bash
hashcat -m 1000 -a 0 hash.txt rockyou.txt
```

### Diccionario + reglas
```bash
hashcat -m 1000 -a 0 hash.txt rockyou.txt -r rules/best64.rule
```

### Fuerza bruta
```bash
hashcat -m 1000 -a 3 hash.txt ?a?a?a?a?a?a
```

### Híbrido
```bash
hashcat -m 1000 -a 6 hash.txt rockyou.txt ?d?d
```

---

## 4️⃣ Reglas importantes

- best64.rule
- rockyou-30000.rule
- OneRuleToRuleThemAll.rule

```bash
hashcat -m 1000 -a 0 hash.txt rockyou.txt -r best64.rule
```

---

## 5️⃣ NetNTLMv2

Formato:
```text
user::DOMAIN:challenge:response
```

Crack:
```bash
hashcat -m 5600 -a 0 netntlmv2.txt rockyou.txt
```

---

## 6️⃣ /etc/shadow (Linux)

```bash
hashcat -m 1800 shadow_hash.txt rockyou.txt
```

---

## 7️⃣ Windows NTLM

```bash
hashcat -m 1000 -a 0 ntlm.txt rockyou.txt
```

---

## 8️⃣ Ver resultados

```bash
hashcat -m 1000 hash.txt --show
```

Con usuario:
```bash
hashcat -m 1000 hash.txt --show --username
```

---

## 9️⃣ Control de sesión

- p → pausar
- s → estado
- --restore → reanudar

---

## 🔥 Tips OSCP

- Empieza siempre con diccionario + reglas
- NetNTLMv2 ≠ NTLM
- bcrypt es lento
- Si no crackea → enumera más

---

## 📁 Rutas útiles

- /usr/share/wordlists/rockyou.txt
- /usr/share/hashcat/rules/

---

## 🧠 Mentalidad OSCP

"Si tienes hashes, tienes una oportunidad.  
Si no crackea, no insistas: enumera más."
---

## 🎯 AD / Kerberos — modos y lección de wordlist (añadido 17 oct 2026)

### Modos Kerberos (NO confundir)
| Ataque | hashcat `-m` | De dónde sale |
|---|---|---|
| **AS-REP Roasting** | **18200** | `impacket-GetNPUsers` → ver [[impacket]], [[../AD/asrep-roasting]] |
| **Kerberoasting** | **13100** (RC4) · 19600/19700 (AES) | `impacket-GetUserSPNs` → [[../AD/kerberoasting]] |

```bash
hashcat -m 18200 asrep.txt seasons.txt --force     # AS-REP
hashcat -m 13100 kerb.txt  seasons.txt --force     # Kerberoasting
hashcat -m 18200 asrep.txt --show                  # ver resultado (potfile)
```

### Lección: rockyou NO lo es todo → wordlist DIRIGIDA
`Autumn2024!` y `Summer2023!` **no están en rockyou**: son patrones *estación+año+símbolo*,
no filtraciones reales. Cuando sospechas un **patrón corporativo** (muy común), te generas
una wordlist a medida:
```bash
for s in Spring Summer Autumn Fall Winter spring summer autumn fall winter; do
  for y in 2021 2022 2023 2024 2025; do
    for sym in '' '!' '1' '123' '2024!'; do echo "${s}${y}${sym}"; done
  done
done > seasons.txt
```
Alternativa: `rockyou.txt` + reglas (`-r /usr/share/hashcat/rules/best64.rule`) o máscaras.

### El potfile (por qué a veces crackea "en 0 segundos")
hashcat guarda lo ya roto en `~/.hashcat/hashcat.potfile`. Re-ejecutar muestra el
resultado al instante aunque uses otra wordlist. Para re-crackear de cero:
`--potfile-disable` o borrar el fichero.
