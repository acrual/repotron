from random import randint

numeros = []

for i in range(10):
    numeros.append(randint(1,100))

mayor = 0
segundo = 0
for i in range(len(numeros)):
    if numeros[i] > mayor:
        segundo = mayor
        mayor = numeros[i]
    elif numeros[i] > segundo:
        segundo = numeros[i]

print(numeros)
print(" El primero es ", mayor, " y el segundo es : ", segundo)
