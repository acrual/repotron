# mostrar los dos menores con una función
N = 5

def menores():
    ultimo = int(input("Introduce un número : "))
    penultimo = int(input("Introduce un número : "))
    if ultimo>penultimo:
        aux = ultimo
        ultimo = penultimo
        penultimo = aux

    for i in range(N-2): #0..N-3
        num = int(input("Introduce un número : "))
        if num<ultimo:
            penultimo = ultimo
            ultimo = num
        elif num<penultimo:
            penultimo = num
    return ultimo, penultimo

menor, menorAnt = menores()
print("El más pequeño es el",menor,"y el segundo más pequeño es el",menorAnt)
