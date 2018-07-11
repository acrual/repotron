from random import randint

N = 10
numeros = []

for i in range(N):
    numeros.append(randint(1,10))

print(numeros)
pregunta = int(input("Dame un número : "))
if pregunta in numeros:
    numeros.remove(pregunta)
    print("El listado se queda así tras eliminar el número : ", numeros)
else:
    print("No se ha encontrado el número en la lista")
