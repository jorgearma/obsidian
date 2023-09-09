
```js
import jwt from "jsonwebtoken";
import config from "../config";
import User from "../models/user";

// Middleware para autenticación y verificación de tokens JWT
export const verifytoken = async (req, res, next) => {
    // Obtener el token del encabezado de la solicitud
    const token = req.headers["x-acess-token"];

    // Si no hay token, devolver un error 403
    if (!token) {
        return res.status(403).json({ message: "No token provided" });
    }

    try {
        // Verificar y decodificar el token usando la clave secreta
        const decoded = jwt.verify(token, config.SECRET);
        
        // Extraer el ID del usuario del token y agregarlo a la solicitud
        req.id = decoded.id;

        // Buscar al usuario en la base de datos usando el ID del token
        const user = await User.findById(req.id, { password: 0 });

        // Si no se encuentra el usuario, devolver un error 404
        if (!user) {
            return res.status(404).json({ message: "No user found" });
        }
        next();
    } catch (error) {
        return res.status(401).json({ message: "Invalid token" });
    }
};

```