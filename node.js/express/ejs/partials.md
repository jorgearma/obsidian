**Parciales en EJS :**

Los parciales en EJS te permiten dividir tus vistas en componentes reutilizables, lo que facilita la creación de interfaces consistentes y reduce la duplicación de código HTML en tus archivos de plantillas.

1. **Creación de un Parcial:**
    
    - Crea una carpeta llamada "partials" dentro de tu carpeta "views".
    - Dentro de la carpeta "partials", crea archivos EJS que contengan fragmentos de HTML reutilizables, como encabezados, pies de página, menús, etc.
2. **Uso de Parciales:**
    
    - Para incluir un parcial en una vista, utiliza la función `<%- include() %>` de EJS, pasando la ruta relativa al parcial que deseas incluir.
        
    - Por ejemplo, si tienes un parcial llamado "_header.ejs" dentro de la carpeta "partials", puedes incluirlo en una vista con:

```ejs
<%- include('./partials/_header') %>

```

**Variables en Parciales:**

- Puedes pasar variables a tus parciales utilizando el mismo mecanismo que en las vistas principales.
    
- Por ejemplo, si tienes un parcial de encabezado que necesita mostrar el nombre de usuario, puedes pasar esa variable al parcial:
```ejs
<%- include('./partials/_header', { username: 'Usuario123' }) %>

```

Reutilización y Mantenimiento:

Los parciales permiten reutilizar componentes en diferentes vistas, lo que mejora la consistencia y facilita el mantenimiento.
Si necesitas realizar cambios en un componente, solo tienes que modificar el parcial en un solo lugar, en lugar de actualizar cada instancia individualmente.
Los parciales son especialmente útiles para simplificar y organizar vistas en proyectos web más grandes y complejos, lo que resulta en un código más limpio y fácil de mantener. 