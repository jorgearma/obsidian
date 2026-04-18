  El flujo paso a paso

  PAGADO / CONTRA_REEMBOLSO
          │                                                                   
          │  gestor_pedidos._asegurar_picking_si_procede()
          │  → crea PickingPedido(estado=PENDIENTE, picker=NULL)              
          │    + crea todos los PickingItems (uno por línea del pedido)       
          │                                                                   
          ▼                                                                   
    [PickingPedido: PENDIENTE, sin picker]                                    
                                                                  
    ¿Quién asigna el picker?                                                  
    ┌──────────────────────────────────────────────────────┐
    │ Dashboard (manager)        Picker app                │                  
    │ reasignar_picker()         reclamar_picking()        │      
    │ → picker asignado          → picker asignado         │                  
    │ → pedido → EN_PREPARACION  → pedido → EN_PREPARACION │                  
    └──────────────────────────────────────────────────────┘                  
          │                                                                   
          ▼                                                       
    EN_PREPARACION                                                            
    [PickingPedido: EN_PROCESO, picker asignado]                  
                                                                              
          │  Picker marca items: encontrado / sin_stock / sustituido          
          │                                                                   
          │  completar_picking()                                              
          │  → pedido → PREPARADO                                 
          │  → crea Reparto(estado=PENDIENTE, repartidor=NULL)                
          │
          ▼                                                                   
    PREPARADO                                                     
    [PickingPedido: COMPLETADO]
    [Reparto: PENDIENTE, sin repartidor]                                      
   
    ¿Quién asigna el repartidor?                                              
    ┌──────────────────────────────────────────────────────┐      
    │ Dashboard (manager)        Repartidor app            │                  
    │ asignar_repartidor()       reclamar_reparto()        │      
    │ → repartidor asignado      → repartidor asignado     │                  
    │ → Reparto: ASIGNADO        → Reparto: ASIGNADO       │
    └──────────────────────────────────────────────────────┘                  
          │                                                       
          ▼                                                                   
    PREPARADO                                                     
    [Reparto: ASIGNADO, repartidor asignado]
                                                                              
          │  marcar_salida_reparto()
          │  → pedido → EN_REPARTO                                            
          │  → Reparto: EN_CAMINO                                             
          │
          ▼                                                                   
    EN_REPARTO                                                    
    [Reparto: EN_CAMINO]
                                                                              
          │  marcar_entregado()
          │  → pedido → ENTREGADO                                             
          │  → Reparto: ENTREGADO                                 
          │                                                                   
          ▼
    ENTREGADO  ✓ 