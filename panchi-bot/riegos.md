1. managers/pedidos/workflow_mixin.py — RIESGO ALTO                                                           
                                                                                                                
  Es el núcleo del flujo de pago. Tres cosas a verificar antes de salir:                                        
                                                                                                                
  - procesar_pago_confirmado vs registrar_pago: son dos métodos distintos. El primero hace la transición de     
  estado + inserta el Pago en un único commit atómico. El segundo solo inserta el registro de pago, sin cambiar
  estado. registrar_pago no se llama desde ningún sitio activo — es código muerto, pero si alguien lo llama por 
  error duplicarías el registro de pago sin mover el estado.                                                  
  - Validación de importe: si el importe de Monei no coincide con pedido.Total, el pago se rechaza
  silenciosamente (return False). Verifica que el Total en BD se guarda en euros (no en céntimos) porque Monei  
  devuelve céntimos y el código divide por 100 en inbound_whatsapp.py antes de pasar a procesar_pago_confirmado.
  - _asegurar_picking_si_procede: crea el PickingPedido cuando el pedido entra en PAGADO/CONTRA_REEMBOLSO. Si ya
   existe uno, lo ignora. Correcto. Pero si el flush() dentro del _set_estado falla, la excepción se propaga    
  antes del commit y el rollback lo limpia todo. OK.
                                                                                                                
  ---                                                                                                         
  2. services/inbound_whatsapp.py — RIESGO MEDIO-ALTO

  Punto de entrada de todos los mensajes y pagos.

  - procesar_pago_monei — notificación sin try/except: tras el self.session.commit() del pago, llama a          
  enviar_mensaje_whatsapp(mensaje, customer_phone) sin protección. Si la API de WhatsApp falla, Flask devuelve
  500 a Monei → Monei reintenta el webhook. La idempotencia por referencia_externa protege de doble             
  procesamiento, pero el cliente no recibe la confirmación hasta que la API de WhatsApp funcione. El pedido   
  queda en PAGADO correctamente en BD — no hay pérdida de datos, pero sí pérdida de notificación.
  - Formato del teléfono: el customer_phone que llega del webhook de Monei es exactamente lo que se guardó al
  crear el pago (whatsapp:+34XXXXXXXXX), así que _enviar_meta y Twilio lo manejan correctamente. No hay bug     
  aquí.
                                                                                                                
  ---                                                                                                         
  3. blueprints/api/cart.py — RIESGO BAJO
                                                                                                                
  - cambiar_estado_a_enlace: el guard if pedido.Estado == CONFIRMANDO_PAGO → 400 es correcto (no revertir un
  pago en proceso). Para cualquier otro estado, transicion_valida_pedido dentro del mixin bloqueará las         
  transiciones inválidas. El error de que el mensaje tiene "error'" (apóstrofe suelto) es un bug cosmético sin
  impacto funcional.                                                                                            
  - volver_al_menu: usa data.get("userID") (D mayúscula) para la validación de identidad. Asegúrate de que el 
  frontend envía exactamente ese campo con esa capitalización.                                                  
  
  ---                                                                                                           
  4. blueprints/api/tracking.py — RIESGO BAJO                                                                 
                                                                                                                
  Ruta de solo lectura. Lo único a verificar es que gestor_pedidos.obtener_seguimiento(redis_id) existe y
  devuelve el formato esperado.                                                                                 
                                                                                                              
  ---                                                                                   