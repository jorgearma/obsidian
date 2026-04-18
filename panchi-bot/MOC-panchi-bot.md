# panchi-bot — Mapa de Contenido

Bot de WhatsApp para gestión de pedidos. Flask + Redis + RQ + Monei.

---

## Estado actual
- En desarrollo activo — arquitectura async con workers RQ
- Webhooks: Meta/Twilio (inbound) + Monei (pagos)
- Pendiente: lógica de cambio de dirección en página web

---

## Arquitectura y flujos

- [[flujo de  estados]] — máquina de estados completa del pedido
- [[flujo]] — flujo principal de ejecución (webhook → worker → controlador)
- [[documentacion/Untitled]] — flujo usuario no registrado
- [[documentacion/resgistrados]] — flujo usuario registrado

## Gestores y lógica

- [[managers]] — GestorPedidos, GestorEmpleado, GestorDashboard
- [[seguridad]] — guards Redis, rate-limit, dedup wamid, validación Pydantic

## Deuda técnica

- [[refatorisacion]] — 3 problemas identificados (duplicación turnos, responsabilidades mal ubicadas)
- [[riegos]] — riesgos conocidos del sistema

## Tareas pendientes

- [[tareas]] — tareas específicas de panchi-bot
- Crear lógica de cambio de dirección (guardar 2 dir, cliente elige)
- Refactorizar CRUD de turnos → GestorEmpleado

## Auditoría

- [[auditoria/promts]] — prompts de auditoría del bot

---

## Stack rápido
```
Flask · SQLAlchemy · Redis · RQ · Pydantic · spaCy · Google Maps API · Monei
WhatsApp: Meta API + Twilio
```
