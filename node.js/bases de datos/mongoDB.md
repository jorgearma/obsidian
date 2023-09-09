```js
// Importa el módulo mongoose
import mongoose from 'mongoose';

// URL de conexión a la base de datos, en este caso a "jorge_api" en localhost
const dbUrl = 'mongodb://127.0.0.1:27017/jorge_api';

// Opciones de configuración de la conexión
const dbOptions = {
    useNewUrlParser: true,       // Usa el nuevo analizador de URL
    useUnifiedTopology: true,   // Utiliza el nuevo motor de topología
};

// Intenta conectarte a la base de datos
mongoose.connect(dbUrl, dbOptions)
    .then(() => {
        console.log('Connected to the database');
    })
    .catch((error) => {
        console.error('Error connecting to the database:', error);
    });

// Manejador de eventos para la conexión exitosa
mongoose.connection.on('connected', () => {
    console.log('Mongoose default connection is open');
});

// Manejador de eventos para la conexión cerrada
mongoose.connection.on('disconnected', () => {
    console.log('Mongoose default connection is disconnected');
});

// Manejador de eventos para errores de conexión
mongoose.connection.on('error', (err) => {
    console.error(`Mongoose default connection error: ${err}`);
});

// Cierre de la conexión si el proceso Node.js se cierra
process.on('SIGINT', () => {
    mongoose.connection.close(() => {
        console.log('Mongoose default connection disconnected through app termination');
        process.exit(0);
    });
});

```


## creacion de modulo

```js
import { Schema, model } from "mongoose";

const productschema = new Schema({
    // Definimos los campos del Schema
    name: String,
    category: String,
    price: Number,
    imgURL: String
}, {
    // Configuraciones adicionales del Schema
    timestamps: true,
    versionKey: false
});

export default Product;

```

## esquema de usuario 
```js
// Importar las bibliotecas necesarias
import mongoose from "mongoose";

// Conectar a la base de datos MongoDB (asegúrate de que tienes una instancia de MongoDB en ejecución)
mongoose.connect('mongodb://localhost/tu_base_de_datos', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// Definir el esquema de usuario
const userSchema = mongoose.Schema({
    username: {
        type: String,
        required: true,
        trim: true
    },
    email: {
        type: String,
        required: true,
        trim: true,
        unique: true
    },
    password: {
        type: String,
        required: true
    }
});

// Crear el modelo de usuario
const User = mongoose.model('User', userSchema);

// Crear un nuevo usuario
const newUser = new User({
    username: 'ejemplo',
    email: 'ejemplo@email.com',
    password:

```
## metodos mongoDB

 Crear un nuevo documento
 
```js
const newProduct = new Product({ name: "Producto Nuevo", category: "Electrónica", price: 599, imgURL: "imagen.jpg" });
```
 Guardar el nuevo documento en la base de datos
 
```js
const savedProduct = await newProduct.save();
```

 Buscar todos los documentos que cumplen con ciertas condiciones
 
```js
const allProducts = await Product.find({ category: "Electrónica" });
```

 Buscar el primer documento que cumple con ciertas condiciones
 
```js
const firstProduct = await Product.findOne({ category: "Ropa" });
```

 Encontrar un documento por su ID
 
```js
const productById = await Product.findById("id-del-producto");
```

 Actualizar un documento por su ID y obtener el documento actualizado
 
```js
const updatedProduct = await Product.findByIdAndUpdate("id-del-producto", { price: 699 }, { new: true });
```

 Eliminar un documento por su ID y obtener el documento eliminado
 
```js
const deletedProduct = await Product.findByIdAndDelete("id-del-producto");
```

 Contar la cantidad de documentos que cumplen con ciertas condiciones
 
```js
const productCount = await Product.countDocuments({ category: "Electrónica" });
```

 Devolver una lista de valores únicos para un campo específico que cumple con ciertas condiciones
 
```js
const uniqueCategories = await Product.distinct("category", { price: { $gt: 500 } });
```


```js

```
