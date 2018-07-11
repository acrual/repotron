# este es diferente a numeroceros porque en vez de lista es variable y por eso no
#cambia el resultado antes y después de la llamada a la función. En lista pasa la variable
# por referencia mientras que en variable la pasa como copia
from random import randint

def numeroCeros(lista):

    count = 0

    lista = lista * 4
    return count

numeros = 3

print(numeros)
print("El número 0 sale ", numeroCeros(numeros), " veces")
print(numeros)
