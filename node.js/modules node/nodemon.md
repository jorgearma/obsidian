**Paso 3: Inicialización del proyecto** Ejecuta `npm init` en la carpeta de tu proyecto para crear un archivo `package.json` donde se almacenarán las dependencias y configuraciones del proyecto.

**Paso 4: Instalación de Nodemon** Instala Nodemon globalmente en tu sistema o como dependencia de desarrollo en tu proyecto:

- Instalación global: `npm install -g nodemon`
- Instalación en el proyecto: `npm install nodemon --save-dev`

**Paso 5: Configuración de scripts en package.json** Abre el archivo `package.json` y agrega un script que utilizará Nodemon para ejecutar tu aplicación. Por ejemplo:

```json
"scripts": {
  "start": "nodemon app.js"
}
```

En este ejemplo, `"start"` es el nombre del script y `"nodemon app.js"` es el comando que Nodemon ejecutará para iniciar tu aplicación (reemplaza `app.js` con el nombre de tu archivo principal).