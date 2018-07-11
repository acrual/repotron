# rellenar array a mano y comprobar si todos sus elementos son positivos.

N = 5
numeros = []
for i in range(N):
    numeros.append(int(input("Dame un número : ")))

todosPositivos = True
negativos = []
for i in range(len(numeros)):
    if numeros[i] < 0:
        todosPositivos = False
        negativos.append(numeros[i])

if todosPositivos:
    print("Son todos positivos")
else:
    print("No son todos positivos. Son negativos :", end=" ")
    for i in range(len(negativos)):
        print(negativos[i], end=" ")
