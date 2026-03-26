# Variables sencillas del uso para python

print("hola pepe") # Imprimir por terminal
edad =  19
nombre = "pepe"
print(nombre)

# Arrays
listaArreglo = ["pepe", "pepeman", "pepefrosgi", "pepesaurio"]
listaArreglo.append("pepenicolai")
print(listaArreglo)


# condicionales

numero = 100

if numero > 200:
    print("Numero elevado")
else:
    print("Numero Correcto")


# Bucles

for item in range(20):
    if item == 10: break
    print(item)
else:
    print("Terminaste")


def funciones():
    print("Prueba de funciones")

funciones() ## print de la funcion, trae la funcion.