# rellenar una lista solicitando valores al usuario
# esos valores deben estar entre 1 y 100 y sino se vuelven a pedir
# mostrar la lista y al final me devuelve el mayor de la lista y el menor

lista = [0,0,0,0,0]

#Rellenar lista, con restricción
for i in range(len(lista)):
    lista[i] = float(input("Introduce un número : "))

#Mostrar elementos de la lista
for i in range(len(lista)):
    print(lista[i], end=" ")
print("")

#calcular la media
suma = 0
for i in range(len(lista)):
    suma = suma + lista[i]

print("La media aritmética es : ", suma/len(lista))
