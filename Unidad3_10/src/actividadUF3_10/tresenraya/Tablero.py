import numpy as np
from random import randint
class Tablero(object):

    MAX = 3
    SIMBOLOJUGADOR = 'X'
    SIMBOLOCPU = 'O'

    def __init__(self):
        self.matriz = np.empty((self.MAX,self.MAX), dtype = np.str)
        for i in range(self.MAX):
            for j in range(self.MAX):
                self.matriz[i,j] = '_'

    def __str__(self):
        cadena = ""
        for i in range(self.MAX):
            for j in range(self.MAX):
                cadena = cadena + self.matriz[i,j] + " "
            cadena = cadena + "\n"
        return cadena

    def colocarFicha(self, fila, columna, ficha):
        self.matriz[fila - 1,columna - 1] = ficha

    def hayTresHorizontal(self, fich):
        for i in range(self.MAX):
            suma = 0
            for j in range(self.MAX):
                if self.matriz[i,j] == fich:
                    suma = suma + 1
            if suma == self.MAX:
                return True
        return False

    def hayTresVertical(self, fich):
        for i in range(self.MAX):
            suma = 0
            for j in range(self.MAX):
                if self.matriz[j,i] == fich:
                    suma = suma + 1
            if suma == self.MAX:
                return True
        return False

    def hayTresDiagonalPrincipal(self, fich):
        suma = 0
        for i in range(self.MAX):
            if self.matriz[i,i] == fich:
                suma = suma + 1
        if (suma == self.MAX):
            return True
        return False

    def hayTresDiagonalSecundaria(self, fich):
        j = self.MAX - 1
        suma = 0
        for i in range(self.MAX):
            if self.matriz[i,j] == fich:
                suma = suma + 1
            j = j - 1
        if (suma == self.MAX):
            return True
        return False

    def hayTresEnRaya(self, ficha):
        return self.hayTresHorizontal(ficha) or self.hayTresVertical(ficha) or self.hayTresDiagonalPrincipal(ficha) or self.hayTresDiagonalSecundaria(ficha)

    def hayCasillaLibre(self):
        for i in range(self.MAX):
            for j in range(self.MAX):
                if self.matriz[i,j] == '_':
                    return True
        return False

    def esPosibleColocar(self,fila,columna):
        if fila < 1 or fila > self.MAX or columna < 1 or columna > self.MAX:
            return False
        if self.matriz[fila - 1, columna - 1] != '_':
            return False
        else:
            return True

    def actualizarStats(self, ganador):
        if ganador == 'cpu':
            self.ganadascpu = self.ganadascpu + 1
        elif ganador == 'jugador':
            self.ganadasjugador = self.ganadasjugador + 1
        elif ganador == 'ninguno':
            self.empatadas = self.empatadas + 1

    def elegirPosicionAleatoria(self):
        fila = randint(1, self.MAX)
        columna = randint(1,self.MAX)
        while not self.esPosibleColocar(fila,columna):
            fila = randint(1,self.MAX)
            columna = randint(1,self.MAX)
        return fila, columna

    def elegirPosicionAleatoria2(self, mejor, tipo):
        if tipo == "fila":
            columna = randint(1,self.MAX)
            while not self.esPosibleColocar(mejor,columna):
                columna = randint(1,self.MAX)
            return mejor, columna
        else:
            fila = randint(1,self.MAX)
            while not self.esPosibleColocar(fila, mejor):
                fila = randint(1,self.MAX)
            return fila, mejor

    def buscarFichaContrariaFila(self, fila):
        enc = False
        j = 0
        while not enc and j < self.MAX:
            if self.matriz[fila,j] == self.SIMBOLOJUGADOR:
                enc = True
            j = j + 1
        return enc

    def contarFichasPropiasFila(self,fila):
        conteo = 0
        for i in range(self.MAX):
            if self.matriz[fila,i] == self.SIMBOLOJUGADOR:
                conteo = conteo + 1
        return conteo

    def devolverMejorFila(self):
        mayor = -1
        mejorFila = -1
        for i in range(self.MAX):
            if not self.buscarFichaContrariaFila(i):
                if self.contarFichasPropiasFila(i) > mayor:
                    mayor = self.contarFichasPropiasFila(i)
                    mejorFila = i
        return mejorFila + 1

    def buscarFichaContrariaColumna(self, columna):
        enc = False
        i = 0
        while not enc and i < self.MAX:
            if self.matriz[i,columna] == self.SIMBOLOJUGADOR:
                enc = True
            i = i + 1
        return enc

    def contarFichasPropiasColumna(self,columna):
        conteo = 0
        for i in range(self.MAX):
            if self.matriz[i,columna] == self.SIMBOLOCPU:
                conteo = conteo + 1
        return conteo

    def devolverMejorColumna(self):
        mayor = -1
        mejorColumna = -1
        for i in range(self.MAX):
            if not self.buscarFichaContrariaColumna(i):
                if self.contarFichasPropiasColumna(i) > mayor:
                    mayor = self.contarFichasPropiasColumna(i)
                    mejorColumna = i
        return mejorColumna + 1
