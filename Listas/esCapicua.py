# Averiguar si una lista es capicúa

def esCapicua(lista):
    capicua = True
    i = 0
    j = len(lista) - 1
    while(i < len(lista) // 2 and capicua):
        if lista[i] != lista[j]: #He encontrado dos no iguales. No capicúa
            capicua = False
        else:
            i = i + 1
            j = j - 1

    return capicua

lista1 = [1,2,3,4,3,2,1]
lista2 = [1,2,2,3,2,1]

if esCapicua(lista1):
    print(lista1, " es capicua ")
else:
    print(lista1, " no es capicua ")

if esCapicua(lista2):
    print(lista2, " es capicua ")
else:
    print(lista2, " no es capicua ")
