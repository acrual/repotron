numeros = [0,0,0,0,0]
contPares = 0
contImpares = 0

for i in range(len(numeros)):
    numeros[i] = int(input("Introduce elemento: "))

for i in range(len(numeros)):
    print(numeros[i],end=" ")
    if numeros[i] % 2 == 0:
        contPares = contPares + 1
    else:
        contImpares = contImpares + 1

print("")
print("Hay",contPares,"pares")
print("Hay",contImpares,"impares")
