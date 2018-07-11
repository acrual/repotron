from random import randint

numeros = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(numeros)):
    numeros[i] = randint(1,100)

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
