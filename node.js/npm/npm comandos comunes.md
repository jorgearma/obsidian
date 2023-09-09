
```bash
# Iniciar un proyecto npm: Iniciar un nuevo proyecto y crear package.json
npm init

# Buscar un módulo: Buscar paquetes en el registro de npm
npm search <nombre-del-módulo>

# Ver información detallada de un módulo: Ver detalles sobre un paquete
npm info <nombre-del-módulo>

# Listar dependencias de desarrollo: Mostrar dependencias de desarrollo
npm list --dev

# Listar todas las dependencias: Mostrar todas las dependencias del proyecto
npm list

# Eliminar un módulo: Eliminar un paquete y sus dependencias del proyecto
npm uninstall <nombre-del-módulo>

# Actualizar un módulo: Actualizar un paquete a la última versión
npm update <nombre-del-módulo>

# Instalar todas las dependencias: Instalar todas las dependencias de package.json
npm install

# Instalar un módulo globalmente: Instalar un paquete globalmente en el sistema
npm install -g <nombre-del-módulo>

# Instalar un módulo: Instalar un paquete y sus dependencias en el proyecto
npm install <nombre-del-módulo>

```

# init

**Comando:** `npm init`

**Uso:** Este comando se ejecuta en el directorio raíz de tu proyecto a través de la línea de comandos. Debes tener Node.js y npm instalados en tu sistema para utilizar este comando.

**Acción:** Al ejecutar `npm init`, se iniciará un proceso interactivo que te guiará a través de la creación del archivo `package.json`. Durante este proceso, se te harán una serie de preguntas sobre la configuración de tu proyecto, y luego se generará el archivo `package.json` en base a tus respuestas.

**Preguntas comunes durante `npm init`:**

1. **package name:** El nombre del paquete (nombre de tu proyecto).
2. **version:** La versión inicial del paquete (generalmente se inicia con "1.0.0").
3. **description:** Una descripción breve del proyecto.
4. **entry point:** El archivo principal de tu aplicación (por lo general, `index.js`).
5. **test command:** El comando para ejecutar pruebas.
6. **git repository:** La URL de tu repositorio Git (opcional).
7. **keywords:** Palabras clave relacionadas con tu proyecto (opcional).
8. **author:** Tu nombre o el nombre de tu equipo.
9. **license:** La licencia bajo la cual deseas distribuir el proyecto.