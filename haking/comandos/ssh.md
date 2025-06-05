
# 🛡️ SSH Cheat Sheet para Pentesting

## 📘 ¿Qué es SSH?
SSH (Secure Shell) es un protocolo de red seguro para acceder y controlar sistemas remotos.

---

## 🔑 Autenticación SSH

### 🔹 Con usuario y contraseña:
```bash
ssh usuario@host -p puerto
```

### 🔹 Con clave privada:
```bash
ssh -i /ruta/a/clave_privada usuario@host -p puerto
```

---

## 🛠️ Generar par de claves
```bash
ssh-keygen -t rsa -b 4096
```
- Guarda en `~/.ssh/id_rsa` (privada) y `~/.ssh/id_rsa.pub` (pública)

---

## 📤 Copiar clave pública al servidor
```bash
ssh-copy-id usuario@host
```

Manual:
```bash
cat ~/.ssh/id_rsa.pub | ssh usuario@host 'mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys'
```

---

## 🔐 Permisos correctos
```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
```

---

## 📁 Archivos clave en `~/.ssh/`
| Archivo            | Función                                      |
|--------------------|----------------------------------------------|
| `id_rsa`           | Clave privada                                |
| `id_rsa.pub`       | Clave pública                                |
| `authorized_keys`  | Lista de claves públicas permitidas (servidor) |
| `known_hosts`      | Hosts conocidos                              |
| `config`           | Config personal de conexiones SSH            |

---

## 🧾 `~/.ssh/config` ejemplo:
```ini
Host mi_servidor
    HostName ejemplo.com
    User jorge
    Port 22
    IdentityFile ~/.ssh/id_rsa
```

Con esto puedes conectarte así:
```bash
ssh mi_servidor
```

---

## 🕵️‍♂️ Uso en pentesting

### 🔎 Buscar claves privadas:
```bash
find / -name "id_rsa" 2>/dev/null
```

### 🧪 Conectarse con clave encontrada:
```bash
chmod 600 id_rsa
ssh -i id_rsa usuario@host
```

### 🔐 Fuerza bruta SSH con Hydra:
```bash
hydra -L users.txt -P pass.txt ssh://ip
```

---

## 🔧 Comandos útiles
| Opción  | Descripción                       |
|---------|-----------------------------------|
| `-i`    | Usar clave privada                |
| `-p`    | Especificar puerto                |
| `-v`    | Modo verbose para debug           |
| `-L`    | Redirección de puertos local      |
| `-N`    | No ejecutar comandos (túneles)    |

---

## 📌 Consejo
Usa `-v` o `-vvv` para depurar problemas de conexión:
```bash
ssh -v -i id_rsa usuario@host
```