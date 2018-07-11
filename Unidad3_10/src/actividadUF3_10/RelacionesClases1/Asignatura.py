
class Asignatura(object):
    def __init__(self, nombre="", nota = [0,0,0]):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return "Nombre: " + str(self.nombre) + "\nNota "+str(self.nota ) + "\n"

    def subirNota(self, val):
        for i in range(len(self.nota)):
            self.nota[i] = self.nota[i] + val
            if self.nota[i] > 10.0:
                self.nota[i] = 10.0

    def bajarNota(self, val):
        for i in range(len(self.nota)):
            self.nota[i] = self.nota[i] - val
            if self.nota[i] < 0.0:
                self.nota[i] = 0.0
