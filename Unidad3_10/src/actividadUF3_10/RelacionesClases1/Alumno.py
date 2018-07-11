from Asignatura import Asignatura

class Alumno(object):

    def __init__(self, dni = "", nombre = "", asignatura = Asignatura()):
        self.dni = dni
        self.nombre = nombre
        self.asignatura = asignatura

    def __str__(self):
        return "DNI: " + str(self.dni) + "\nNombre: " + str(self.nombre) + "\nAsignatura:\n" + self.asignatura.__str__()
