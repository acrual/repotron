from Partida import Partida
from Tablero import Tablero

class Juego(object):
    def __init__(self, partida = Partida(), ganadascpu = 0, ganadasjugador = 0, empatadas = 0):
        self.partida = partida
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

    def jugarPartida(self):

        while True:
            self.partida = Partida()
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
