**`src/routes/products.routes.js`**:
importa las funciones de controllers 
```js routes
import { Router } from 'express';
import * as productsCtrl from '../controllers/products.controller.js'; // Importar el controlador

const router = Router();

router.post('/', productsCtrl.createProduct);
router.get('/', productsCtrl.getProducts);
router.get('/:producId', productsCtrl.getProducById);
router.put('/:producId', productsCtrl.updateProducByid);
router.delete('/:productId', productsCtrl.deletePraducById);

export default router;

```

**`src/controllers/products.controller.js`**:
defina las funciones para que se ultilicen desde routes
```js
// Las importaciones aquí pueden variar según cómo estén organizadas tus funciones

// Función para crear un producto
export const createProduct = async (req, res) => {
    // Lógica para crear un producto
};

// Función para obtener todos los productos
export const getProducts = async (req, res) => {
    res.json('get products');
};

// Función para obtener un producto por su ID
export const getProducById = async (req, res) => {
    // Lógica para obtener un producto por su ID
};

// Función para actualizar un producto por su ID
export const updateProducByid = async (req, res) => {
    // Lógica para actualizar un producto por su ID
};

// Función para eliminar un producto por su ID
export const deletePraducById = async (req, res) => {
    // Lógica para eliminar un producto por su ID
};

```

**`src/app.js`**:
pagina principal
```js
import express from "express";
import morgan from "morgan";
import pkg from "../package.json"; // Importar el package.json

import productsRoutes from './routes/products.routes.js'; // Importar las rutas de productos

// Crear una nueva instancia de Express
const app = express();

// Configurar la información del package.json en la aplicación
app.set('pkg', pkg);

// Usar el middleware Morgan para el registro de solicitudes
app.use(morgan('dev'));

// Ruta de inicio que devuelve información del package.json
app.get('/', (req, res) => {
    res.json({
        name: app.get('pkg').name,
        author: app.get('pkg').author,
        description: app.get('pkg').description,
        version: app.get('pkg').version,
    });
});

// Usar las rutas de productos
app.use('/products', productsRoutes);

export default app;

```