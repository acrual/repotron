#
class Asignatura(object):
    def __init__(self, nombre="", nota = 0.0):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return "Nombre: " + str(self.nombre) + "\nNota "+str(self.nota ) + "\n"

    def subirNota(self, val):
        self.nota = self.nota + val
        if self.nota > 10.0:
            self.nota = 10.0

    def bajarNota(self, val):
        self.nota = self.nota - val
        if self.nota < 0.0:
            self.nota = 0.0
