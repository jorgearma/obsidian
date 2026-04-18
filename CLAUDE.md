# Contexto de Jorge — Segundo Cerebro

## Quién soy
Desarrollador Python en crecimiento, apuntando a nivel **junior-medio competente**.
Trabajo principalmente en español. Intereses: desarrollo backend, ciberseguridad, automatización e IA.

## Stack técnico actual
- **Backend**: Python, Flask, SQLAlchemy, Pydantic, RQ (Redis Queue)
- **Infraestructura**: Redis, PostgreSQL/SQLite, Docker básico
- **APIs externas**: WhatsApp (Meta + Twilio), Monei (pagos), VirusTotal, AbuseIP
- **Frontend básico**: JavaScript, HTML, CSS
- **Cloud**: Azure (aprendiendo)
- **Ciberseguridad**: nmap, subfinder, amass, scapy, openssl, paramiko, impacket

## Proyecto principal: panchi-bot
Bot de WhatsApp para gestión de pedidos de una tienda.

**Arquitectura:**
- Webhook HMAC (Meta/Twilio) → RQ async worker → `enrutar_mensaje()`
- Máquina de estados por pedido: `PENDIENTE → ENLACE → CONFIRMANDO_PAGO → PAGADO → EN_PREPARACION → EN_REPARTO → ENTREGADO`
- Guards anti-race: lock Redis 10s para doble pedido, rate-limit 4s anti-spam, dedup por wamid
- Pago via webhook Monei (HMAC separado)
- Validación de inputs con Pydantic

**Archivos clave de referencia en este vault:**
- `panchi-bot/documentacion/` — flujos detallados
- `panchi-bot/flujo de estados.md` — máquina de estados
- `panchi-bot/managers.md` — gestores principales
- `panchi-bot/seguridad.md` — guards y validaciones

## Aprendizaje activo
- **Python**: Completando fundamentos hacia junior-medio (testing, módulos, decoradores, logging)
- **Ciberseguridad**: Recon (DNS, nmap scripts, subfinder/amass), análisis de red (scapy), protocolos (SMB, SSH)
- **Inglés**: Traducción de frases, vocabulario técnico
- **IA/Agentes**: Explorando arquitecturas multi-agente (ver `claude/agentes.md`)

## Cómo ayudarme mejor
- Responder en **español** siempre
- Código Python: preferir claridad sobre brevedad; nombrar bien las cosas
- En ciberseguridad: contexto es CTF, scripts personales de recon, aprendizaje — no ataques reales
- Cuando toco `panchi-bot`: recordar la arquitectura async RQ + los guards Redis antes de sugerir cambios
- Señalar cuando algo que hago podría romperse en producción (race conditions, manejo de errores, etc.)

## Metas a mediano plazo
1. Llevar `panchi-bot` a producción estable
2. Consolidar nivel junior-medio en Python
3. Progresar en ciberseguridad (recon → análisis de vulnerabilidades)
4. Explorar desarrollo de agentes IA con Claude API
