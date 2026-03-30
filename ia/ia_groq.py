from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

cliente = Groq(api_key=os.getenv('API_Groq'))

response = cliente.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "hola pepe"}]
    
)

print(response.choices[0].message.content)