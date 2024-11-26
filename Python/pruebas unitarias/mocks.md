### **Mocks**

Un **mock** es un objeto simulado que reemplaza a uno real en tus pruebas. En este código, estás utilizando `mock_enviar_mensaje` y `mock_carrito_instancia` como mocks para simular:

```python
@patch('controllers.pago.enviar_mensaje_whatsapp')

def test_preguntar_metodo_pago(self, mock_enviar_mensaje):

	self.handler.preguntar_metodo_pago()
	
	mock_enviar_mensaje.assert_called_once_with(
	
	"🔷¿como te gustaria pagar?🔷\n 👇 Escribe 👇 \n\n▪️ *Efectivo* *Tarjeta* ▪️",
	
	self.numero_cliente

)
```