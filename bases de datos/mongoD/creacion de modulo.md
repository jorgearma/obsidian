
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
