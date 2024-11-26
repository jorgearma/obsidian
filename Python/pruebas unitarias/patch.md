### **Patches**

<mark style="background: #FFF3A3A6;">se llama al archivo del test no l aubicacion original de las funciones mockeadas</mark>

El **patch** reemplaza temporalmente una función, método o clase por un mock durante el alcance de la prueba. En tu código:

- **`@patch('controllers.pago.enviar_mensaje_whatsapp')`:** Esto sustituye la función real `enviar_mensaje_whatsapp` por un mock (`mock_enviar_mensaje`). De este modo:
    
    - No se envían mensajes reales.
    - Puedes verificar las interacciones con esta función, como cuántas veces se llamó y con qué argumentos.
- **`@patch('controllers.pago.carrito_instancia')`:** Esto reemplaza la instancia real de `carrito_instancia` por un mock. Así puedes simular cualquier comportamiento del carrito.
  
  
```python
	@patch('controllers.pago.enviar_mensaje_whatsapp')
	@patch('controllers.pago.carrito_instancia')
	def test_salir_o_proceder_al_pago_sin_pedido(
		self,
		mock_carrito_instancia,
		mock_enviar_mensaje):
		
	    mock_carrito_instancia.verificar_carrito.return_value = False
	    result = self.handler.salir_o_proceder_al_pago("salir")
	    self.assertTrue(result)
	    mock_enviar_mensaje.assert_called_once_with(
	        "No tienes ningún pedido. ¡Gracias y que tenga un buen día!",
	        self.numero_cliente
	    )

```
En este caso:

1. `carrito_instancia.verificar_carrito` se reemplaza con un mock que siempre devuelve `False`, simulando un carrito vacío.
2. `enviar_mensaje_whatsapp` se reemplaza con un mock para verificar que se llama al mensaje esperado.