# La mas sencilla e intuitiva
matriz1 = []
filas = 3
columnas = 3

for i in range(filas):
    matriz1.append([])
    for j in range(columnas):
        matriz1[i].append(0)

matriz2 = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(filas):
    for j in range(columnas):
        matriz2[i][j] = int(input("Introduce elemento: "))
    print("")

for i in range(filas):
    for j in range(columnas):
        print(matriz1[i][j],end = " ")
    print("")
print("")
for i in range(filas):
    for j in range(columnas):
        print(matriz2[i][j],end = " ")
    print("")
