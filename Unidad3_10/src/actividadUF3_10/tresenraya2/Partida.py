from Tablero import Tablero

from random import randint
class Partida(object):

    def __init__(self, jugador1, jugador2):
        self.tablero = Tablero()
        self.turno = randint(1,2)
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def jugar(self):
        hayGanador = False
        #and not hayGanador1 and not hayGanador2
        while self.tablero.hayCasillaLibre() and not hayGanador:
            #Mostramos estado actual del tablero
            print(self.tablero)
            #determinamos si está jugando jugador o cpu
            if self.turno == 1:
                jugadorActual = self.jugador1
            else:
                jugadorActual = self.jugador2

            if jugadorActual == "jugador":
                #Pedimos datos al jugador
                fila = int(input("Dime la fila: "))
                columna = int(input("Dime la columna: "))
                while not self.tablero.esPosibleColocar(fila,columna):
                    print("Casilla incorrecta. Vuelve a intentarlo por favor")
                    fila = int(input("Dime la fila: "))
                    columna = int(input("Dime la columna: "))
                if self.turno == 1:
                    self.tablero.colocarFicha(fila,columna, Tablero.SIMBOLO1)
                    if self.tablero.hayTresEnRaya(Tablero.SIMBOLO1):
                        hayGanador = True
                else:
                    self.tablero.colocarFicha(fila,columna, Tablero.SIMBOLO2)
                    if self.tablero.hayTresEnRaya(Tablero.SIMBOLO2):
                        hayGanador = True
            #turno CPU
            else:
                mejorFila = self.tablero.devolverMejorFila(self.turno)
                if mejorFila != 0:
                    #Elegir casilla aleatoria, pero ojo con la fila fija
                    posiciones = self.tablero.elegirPosicionAleatoria2(mejorFila, "fila")
                    print("POSICION ELEGIDA POR LA CPU(",posiciones[0],",",posiciones[1],")")
                else:
                    mejorColumna = self.tablero.devolverMejorColumna(self.turno)
                    if mejorColumna != 0:
                        posiciones = self.tablero.elegirPosicionAleatoria2(mejorColumna, "columna")
                        print("POSICION ELEGIDA POR LA CPU(",posiciones[0],",",posiciones[1],")")
                    else:
                        posiciones = self.tablero.elegirPosicionAleatoria()
                        print("POSICION ELEGIDA POR LA CPU(",posiciones[0],",",posiciones[1],")")

                if self.turno == 1:
                    self.tablero.colocarFicha(posiciones[0],posiciones[1], Tablero.SIMBOLO1)
                    if self.tablero.hayTresEnRaya(Tablero.SIMBOLO1):
                        hayGanador = True
                else:
                    self.tablero.colocarFicha(posiciones[0],posiciones[1], Tablero.SIMBOLO2)
                    if self.tablero.hayTresEnRaya(Tablero.SIMBOLO2):
                        hayGanador = True

            if self.turno == 1:
                self.turno = 2
            else:
                self.turno = 1

        if hayGanador:
            if self.turno == 1:
                print("Gana ",self.jugador2)
                return self.jugador2
            else:
                print("Gana ",self.jugador1)
                return self.jugador1
        else:
            print("HABÉIS EMPATADO")
            return "ninguno"
