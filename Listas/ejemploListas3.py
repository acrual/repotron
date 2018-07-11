# rellenar un array de 10 elementos con números aleatorios entre 1-10
# muestra la lista completa
#muestra los elmentos pares
#otro con sublista con los elementos que ocupan las posiciones impares
# contar cuantos múltiplos de 5 Hay

from random import randint

numeros = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(numeros)):
    numeros[i] = randint(1,10)

cuentaMultiplosCinco = 0

for i in range(len(numeros)):
    print(numeros[i], end=" ")
print("")

print("Los elementos pares son:",end=" ")
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        print(numeros[i],end= " " )
print("")

print("En las posiciones impares están: ", end=" ")
for i in range(len(numeros)):
    if i % 2 == 1:
        print(numeros[i], end=" ")
print("")

for i in range(len(numeros)):
    if numeros[i] % 5 == 0:
        cuentaMultiplosCinco = cuentaMultiplosCinco + 1
print("Hay ", cuentaMultiplosCinco, " múltiplos de cinco")
