1. **Global**:
    
    - Objeto que representa el ámbito global en Node.js.
    - Variables declaradas sin var, let o const se asignan automáticamente a este objeto.
    - Evita el exceso de variables globales para prevenir colisiones y problemas de mantenimiento.
2. **Console**:
    
    - Objeto para imprimir mensajes en la consola.
    - Métodos como console.log(), console.error(), console.warn() para mostrar información durante la ejecución.
3. **Process**:
    
    - Objeto global para controlar el proceso actual en Node.js.
    - Propiedades:
        - process.env: Acceso a variables de entorno.
        - process.argv: Acceso a argumentos de línea de comandos.
    - Métodos:
        - process.exit(): Finaliza la ejecución del proceso.
4. **__dirname y __filename**:
    
    - Variables globales con rutas absolutas del directorio y archivo actual.
5. **setTimeout() y setInterval()**:
    
    - Funciones globales para programar la ejecución después de cierto tiempo o en intervalos.
    - setTimeout(callback, tiempo): Ejecuta callback después de un tiempo específico.
    - setInterval(callback, intervalo): Ejecuta callback en intervalos regulares.
6. **Require()**:
    
    - Función fundamental para importar módulos y archivos en Node.js.