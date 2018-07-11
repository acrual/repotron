from Tablero import Tablero

from random import randint
class Partida(object):

    def __init__(self):
        self.tablero = Tablero()
        num = randint(1,2)
        if num == 1:
            self.turno = "jugador"
        else:
            self.turno = "cpu"

    def jugar(self):
        hayGanador = False
        while self.tablero.hayCasillaLibre() and not hayGanador:
            #Mostramos estado actual del tablero
            print(self.tablero)
            #determinamos si está jugando jugador o cpu
            if self.turno == "jugador":
                #Pedimos datos al jugador
                fila = int(input("Dime la fila: "))
                columna = int(input("Dime la columna: "))
                while not self.tablero.esPosibleColocar(fila,columna):
                    print("Casilla incorrecta. Vuelve a intentarlo por favor")
                    fila = int(input("Dime la fila: "))
                    columna = int(input("Dime la columna: "))
                if self.tablero.esPosibleColocar(fila,columna):
                    self.tablero.colocarFicha(fila,columna, Tablero.SIMBOLOJUGADOR)
                    if self.tablero.hayTresEnRaya(Tablero.SIMBOLOJUGADOR):
                        hayGanador = True
                else:
                    print("casilla equivocada")

            #turno CPU
            else:
                mejorFila = self.tablero.devolverMejorFila()
                if mejorFila != 0:
                    #Elegir casilla aleatoria, pero ojo con la fila fija
                    posiciones = self.tablero.elegirPosicionAleatoria2(mejorFila, "fila")
                    print("POSICION ELEGIDA POR LA CPU(",posiciones[0],",",posiciones[1],")")
                else:
                    mejorColumna = self.tablero.devolverMejorColumna()
                    if mejorColumna != 0:
                        posiciones = self.tablero.elegirPosicionAleatoria2(mejorColumna, "columna")
                        print("POSICION ELEGIDA POR LA CPU(",posiciones[0],",",posiciones[1],")")
                    else:
                        posiciones = self.tablero.elegirPosicionAleatoria()
                        print("POSICION ELEGIDA POR LA CPU(",posiciones[0],",",posiciones[1],")")

                self.tablero.colocarFicha(posiciones[0],posiciones[1], Tablero.SIMBOLOCPU)
                if self.tablero.hayTresEnRaya(Tablero.SIMBOLOCPU):
                    hayGanador = True

            if self.turno == "jugador":
                self.turno = "cpu"
            else:
                self.turno = "jugador"

        if hayGanador:
            if self.turno == 'jugador':
                print("GANA LA CPU")
                ganador = 'cpu'
                print(self.tablero)
            else:
                print("GANA EL JUGADOR")
                ganador = 'jugador'
                print(self.tablero)
        else:
            print("HABÉIS EMPATADO")
            ganador = 'ninguno'
            print(self.tablero)
        return ganador
