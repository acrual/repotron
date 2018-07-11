N = 5

numeros = []

for i in range(N):
    pregunta = int(input("Dame un número entre 1 y 10 : "))
    while pregunta < 1 or pregunta > 10:
        pregunta = int(input("Error. Dame un número entre 1 y 10 : "))
    numeros.append(pregunta)

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
