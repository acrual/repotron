# lista ordenada
from random import randint

def esOrdenada(vector):
    for i in range(1, len(vector)):
        if vector[i] < vector[i-1]: #están desordenados
            return False
    return True

def estaOrdenada(vector):
    i = 0
    ordenada = True

    while ordenada and i < len(vector) - 1:
        if (vector[i] > vector[i+1]):
            ordenada = False
        else:
            i = i + 1
    return ordenada

vector = [2,8,6,8,9]
print(vector)
if esOrdenada(vector):
    print("La lista está ordenada")
else:
    print("La lista está desordenada")

if not estaOrdenada(vector):
    print("La lista NO está ordenada")
else:
    print("La lista está ordenada")
