# segunda intentona del juego de capicua

def rellenarLista(lista):

    for i in range(len(lista)):
        lista[i] = int(input("Dame un número : "))
        while lista[i] < 1 or lista[i] > 9:
            lista[i] = int(input("Error. Dame un número : "))

def esCapicua(lista):

    capicua = True
    i = 0
    j = len(lista) - 1 #última posición
    while capicua and i < len(lista) // 2:
        if numeros[i] != numeros[j]:
            capicua = False
        else:
            i = i + 1
            j = j - 1
    return capicua

numeros = [0,0,0,0,0,0,0]

rellenarLista(numeros)
if esCapicua(numeros):
    print("La lista es capicua")
else:
    print("La lista no es capicua")
