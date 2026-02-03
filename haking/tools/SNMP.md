# SNMP Cheatpage 

## Qué es SNMP
SNMP (Simple Network Management Protocol) expone información interna del sistema.
Una mala configuración implica **fuga crítica de información**.

Puerto típico:
- UDP 161

---

## Versiones
- SNMPv1 / SNMPv2c → **INSEGURAS** (community string en texto claro)
- SNMPv3 → autenticada y cifrada

En OSCP / HTB: **SNMPv2c + public** es lo más común.

---

## Herramienta principal
`snmpbulkwalk`

Enumeración rápida y masiva de OIDs (mejor que `snmpwalk` en v2c).

Sintaxis:
```bash
snmpbulkwalk -v2c -c <community> <IP> <OID>
```

---

## OID raíz (PUNTO CLAVE)
❗ No existe una bandera para “empezar desde la raíz”.

Para enumerar **todo el árbol MIB**, debes indicar explícitamente el OID raíz:

```bash
.1
```

Ejemplo:
```bash
snmpbulkwalk -v2c -c public 10.129.228.106 .1
```

Alternativa equivalente:
```bash
snmpbulkwalk -v2c -c public 10.129.228.106 .
```

Si no indicas `.1`, **NO se enumera todo el árbol**.

---

## Mostrar OIDs numéricos (MUY IMPORTANTE)
Para evitar resolución de MIBs y facilitar parsing automático:

```bash
-On
```

Ejemplo recomendado:
```bash
snmpbulkwalk -v2c -c public -On 10.129.228.106 .1
```

---

## Ramas CRÍTICAS para OSCP

### Información del sistema
OID:
```text
1.3.6.1.2.1.1
```

Buscar:
- Hostname
- Sistema operativo
- Uptime
- Contact / Location

---

### Procesos en ejecución (🔥 GOLD)
OID:
```text
1.3.6.1.2.1.25.4.2.1
```

Buscar:
- Servicios internos
- Scripts
- Rutas absolutas a binarios
- Procesos que no aparecen en nmap

---

### Software instalado
OID:
```text
1.3.6.1.2.1.25.6.3.1
```

Buscar:
- Versiones vulnerables
- Software legacy
- Aplicaciones internas

---

### Usuarios / sesiones
OID:
```text
1.3.6.1.2.1.25.1.5
```

Buscar:
- Usuarios reales del sistema
- Sesiones activas

---

### Interfaces de red
OID:
```text
1.3.6.1.2.1.2
```

Buscar:
- Interfaces internas
- IPs adicionales
- VLANs / bridges

---

## Flujo recomendado (OSCP)
1. Detectar UDP/161 abierto
2. Probar community string (`public`)
3. Enumerar todo el árbol:
```bash
snmpbulkwalk -v2c -c public -On <IP> .1
```
4. Repetir por ramas clave para reducir ruido
5. Correlacionar con Nmap y exploits

---

## Comando que DEBES memorizar
```bash
snmpbulkwalk -v2c -c public -On <IP> .1
```

Si este comando devuelve información → **el host está filtrando datos críticos**.