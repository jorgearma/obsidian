import openai
import config

openai.api_key = config.api_key

messages=[{"role":"system","content": "eres un chaman , que ah llegado a occidente para concianciar a la gente"
                                      "hablo con frases cortas" "vivo en la luna"}]


#contexto del asistente
while True:
    content = input('pregunta lo que quieras')
    if content =="exit":
        break

    messages.append({"role": "user", "content": content})
    repuesta = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                             messages=messages)
    repuesta_conted = repuesta.choices[0].message.content
    messages.append({"role": "assistant", "content":repuesta_conted})


    print(repuesta_conted)