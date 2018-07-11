# rellenar una lista solicitando valores al usuario
# esos valores deben estar entre 1 y 100 y sino se vuelven a pedir
# mostrar la lista y al final me devuelve el mayor de la lista y el menor

numeros = [0,0,0]

for i in range(len(numeros)):
    numeros[i] = int(input("Introduce un número : "))
    while numeros[i] < 1 or numeros[i] > 100:
        numeros[i] = int(input("Error, introduce un número : "))

mayor = 0
for i in range(len(numeros)):
    print(numeros[i], end=" ")
    if i > 0:
        if numeros[i] > numeros[i-1]:
            mayor = numeros[i]
    if i > 0:
        if numeros[i] < numeros[i-1]:
            menor = numeros[i]

print("El mayor es : ", mayor)
print("El menor es : ", menor)
