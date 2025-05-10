# 🧠 Guía para Leer e Interpretar la Salida de `linpeas.sh` (OSCP)

## 🎯 Objetivo

Saber **interpretar correctamente el output de `linpeas.sh`** para detectar vectores de **escalada de privilegios** en sistemas Linux.

---

## 🧾 ¿Qué es `linpeas`?

`linpeas.sh` es un script de enumeración automatizada que recopila información del sistema Linux para detectar **vulnerabilidades de escalada de privilegios**.

- 📦 Repositorio: [https://github.com/carlospolop/PEASS-ng](https://github.com/carlospolop/PEASS-ng)

---

## 🚀 Ejecución

```bash
chmod +x linpeas.sh
./linpeas.sh
```

También puedes subirlo con `scp`, `wget`, o usar `curl`:

```bash
curl -sL https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | bash
```

---

## 🔍 ¿Qué secciones son más importantes?

### 🟩 1. **SUID Binaries**
Busca binarios con el bit SUID activado (ejecutados como el propietario, normalmente root).

🔎 Busca líneas como:
```bash
-rwsr-xr-x 1 root root 123K date /usr/bin/somebinary
```

✔️ Revisa si ese binario está listado en [GTFOBins](https://gtfobins.github.io/).

---

### 🟨 2. **Capabilities**
Busca binarios con capacidades peligrosas (ej. `cap_setuid`, `cap_net_raw`, etc.)

```bash
/usr/bin/python3.8 = cap_setuid+ep
```

✔️ Si puedes ejecutarlo, podrías escalar privilegios con él.

---

### 🟥 3. **Archivos con permisos de escritura**
Te muestra archivos propiedad de root o con permisos interesantes:

```bash
-rw-rw-r-- 1 root root 12K /etc/passwd
```

✔️ Si puedes escribir en `/etc/passwd` o `/etc/shadow`, puedes añadir un usuario.

---

### 🟦 4. **Tareas cron**
Busca trabajos automáticos como:

```bash
/etc/cron.d/backup
```

✔️ Abre el script y verifica si puedes modificarlo o alguno de los comandos que ejecuta.

---

### 🟪 5. **Servicios y Timers**
`systemd` puede ejecutar tareas con permisos elevados.

Ejemplo:
```bash
UNIT FILE          STATE   
backup.service     enabled
```

✔️ Revisa si puedes escribir sobre el servicio o algún binario involucrado.

---

### 🧾 6. **Archivos interesantes y credenciales**
- `.bash_history`
- `.ssh/id_rsa`
- `.git/config`
- Archivos de configuración de bases de datos (`config.php`, `.env`)

✔️ Busca contraseñas o claves SSH privadas.

---

### 🧬 7. **Información de red**
- Puertos abiertos
- Servicios escuchando en localhost
- Archivos `/etc/hosts` modificados

✔️ Puede ayudarte a pivotear o entender mejor el contexto.

---

### 🛠️ 8. **Binarios en PATH modificables**
Muestra rutas donde puedes colocar un binario malicioso.

```bash
PATH=/usr/local/bin:/usr/bin:/home/user/bin
```

✔️ Busca directorios donde tengas permisos de escritura.

---

### 🔐 9. **Usuarios en sudoers**
Te indica si puedes usar `sudo` sin contraseña:

```bash
(ALL) NOPASSWD: /usr/bin/vim
```

✔️ ¡Entrada directa a root!

---

## 🧠 Consejos para la lectura

- Lee primero lo que esté **en colores más intensos**: es lo más crítico.
- Busca palabras como `writable`, `executable`, `interesting`, `SUID`, `shadow`, `passwd`.
- Usa `/` para buscar en el output si estás en `less` o en tu terminal.
- Combínalo con `pspy` para detectar procesos dinámicos.

---

## ✅ Conclusión

`linpeas.sh` te da casi todo lo que necesitas para encontrar vectores locales. Saber **leer su output rápido y enfocado** puede marcar la diferencia entre perder o ganar puntos en el OSCP.
