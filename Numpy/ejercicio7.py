import numpy as np
from random import randint

# sin numpy
N = 10

def rellenarVector(v):
    for i in range(N):
        v.append(randint(1,10))
    return v

def mostrarVector(v):
    for i in range(len(v)):
        print(v[i], end = " ")
    print("")

def mostrarVectorMovido(v,n):
    for i in range(len(v)):
        if i < n:
            print(v[(len(v) - n) + i], end = " ")
        else:
            print(v[i - n], end = " ")
    print("")

lista = []
rellenarVector(lista)
mostrarVector(lista)

posiciones = int(input("Posiciones a la derecha?: "))
while posiciones < 0:
    posiciones = int(input("Error, no puede ser negativo. Posiciones a la derecha?: "))
mostrarVectorMovido(lista,posiciones)
