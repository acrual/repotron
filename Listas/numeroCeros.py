from random import randint

def numeroCeros(lista):

    count = 0
    for i in range(len(numeros)):
        if lista[i] == 0:
            count = count + 1
    lista.append(10000)
    return count

numeros = []
N = 10

for i in range(N):
    numeros.append(randint(-3,3))

print(numeros)
print("El número 0 sale ", numeroCeros(numeros), " veces")
print(numeros)
