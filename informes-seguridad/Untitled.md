# 🛠️ Reporte de fallo: Incoherencia en el flujo de preguntas del bot Mia

## **Resumen**

Se ha detectado un fallo crítico en el flujo de interacción del bot **Mia** durante la sección de presentación de proyectos. Después de finalizar la grabación de la presentación, el bot inicia preguntas sobre la transcripción del audio. Sin embargo, **si no se detecta audio o la transcripción falla**, el bot sigue su flujo sin contexto, haciendo preguntas incoherentes o incorrectas.

---

## **Descripción del fallo**

- La lógica de grabación de audio y transcripción se encuentra en el **frontend**, en archivos de los que no dispongo de acceso directo.
  - No hay control sobre **ausencia de audio** (`W` vacío).
  - No hay control sobre **fallos de transcripción** (errores en la llamada a la API o respuesta vacía).
  - En estos casos, el bot **continúa haciendo preguntas** como si hubiera transcripción válida.

---
## **Ejemplo de fallo detectado**

  ``` bash
  "group": {
    "ficha": "4343",
    "is_evaluated": true,
    "department": "Bogotá",
    "raw_conversation": "[{\"type\":\"user\",\"content\":\"No se grabó audio.\"},{\"type\":\"model\",\"content\":\"Muy bien. Entendí que el proyecto está relacionado con IoT. Ahora, voy a hacerles tres preguntas para conocer mejor el desarrollo. La primera pregunta es ¿cuál fue la estructura del proyecto que implementaron?\"},{\"type\":\"user\",\"content\":\"Estoy listo(a) para responder la siguiente pregunta\"},{\"type\":\"model\",\"content\":\"Muy bien. La segunda pregunta es: ¿cómo llevaron a cabo la gestión y ejecución de este proyecto?\"}....
  }
```

**Observaciones sobre el fallo:**

- El campo `"raw_conversation"` muestra que **el usuario no grabó audio** (`"No se grabó audio."`).
    
- A pesar de esto, el bot hace **preguntas como si hubiera una presentación válida**.
    
- Esto genera incoherencia en la conversación y confusión en los participantes.
## **Impacto**

- Preguntas del bot incoherentes o sin contexto.
- Experiencia de usuario confusa.
- Riesgo de que la presentación quede incompleta o invalidada por falta de datos.
- Posible impacto en evaluación de proyectos automatizados.

---

## **Posibles causas**

1. La variable que contiene el audio grabado (`U.getRecordedAudio()`) puede ser `null` o `undefined`.
2. La llamada a la API de transcripción (`POST /transcribe`) puede fallar por:
   - Problemas de red.
   - Formato incorrecto del audio.
   - Fallos internos del servicio de transcripción.
3. No existe lógica en frontend para **validar la transcripción antes de continuar** con el flujo de preguntas.

---

## **Posibles soluciones (requieren cambios en frontend)**

1. **Validar la existencia de audio antes de enviar a transcripción**

  ```js
   const audioBlob = U.getRecordedAudio();
   if (!audioBlob) {
       alert("No se detectó audio. Por favor, grabe la presentación.");
       return; // Detener flujo
   }
   
   const transcription = await OB(audioBlob);
if (!transcription || transcription.trim() === "") {
    alert("La transcripción no generó contenido válido. Reiniciando sesión.");
    initializePresentation(); // Reinicia la presentación desde el inicio
    return;
}
```



2. **Mecanismo de reintento**
    
    - Permitir un máximo de 2-3 intentos si la transcripción falla.
        
    - Mostrar mensajes claros al usuario sobre el fallo y la acción que debe tomar.
        
3. **Bloquear preguntas del bot hasta tener transcripción válida**
    
    - Solo permitir que el bot comience su flujo de preguntas si existe texto transcrito.
        
    - Evitar llamadas a funciones que dependen del contenido transcrito si este está vacío.
        

---

## **Recomendación**

- Implementar validaciones en frontend para:
    
    1. Detectar ausencia de audio.
        
    2. Manejar fallos de transcripción.
        
    3. Reiniciar o reintentar el flujo si no hay datos válidos.
        
- Esto asegurará que **el bot Mia solo haga preguntas coherentes**, evitando errores de flujo y mejorando la experiencia del usuario.
    

---

**Observación:**  
Como el frontend actual no está disponible, estas soluciones son propuestas teóricas basadas en la revisión de la lógica de transcripción observada. La implementación real deberá adaptarse al código y librerías usadas en la aplicación.
