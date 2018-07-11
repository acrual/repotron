
class Asignatura(object):

    def __init__(self, nombre="", nota = 0):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return "\nAsignatura: " + str(self.nombre) + "\nNota: " + str(self.nota) + " \n"
