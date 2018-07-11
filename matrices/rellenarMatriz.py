from random import randint

def rellenarMatriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = randint(1,5)

def imprimirMatriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end = " ")
        print("") #Se termina de dibujar una fila y se salta de línea

def contarParesImpares(m):
    pares = 0
    impares = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] % 2 == 0:
                pares = pares + 1
            else:
                impares = impares + 1
    return pares, impares

def sumaElementos(m):
    suma = 0
    for i in range(len(m)):
        for j in range(len(m)):
            suma = suma + m[i][j]
    return suma

def sumarDiagonal(m):
    suma = 0
    for i in range(len(matriz)):
        suma = suma + matriz[i][i]
    return suma

matriz = [[0,0,0],[0,0,0],[0,0,0]]
rellenarMatriz(matriz) #por referencia
imprimirMatriz(matriz)
contPares,contImpares = contarParesImpares(matriz)
print("Hay ", contPares, " pares y ", contImpares, " impares y la suma de la diagonal es ", sumarDiagonal(matriz))
print("La suma de los elementos es : ", sumaElementos(matriz))
