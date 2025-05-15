# 🔐 SUID Binaries Enumeration Cheatsheet

Estas búsquedas son útiles durante auditorías de seguridad o CTFs para encontrar **binarios con el bit SUID** activo, lo cual puede ser una **vulnerabilidad crítica** si se abusa correctamente.

## 🔍 ¿Qué es el bit SUID?

El bit SUID (Set User ID) permite que un binario se ejecute con los privilegios del **propietario del archivo**, en lugar del usuario que lo ejecuta. Si el propietario es **root**, el binario se ejecutará con privilegios de root.

---

## 📂 Comandos para encontrar binarios con SUID

### 1. Mostrar archivos con SUID activos y detalles:

```bash
find / -perm -4000 -type f -exec ls -la {} 2>/dev/null \;
```

🔹 **Explicación:**

- `find /`: Busca desde el directorio raíz.
- `-perm -4000`: Encuentra archivos con el bit SUID activo.
- `-type f`: Limita la búsqueda a archivos (no directorios).
- `-exec ls -la {}`: Muestra detalles del archivo encontrado.
- `2>/dev/null`: Suprime errores (por ejemplo, permisos denegados).

---

### 2. Mostrar binarios SUID específicamente de `root`:

```bash
find / -uid 0 -perm -4000 -type f 2>/dev/null
```

🔹 **Explicación:**

- `-uid 0`: Solo archivos cuyo propietario es el usuario `root`.
- Lo demás igual que en el primer comando.

---

## 🛠 ¿Qué hacer con estos binarios?

Consulta si alguno de estos binarios es explotable:

- Usa [GTFOBins](https://gtfobins.github.io) para ver si alguno permite escalada de privilegios.
- Verifica si puedes escribir sobre variables de entorno que afecten al binario.
- Mira si puedes aprovechar scripts que ejecuta.

---

## 📘 Referencias útiles

- [GTFOBins](https://gtfobins.github.io)
- [PayloadsAllTheThings - SUID](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Linux%20Privilege%20Escalation/SUID.md)