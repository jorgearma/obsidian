  CASO 1: Sin pedido activo                                                                                           
      → _iniciar_pedido_y_enviar_menu()                                                                               
          ├─ LOCK Redis (pedido_lock:<numero>, TTL 10s) — guard anti-doble pedido                                     
          ├─ gestor_pedidos.iniciar_pedido(...)       → estado PENDIENTE en DB                                        
          └─ _enviar_bienvenida_menu()                                                                                
                                                                                                                      
  CASO 2: Estado PENDIENTE                                                                                            
      → procesar_pedido(mensaje, numero, id_pedido, usuario_datos)   [controllers/pedido.py]                          
          ├─ Valida con Pydantic (PedidoInput)                                                                        
          ├─ es_pregunta() → respuesta genérica                                                                       
          ├─ Busca coincidencia en menu{} por texto o código                                                          
          │   ├─ opción "Tienda online"                                                                               
          │   │   ├─ Guard: pedido sigue en PENDIENTE (re-lee DB)                                                     
          │   │   ├─ generar_enlace() → token Redis con TTL                                                           
          │   │   └─ gestor_pedidos.iniciar_enlace() → estado ENLACE                                                  
          │   └─ otra opción → devuelve texto de respuesta                                                            
          └─ _enviar_respuesta_pedido(mensaje)                                                                        
                                                                                                                      
  CASO 3: Estado ENLACE o ENLACE2                                                                                     
      → pedido_activo.enlace existe?                              
          ├─ No  → _enviar_enlace_caducado()                                                                          
          └─ Sí  → _enviar_enlace_pedido(enlace)                                                                      
                                                                                                                      
  CASO 4: Estado CONFIRMANDO_PAGO                                                                                     
      → _enviar_enlace_pago(pedido_activo.enlace)   (reenvía link de pago Monei)                                      
                                                                                                                      
  CASO 5: PAGADO / CONTRA_REEMBOLSO / EN_PREPARACION / PREPARADO / EN_REPARTO                                         
      → _enviar_estado_en_curso(pedido_activo)       [mensajes_registrados_notifier.py]                               
          ├─ PAGADO           → "pago confirmado, preparando"                                                         
          ├─ CONTRA_REEMBOLSO → "confirmado, pago en entrega"                                                         
          ├─ EN_PREPARACION / PREPARADO → "en preparación"                                                            
          └─ EN_REPARTO                                                                                               
              ├─ con repartidor → nombre + teléfono del repartidor                                                    
              └─ sin repartidor → mensaje genérico                                                                    
                                                                  
  CASO 6: Estado no contemplado (ENTREGADO, CANCELADO, REEMBOLSADO, desconocido)                                      
      → _enviar_error_generico()   + warning en log               
                                                                                                                      
  5. Flujo paralelo: pago Monei (no pasa por mensajes_registrados)                                                    
                                                                                                                      
  POST /webhook/monei                                                                                                 
      ├─ verifica HMAC Monei                                      
      ├─ status == SUCCEEDED → gestor_pedidos.procesar_pago_confirmado()                                              
      │                              → estado PAGADO en DB
      └─ enviar_mensaje_whatsapp directamente (sin notifier, inline en inbound_whatsapp.py)                           
                                                                                                                      
  ---                                                                                                                 
  Resumen de guardias                                                                                                 
                                                                                                                      
  ┌────────────────────────┬───────────────────────────────┬────────────────────────────────────────┐
  │        Guardia         │             Dónde             │             Protege contra             │                 
  ├────────────────────────┼───────────────────────────────┼────────────────────────────────────────┤
  │ wamid deduplicación    │ encolar_mensaje               │ Duplicados de Meta                     │
  ├────────────────────────┼───────────────────────────────┼────────────────────────────────────────┤
  │ Rate-limit 4s Redis    │ enrutar_mensaje               │ Spam / doble envío                     │                 
  ├────────────────────────┼───────────────────────────────┼────────────────────────────────────────┤
  │ Lock pedido 10s Redis  │ _iniciar_pedido_y_enviar_menu │ Crear dos pedidos simultáneos          │                 
  ├────────────────────────┼───────────────────────────────┼────────────────────────────────────────┤                 
  │ Guard estado PENDIENTE │ procesar_pedido (re-lee DB)   │ Race condition antes de generar enlace │
  ├────────────────────────┼───────────────────────────────┼────────────────────────────────────────┤                 
  │ Validación Pydantic    │ procesar_pedido               │ Inputs malformados                     │
  └────────────────────────┴───────────────────────────────┴────────────────────────────────────────┘                 