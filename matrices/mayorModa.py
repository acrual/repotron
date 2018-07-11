from random import randint

def crearLista(N):
    array = []
    for i in range(N):
        array.append(randint(1,5))
    return array

def cualMayor(lista):
    mayor = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

def cuantasMayor(lista, mayor):
    count = 0
    for i in range(len(lista)):
        if lista[i] == mayor:
            count = count + 1
    return count

N = 20

lista = crearLista(N)
mayor = cualMayor(lista)
print("El mayor de la lista",lista,"es",mayor,"y sale", cuantasMayor(lista,mayor), "veces")
