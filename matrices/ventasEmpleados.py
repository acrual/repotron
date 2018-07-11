# rellenar lista con N números entre 1 y 5
from random import randint

def rellenarMatriz(numEmpleados, numDiasSemana):
    ventasEmpleados = [[],[],[]] #Local a la función
    for i in range(numEmpleados):
        for j in range(numDiasSemana):
            ventasEmpleados[i].append(randint(1,9))
    return ventasEmpleados

def mostrarMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print("")

def calcularVentasPorEmpleado(matriz):
    ventasPorEmpleado = []
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            suma = suma + matriz[i][j]
        ventasPorEmpleado.append(suma)
    return ventasPorEmpleado

def calcularMedias(vEmpleados, numDiasSemana):
    mediaPorEmpleado = []
    for i in range(len(vEmpleados)):
        mediaPorEmpleado.append(vEmpleados[i]/numDiasSemana)
    return mediaPorEmpleado

def mostrarDatos(vEmpleados, mEmpleados):
    for i in range(len(vEmpleados)):
        print("Las ventas del empleado ", i + 1,"son:",vEmpleados[i] )
        print("La media del empleado ", i + 1, "es:", mEmpleados[i])
    print("")

numEmpleados = 3
numDiasSemana = 5

matriz = rellenarMatriz(numEmpleados, numDiasSemana)
mostrarMatriz(matriz)
ventasEmpleados = calcularVentasPorEmpleado(matriz)
mediaEmpleados = calcularMedias(ventasEmpleados, numDiasSemana)
mostrarDatos(ventasEmpleados, mediaEmpleados)
