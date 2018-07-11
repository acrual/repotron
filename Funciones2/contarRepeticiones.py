#contar cuantas veces se repite un números
from random import randint

def calcularJugada():
    valor = randint(1,5)
    return valor

num1 = calcularJugada()
num2 = calcularJugada()
num3 = calcularJugada()

def numRepeticiones():
    if num1 == num2 and num1 == num3:
        return 2
    elif num1 != num2 and num1 != num3:
        return 0
    elif :
        return 1

print("Los números son ", num1, " , ", num2, " y ", num3)
print("El número de repeticiones es: ", numRepeticiones())
