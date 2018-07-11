# pedir piedra papel tijera, calcular aleatoriamente lo que sale a la máquina
# y decir si ganas o no
# obtener ganador, humano y computadora, en forma string
# todas las posibilidades definir
# cero es empate
from random import randint

# damos por hecho que los valores de las jugadas son correctas
def obtenerGanador(jugada1,jugada2):

    if jugada1 =="piedra" and jugada2 == "piedra":
        resultado = 0
    elif jugada1 == "piedra" and jugada2 == "papel":
        resultado = 2
    elif jugada1 == "piedra" and jugada2 == "tijeras":
        resultado = 1
    elif jugada1 == "papel" and jugada2 == "piedra":
        resultado = 1
    elif jugada1 == "papel" and jugada2 == "papel":
        resultado = 0
    elif jugada1 == "papel" and jugada2 == "tijeras":
        resultado = 2
    elif jugada1 == "tijeras" and jugada2 == "piedra":
        resultado = 2
    elif jugada1 == "tijeras" and jugada2 == "papel":
        resultado = 1
    else:
        resultado = 0
    return resultado

# Solicita una jugada al usuario
def solicitarJugada():
    jugada = input("Introduce la jugada (piedra/papel/tijeras): ")
    while jugada != "piedra" and jugada != "papel" and jugada != "tijeras":
            jugada = input("Error. Introduce la jugada (piedra/papel/tijeras): ")
    return jugada

# Elige de manera aleatoria una jugada
def calcularJugada():
    valor = randint(1,3)
    if valor == 1:
        return "piedra"
    elif valor == 2:
        return "papel"
    else:
        return "tijeras"

def mostrarEstadisticas(numEmpatados,numGanadosHumano,numGanadosCpu):
    print("")
    print("En total has ganado", numGanadosHumano, " veces")
    print("En total te han ganado", numGanadosCpu, " veces")
    print("Habéis empatado ", numEmpatados, "veces")
    print("")

def mostrarResultado(ganador):

    if  ganador == 0:
        print("Habéis empatado ")
    elif ganador == 1:
        print("Has ganado")
    else:
        print("Ha ganado la máquina ")

def repetirPartida():
    print("")
    resp = input("¿Quieres seguir jugando? (S/N) : ")
    print("")
    while resp != "S" and resp != "N":
         resp = input("¿Quieres seguir jugando? (S/N) : ")
    return(resp)

def jugarPartida():
    jugadaUsuario = solicitarJugada()
    jugadaCpu = calcularJugada()
    print("La máquina ha elegido", jugadaCpu)
    ganador = obtenerGanador(jugadaUsuario, jugadaCpu)
    mostrarResultado(ganador)

#PROGRAMA PRINCIPAL
empatados = 0
ganadosCpu = 0
ganadosHumano = 0

resp = "S" #forzar a que entre la primera
while resp == "S":
    ganador = jugarPartida()
    if ganador == 0:
        empatados = empatados + 1
    elif ganador == 1:
        ganadosHumano = ganadosHumano + 1
    else:
        ganadosCpu = ganadosCpu + 1
    resp = repetirPartida()

print("Gracias por jugar ")
mostrarEstadisticas(empatados,ganadosHumano,ganadosCpu)
