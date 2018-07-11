# rellenar una lista solicitando valores al usuario
# esos valores deben estar entre 1 y 100 y sino se vuelven a pedir
# mostrar la lista y al final me devuelve el mayor de la lista y el menor

lista = [0,0,0,0,0]

#Rellenar lista, con restricción
for i in range(len(lista)):
    lista[i] = int(input("Introduce un número : "))
    while lista[i] < 1 or lista[i] > 100:
        lista[i] = int(input("Error, introduce un número : "))

#Mostrar elementos de la lista
for i in range(len(lista)):
    print(lista[i], end=" ")
print("")

#Obtener el mayor y el menor
mayor = lista[0]
menor = lista[0]
for i in range(1,len(lista)):
    if lista[i] > mayor:
        mayor = lista[i]
    if lista[i] < menor:
        menor = lista[i]

print("El mayor es : ", mayor)
print("El menor es : ", menor)
