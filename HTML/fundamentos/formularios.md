
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formularios</title>
</head>
<body>

    <h1>Aplica al trabajo</h1>


    <form>
        <!-- Ingresa nombre -->
        <label for="nombre">Ingresa tu nombre</label>
        <input type="text"  id="nombre">

        <br> <br>

        <!-- Ingresa email -->
        <label for="email">Ingresa tu Email</label>
        <input type="email"  id="email" required>

        <br> <br>

        <!-- Ingrese su país -->
        <h3>Elige tu país</h3>

        <select>
            <option value="MX">México</option>
            <option value="ARG">Argentina</option>
            <option value="BR">Brasi</option>
            <option value="NO" selected>Otro</option>
        </select>

        <!-- ¿Qué horario quieres? -->
        
        <h3>Elige el horario</h3>

        <label>
            <input type="radio" name="horario">Matutino
        </label>
        <label>
            <input type="radio" name="horario">Nocturno
        </label>
        <label>
            <input type="radio" name="horario">Mixto
        </label>

        <!-- Acepta terminos -->
        <h3>Acepta terminos</h3>

        <label>
            <input type="checkbox">Acepta terminos y condiciones
        </label>

        <!-- Deje comentarios -->
        
        <h3>Dejame tus comentarios</h3>
        <textarea cols="50" rows="5"></textarea>

        <br><br>

        <input type="submit" >
        <input type="reset" value="Reiniciar Valores">
    </form>

    <!-- maxlength="10" minlength="3"  placeholder="Ingresa tu nombre:"-->
    <!-- <input type="password" placeholder="Ingresa tu contraseña"> -->
    <!-- <input type="color"> -->
    <!-- <input type="date"> -->
    <!-- <input type="number" placeholder="Ingresa tu numero"> -->
    
</body>
</html>
```