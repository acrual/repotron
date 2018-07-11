numeros = [0,0,0,0,0]

for i in range(len(numeros)):
    numeros[i] = int(input("Dame un número entre 1 y 10 : "))
    while numeros[i] < 1 or numeros[i] > 10:
        numeros[i] = int(input("Error. Dame un número entre 1 y 10 : "))

print("Lista del revés : ", end="")
for i in range(len(numeros)-1, -1, -1):
    print(numeros[i], end=" ")
print("")

print("Lista posiciones impares del revés : ", end="")
for i in range(len(numeros)-1, -1, -1):
    if i % 2 == 1:
        print(numeros[i], end=" ")
print("")

print("Lista posiciones pares del revés : ", end="")
for i in range(len(numeros)-1, -1, -1):
    if i % 2 == 0:
        print(numeros[i], end=" ")
print("")
