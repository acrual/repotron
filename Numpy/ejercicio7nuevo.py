
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

def moverElementosVector(v,n):
    aux = []
    for i in range(len(v)):
        aux.append(0)

    for i in range(len(aux)):
        aux[(i + n) % len(v)] = v[i]

    for i in range(len(aux)):
        v[i] = aux[i]

lista = []
rellenarVector(lista)
mostrarVector(lista)

posiciones = int(input("Posiciones a la derecha?: "))
while posiciones <0:
    posiciones = int(input("Error, no puede ser negativo. Posiciones a la derecha?: "))
moverElementosVector(lista,posiciones)
mostrarVector(lista)
