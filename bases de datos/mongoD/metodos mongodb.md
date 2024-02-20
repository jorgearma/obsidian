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
