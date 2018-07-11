from Partida import Partida
from Tablero import Tablero

class Juego(object):
    def __init__(self, ganadascpu = 0, ganadasjugador = 0, empatadas = 0):
        self.partida = Partida("", "")
        self.ganadascpu = ganadascpu
        self.ganadasjugador = ganadasjugador
        self.empatadas = empatadas

    def __str__(self):
        cadena = "\nLlevas " + str(self.ganadascpu + self.ganadasjugador + self.empatadas) + " partidas\n"
        cadena = cadena + "de las que " + str(self.ganadasjugador) + " son ganadas por tí, " + str(self.ganadascpu)
        cadena = cadena + " son ganadas por cpu, y " + str(self.empatadas) + " son empatadas"
        return cadena

    def actualizarStats(self, ganador):
        if ganador == "cpu":
            self.ganadascpu = self.ganadascpu + 1
        elif ganador == "jugador":
            self.ganadasjugador = self.ganadasjugador + 1
        else:
            self.empatadas = self.empatadas + 1

    def menuTipoPartida(self):
        while True:
            print("1. Opcion jugador vs jugador")
            print("2. Opcion jugador vs cpu")
            print("3. Opcion cpu vs cpu")
            opc = int(input("Por favor escoge opción: "))
            if opc < 1 or opc > 3:
                print("ERROR. Has elegido una opción no válida")
            else:
                break
        return opc

    def jugarPartida(self):
        while True:
            opcion = self.menuTipoPartida()
            if opcion == 1:
                jugador1 = "jugador"
                jugador2 = "jugador"
            elif opcion == 2:
                jugador1 = "jugador"
                jugador2 = "cpu"
            else:
                jugador1 = "cpu"
                jugador2 = "cpu"

            self.partida = Partida(jugador1, jugador2)
            ganador = self.partida.jugar()
            self.actualizarStats(ganador)
            respuesta = input("¿Quieres volver a jugar? (s/n): ")
            while respuesta != "s" and respuesta != "n":
                print("respuesta incorrecta")
                respuesta = input("¿Quieres volver a jugar? (s/n): ")
            if (respuesta == "n"):
                break

        print("Gracias por jugar!")
        print(self.__str__())
