from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

cliente = Groq(api_key=os.getenv('API_Groq'))

messages=[
    {
        "role": "system",
        "content": "Respondeme  en español de una forma relajada"
    },
]

print("Chat iniciado con la ia, Escribe 'salir' para terminar.\n")


chat_stream = cliente.chat.completions.create(
    messages=messages,
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    max_completion_tokens=1024,
    stream=True
)

print("IA: ", end="")
respuesta_completa = ""

for chunk in chat_stream:
    contenido = chunk.choices[0].delta.content
    if contenido:
        print(contenido, end="", flush=True)
        respuesta_completa += contenido

print() 

messages.append({
    "role": "assistant",
    "content": respuesta_completa
})

while True: 
    user_input = input("Tu: ")

    if user_input.lower() == 'salir':
        print("Chat Cerrado")
        break
            
        messages.append({
            "role": "user",
            "content": user_input
        })
