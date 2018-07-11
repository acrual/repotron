from random import randint

N = 10
numeros = []

for i in range(N):
    numeros.append(randint(1,N))

print(numeros)
pregunta = int(input("Dame un número : "))
count = 0
for i in range(len(numeros)):
    if numeros[i] == pregunta:
        print("El número ", pregunta, " está en la posición ", i)
        count = count + 1

for i in range(count):
    numeros.remove(pregunta)

print(numeros)
