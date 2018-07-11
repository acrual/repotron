from random import randint

N = 5

def crearLista():
    array = []
    for i in range(N):
        array.append(randint(1,5))
    return array

def calcularMayorVeces(lista):
    mayor = lista[0]
    contMayor = 1
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            contMayor = 1
        elif lista[i] == mayor:
            contMayor = contMayor + 1
    return mayor,contMayor

lista = crearLista()
mayor,veces = calcularMayorVeces(lista)
print("El mayor de la lista",lista,"es",mayor,"y sale",veces, "veces")
