#relleno lista con valores aleatorios 1-5
# muestra la lista y pones la suma de los elementos de la lista
# muestra el prdoucto de los elementos

from random import randint

numeros = [0,0,0,0,0]
for i in range(len(numeros)):
    numeros[i] = randint(0,9)

for i in range(len(numeros)):
    print(numeros[i],end=" ")
print("")

suma = 0
prod = 1

for i in range(len(numeros)):
    suma = suma + numeros[i]
    prod = prod*numeros[i]

print("La suma de los elementos la la lista es : ", suma)
print("El producto de los elementos de la lista es : ", prod)
