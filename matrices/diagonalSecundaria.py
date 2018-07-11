# crear matriz con números aleatorios
# sumar los elementos de la diagonal secundaria

from random import randint

def rellenarMatriz(m):
    for i in range(len(m)):
        for j in range(len(m)):
            m[i][j] = randint(1,9)

def imprimirMatriz(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(m[i][j], end =" ")
        print("")

def sumarDiagonalSecundaria(m):
    sum = 0
    for i in range(len(m)):
        sum = sum + m[i][len(m) - i - 1]
    return sum

matriz = [[0,0,0],[0,0,0],[0,0,0]]
rellenarMatriz(matriz)
imprimirMatriz(matriz)
print("La suma de elementos de la diagonal secundaria es: ", sumarDiagonalSecundaria(matriz))
