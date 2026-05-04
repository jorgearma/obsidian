# Clickjacking

## Qué es

Ataque donde incrustas una página víctima en un `<iframe>` (normalmente invisible o transparente) sobre tu propia web. Superpones botones/enlaces falsos y el usuario, creyendo que interactúa con tu página, en realidad hace clic sobre la víctima.

También se llama **UI redressing**.

## Por qué es peligroso

- **En un login:** el atacante puede hacer que la víctima escriba credenciales en un formulario real de la víctima sin darse cuenta.
- **En acciones autenticadas:** si la víctima ya tiene sesión abierta en el dominio objetivo, el atacante puede provocar clics que ejecuten acciones (cambiar email, borrar cuenta, transferir, aceptar permisos OAuth...).
- **Combinado con CSRF:** se usa para saltarse confirmaciones donde el usuario tiene que pulsar "Aceptar".

## PoC mínima

```html
<!DOCTYPE html>
<html>
<body>
  <h1>Haz clic para ganar un premio</h1>
  <iframe
    src="https://objetivo.com/accion-sensible"
    width="800" height="600"
    style="opacity:0.0001; position:absolute; top:0; left:0;">
  </iframe>
</body>
</html>
```

El iframe se superpone al botón "ganar premio". El clic va realmente al iframe.

## Cómo detectarlo

### 1. Revisar headers de respuesta

```bash
curl -I https://objetivo.com -H "X-Bug-Bounty: HackerOne-siemprearmando"
```

Buscar:
- `X-Frame-Options` → si no está, **posible** vulnerable
- `Content-Security-Policy` con `frame-ancestors` → equivalente moderno

### 2. Probar con iframe real

Crear el HTML de PoC, abrirlo en el navegador y ver si la página carga dentro del iframe.

**Importante:** que carguen los headers puede no ser suficiente — hay que confirmar que **realmente** se ve y se puede interactuar.

## Headers de protección

| Header | Función |
|---|---|
| `X-Frame-Options: DENY` | Nadie puede incrustar en iframe |
| `X-Frame-Options: SAMEORIGIN` | Solo el mismo dominio puede incrustar |
| `Content-Security-Policy: frame-ancestors 'none'` | Equivalente moderno a DENY |
| `Content-Security-Policy: frame-ancestors 'self'` | Equivalente a SAMEORIGIN |
| `Content-Security-Policy: frame-ancestors https://trusted.com` | Lista blanca |

**CSP `frame-ancestors` prevalece sobre `X-Frame-Options`** en navegadores modernos.

## Mitigaciones adicionales (framebusting por JS)

Cuando los headers fallan, muchos frameworks bloquean el render desde cliente:

```javascript
if (window.top !== window.self) {
  window.top.location = window.self.location;
}
```

**Next.js** hace detección similar automáticamente: si detecta que está en un iframe no permitido, deja la página en blanco.
## Caso real — authentication.clearme.com (2026-04-19)

### Al probar la PoC real
- El iframe **cargaba en blanco**
- Next.js detecta el contexto de iframe por JavaScript y bloquea el render
- Resultado: no hay forma de que la víctima vea ni interactúe con nada

### Conclusión
**No reportable.** La ausencia de headers es un hallazgo de hardening, pero sin impacto demostrable 

## Lección clave

> **La ausencia de un header de seguridad NO es automáticamente un bug reportable.**

Para reportar clickjacking necesitas:
1. Página carga dentro de iframe (no se queda en blanco)
2. La acción del clic tiene **impacto real** (cambio de estado, credenciales, permisos...)
3. Poder demostrarlo con una PoC funcional

## Qué sí suele ser reportable

- Acción sensible en iframe que se puede accionar (transferir, borrar, cambiar email/password, aceptar OAuth scopes)
- Bypass de confirmaciones de CSRF mediante clickjacking
- Logout + login en otra cuenta controlada para phishing de credenciales


## Checklist para próximas pruebas

- [ ] Curl con `-I` para ver headers
- [ ] Buscar tanto `X-Frame-Options` como `frame-ancestors` en CSP
- [ ] Si faltan, crear PoC HTML y abrirla en navegador
- [ ] Confirmar que **realmente** se ve el contenido
- [ ] Identificar una acción con impacto dentro del iframe
- [ ] Grabar PoC en vídeo si es reportable

## Enlaces relacionados

- [[enumeracion web]]
- [[login]]
- [[metodologia]]
