from Asignatura import Asignatura

class Alumno(object):
#
    def __init__(self, dni = "", nombre = "", asignaturas = Asignatura()):
        self.dni = dni
        self.nombre = nombre
        self.asignaturas = asignaturas

    def __str__(self):
        cadena = "DNI: " + str(self.dni) + "\nNombre: " + str(self.nombre) + "\n"
        for i in range(len(self.asignaturas)):
            cadena= cadena + str(self.asignaturas[i]) + " "
        return cadena + "\n"

    def esPosValida(self, posicion):
        return posicion >= 0 and posicion < len(self.asignaturas)

    def noSuperaNotaMax(self, valor, i):
        return self.asignaturas[i].nota + valor <= 10.0

    def noSuperaNotaMin(self, valor, i):
        return self.asignaturas[i].nota - valor >= 0.0

    def subirNota(self, pos, val):
        if self.esPosValida(pos) and self.noSuperaNotaMax(val, pos):
            self.asignaturas[pos].nota = self.asignaturas[pos].nota + val
            return True
        return False

    def bajarNota(self, pos, val):
        if self.esPosValida(pos) and self.noSuperaNotaMin(val, pos):
            self.asignaturas[pos].nota = self.asignaturas[pos].nota - val
            return True
        return False

    def subirTodasNotas(self,val):
        for i in range(len(self.asignaturas)):
            self.subirNota(i, val)

    def bajarTodasNotas(self,val):
        for i in range(len(self.asignaturas)):
            self.bajarNota(i, val)

    def ponerNota(self, pos, nota):
        if self.esPosValida(pos):
            self.asignaturas[pos].nota = nota
            return True
        return False

    def calcularNotaMedia(self):
        sum = 0.0
        for pos in range(len(self.asignaturas)):
            sum = sum + self.asignaturas[pos].nota
        print("La nota media del alumno es",sum/len(self.asignaturas))

    def calcularNotaMasAlta(self):
        mayor = 0.0
        for pos in range(len(self.asignaturas)):
            if self.asignaturas[pos].nota > mayor:
                mayor = self.asignaturas[pos].nota
        return mayor

    def calcularNotaMasBaja(self):
        menor = 10.0
        for pos in range(len(self.asignaturas)):
            if self.asignaturas[pos].nota < menor:
                menor = self.asignaturas[pos].nota
        return menor
