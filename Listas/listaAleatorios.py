from random import randint

N = 10
numeros = []

for i in range(N):
    numeros.append(randint(1,10))

print(numeros)
pregunta = int(input("Dame un número : "))
enc = False
i = 0
#mientras no encuentro lo que busco Y tengo dónde buscar
while not enc and i < len(numeros):
    if numeros[i] == pregunta:
        print("El número ", pregunta, " está en la posición ", i)
        enc = True
    else:
        i = i + 1

if enc:
    numeros.remove(pregunta)
    print("El listado se queda así tras eliminar el número : ", numeros)
else:
    print("No se ha encontrado el número en la lista")
