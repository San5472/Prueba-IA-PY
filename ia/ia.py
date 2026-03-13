import torch
import torch.nn as nn
import torch.optim as optim

with open('texto.txt', 'r', encoding='utf-8') as f:
    texto = f.read();

chars = sorted(list(set(texto)))
vocab_size = len(chars)
chat_to_int = {ch: i for i, ch in enumerate(chars)}
int_to_char = {i: ch for i, ch in enumerate(chars)}

datos = torch.tensor([chat_to_int[c] for c in texto], dtype=torch.long)

class IA(nn.Module): 
    def __init__(self, vocab_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, 64)
        self.lstm = nn.LSTM(64, 256, batch_first=True)
        self.fc = nn.Linear(256, vocab_size)

    def forward(self, x, h):
        x = self.embedding(x)
        out, h = self.lstm(x, h)
        out = self.fc(out)
        return out, h
        
modelo = IA(vocab_size)
optimizer = optim.Adam(modelo.parameters(), lr=0.002)
criterion = nn.CrossEntropyLoss()

def entrenar():
    modelo.train()
    h = None
    
    for i in range(5000):
        idx = torch.randint(0, len(datos) -20, (1,))
        x = datos[idx:idx+20].unsqueeze(0)
        y = datos[idx+1:idx+21].unsqueeze(0)

        optimizer.zero_grad()
        output, h = modelo(x, None)
        loss = criterion(output.transpose(1, 2), y)
        loss.backward()
        optimizer.step()

        if i % 100 == 0:
            print(f"progreso: {i}/500 - Error: {loss.item():.4f}")

    print("Arrancando entrenamiento")
    entrenar();
    print("Entrenamiento completado")


## generar respuesta

def generar_respuesta(modelo, inicio_frase, longitud=50):
    modelo.eval() # se coloca la ia en modo de lectura
    with torch.no_grad():
        input_seq = torch.tensor([chat_to_int[c] for c in inicio_frase]).unsqueeze(0)
        h = None
        resultado = inicio_frase
        
        for _ in range(longitud):
            output, h = modelo(input_seq, h)
            # Tomamos la letra con mayor probabilidad
            prob = torch.softmax(output[0, -1] / 0.7, dim=0)
            proximo_char_idx = torch.multinomial(prob, 1).item()
            
            letra = int_to_char[proximo_char_idx]
            resultado += letra
            
            # Entrada para la siguiente letra
            input_seq = torch.tensor([[proximo_char_idx]])
            
        return resultado
    
print("IA Comenzando")
while True:
        usuario = input("Escribe tu pregunta (o 'salir'): ")

        if usuario.lower() == "salir": 
            break 

        try: 
            respuesta = generar_respuesta(modelo, usuario)
            print(f"IA: {respuesta}")
        except KeyError:
            print("IA: Usastes una letra que no conozco")