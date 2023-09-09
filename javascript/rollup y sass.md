1. iniciamos
```bash
npm init -y
Wrote to /home/kali/Desktop/js_curso/galeria/package.json:

{
  "name": "galeria",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```
esto crea  package.json

2. lo instalamos en la dependencia
```bash
npm install -D rollup

added 1 package, and audited 2 packages in 573ms

found 0 vulnerabilities
```

3. creamos la carperta  .rollup.config.js
```bash
echo "export default {
    input: 'src/main.js',
    output: {
        file: 'bundle.js', #modificar
        format: 'cjs'
    }
};" > rollup.config.js

```

4. creamos la carperta src con el archivo index.js
```bash
mkdir src && touch src/index.js
```

5. para trabajar con export default necesitamos modificar  package.json

 "type": "module",
 "build":"rollup --watch --config"
```json
{
"type": "module",   /* linea agregar*/
"name": "galeria",
"version": "1.0.0",
"description": "",
"main": "index.js",
"scripts": {
"test": "echo \"Error: no test specified\" && exit 1",
"build":"rollup --watch --config" /*linea a agregar*/
},
"keywords": [],
"author": "",
"license": "ISC",
"devDependencies": {
"rollup": "^3.25.1"
}
}
```

6. ya esta listo para correr
```bash
npm run build
```


# Sas

```shell
npm install sass
```

ponemos el comando sass en package.json
```json
"scripts": {

"test": "echo \"Error: no test specified\" && exit 1",

"sass": "sass --watch --style=compressed sass/index.scss public/bundle.css",

"build": "rollup --watch --config"

},
```

```shell
npm run sass 
```