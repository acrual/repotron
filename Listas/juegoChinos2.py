# hacer un juego de los chinos con funciones y control de errores
from random import randint

CHINOS = 3
# damos por hecho que los valores de las jugadas son correctas
def obtenerGanador(resultado,eleccion1,eleccion2):

    if eleccion1 == resultado and eleccion1 != eleccion2:
        return 1
    elif eleccion2 == resultado and eleccion1 != eleccion2:
        return 2
    else: #no acierta ninguno
        return 0

# Solicita una jugada al usuario.
def solicitarJugada():
    jugada = int(input("Cuántas monedas tienes en tu mano?(0/1/2/3): "))
    while jugada < 0 or jugada > CHINOS:
            jugada = int(input("Error. Introduce la jugada (0/1/2/3): "))
    return jugada

# El usuario elige número de monedas que cree que hay en total
def eligeResultado():
    num = int(input("Cuántas monedas crees que hay en total?: "))
    while num < 0 or num > 6:
        num = int(input("Error. Dime cuántas monedas crees que hay en total?: "))
    return num

# El ordenador elige número de monedas que cree que hay en total
def cpuEligeNumMonedas(jugada):
    return randint(jugada,jugada + CHINOS)

def calcularJugadaCpu():
    return randint(0,CHINOS)

def mostrarEstadisticas(numEmpatados,numGanadosHumano,numGanadosCpu):
    print("")
    print("Habéis empatado ", numEmpatados, " veces")
    print("En total has ganado", numGanadosHumano, " veces")
    print("En total te han ganado", numGanadosCpu, " veces")
    print("")

def mostrarElecciones(eleccion1, resultado):
    print("Tu has elegido: ", eleccion1)

def mostrarElecciones2(eleccion2, resultado):
    print("La máquina ha elegido: ", eleccion2)

def mostrarElecciones3(jugadaCpu, resultado):
    print("La máquina tiene en la mano: ", jugadaCpu)

def mostrarResultado(ganador, resultado):
    print("En total hay :", (resultado))
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
    return resp

def jugarPartida(numPartidas):
    if numPartidas % 2 == 0:
        jugadaUsuario = solicitarJugada()
        jugadaCpu = calcularJugadaCpu()
        resultado = jugadaUsuario + jugadaCpu
        eleccionUsuario = eligeResultado()
        while eleccionUsuario < jugadaUsuario or eleccionUsuario > (jugadaUsuario + 3):
            print("Estás apampanado, ", end="")
            eleccionUsuario = eligeResultado()
        mostrarElecciones(eleccionUsuario, resultado)
        eleccionCpu = cpuEligeNumMonedas(jugadaCpu)
        while eleccionCpu < jugadaCpu or eleccionCpu > (jugadaCpu + 3):
            eleccionCpu = cpuEligeNumMonedas()
        mostrarElecciones2(eleccionCpu, resultado)
        ganador = obtenerGanador(resultado, eleccionUsuario, eleccionCpu)
        mostrarResultado(ganador, resultado)
    else:
        jugadaCpu = calcularJugadaCpu()
        jugadaUsuario = solicitarJugada()
        resultado = jugadaUsuario + jugadaCpu
        eleccionCpu = cpuEligeNumMonedas(jugadaCpu)
        while eleccionCpu < jugadaCpu or eleccionCpu > (jugadaCpu + 3):
            eleccionCpu = cpuEligeNumMonedas()
        mostrarElecciones2(eleccionCpu, resultado)
        eleccionUsuario = eligeResultado()
        while eleccionUsuario < jugadaUsuario or eleccionUsuario > (jugadaUsuario + 3):
            print("Estás apampanado, ", end="")
            eleccionUsuario = eligeResultado()
        mostrarElecciones3(jugadaCpu, resultado)
        mostrarElecciones(eleccionUsuario, resultado)
        ganador = obtenerGanador(resultado, eleccionUsuario, eleccionCpu)
        mostrarResultado(ganador, resultado)
    #print("La máquina tiene en la mano ", jugadaCpu)
    #mostrarElecciones(eleccionUsuario, eleccionCpu, jugadaCpu, resultado)
    return ganador

#PROGRAMA PRINCIPAL
empatados = 0
ganadosCpu = 0
ganadosHumano = 0
numPartidas = 0

resp = "S" #forzar a que entre la primera
while resp == "S":
    ganador = jugarPartida(numPartidas)
    numPartidas = numPartidas + 1
    if ganador == 0:
        empatados = empatados + 1
    elif ganador == 1:
        ganadosHumano = ganadosHumano + 1
    else:
        ganadosCpu = ganadosCpu + 1
    resp = repetirPartida()

print("Gracias por jugar ")
mostrarEstadisticas(empatados,ganadosHumano,ganadosCpu)
