# rellenar matriz con elementos solicitados al usuario de 1 a 10
# mostrar matriz
# pedir una fila al usuario
# crear una lista con esos elementos y append
# mostrar la lista resultante

#Se devuelve la matriz rellena mediante referencia (modificamos la original a través de m)
def rellenarMatriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print("Dame el elemento fila ", i + 1, " y columna ", j + 1,end=": ")
            m[i][j] = int(input())
            while m[i][j] < 1 or m[i][j] > 10:
                m[i][j] = int(input("Error. Dame el elemento fila: "))

def imprimirMatriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end = " ")
        print("")

def copiarMostrarFila(f, m):
    #f = f - 1
    lista_fila = []
    print("La fila es : ", end = " ")
    for j in range(len(m)):
        lista_fila.append(m[f][j])
        print(lista_fila[j], end = " ")
    print("")

def pedirFila(max):
    fila = int(input("Introduce el número de fila: "))
    while fila < 1 or fila > max:
        fila = int(input("Error. Introduce el número de fila: "))
    return fila

def pedirColumna(maxcol):
    columna = int(input("Introduce el número de columna: "))
    while columna < 1 or columna > 10:
        columna = int(input("Error. Introduce el número de columna: "))
    return columna

def copiarMostrarColumna(c, m):
    #c = c - 1
    lista_columna = []
    print("La columna es : ", end = " ")
    for i in range(len(m)):
        lista_columna.append(m[i][c])
        print(lista_columna[i], end = " ")
    print("")

matriz = [[0,0,0],[0,0,0],[0,0,0]]
rellenarMatriz(matriz)
imprimirMatriz(matriz)
fila = pedirFila(len(matriz))
copiarMostrarFila(fila - 1, matriz)
columna = pedirColumna(len(matriz))
copiarMostrarColumna(columna - 1, matriz)
