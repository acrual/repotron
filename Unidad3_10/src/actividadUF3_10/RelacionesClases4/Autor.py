from Fecha import Fecha

class Autor(object):
    def __init__(self, nombre="", nacionalidad="", fecha = Fecha()):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha = fecha

    def __str__(self):
        return "\nNombre: " + str(self.nombre) + "\nNacionalidad: " + str(self.nacionalidad) + "\nFechaNacimiento: " + self.fecha.__str__() + "\n"

    def modificarAutor(self):
        self.nombre = input("Nuevo nombre de Autor: ")
        self.nacionalidad = input("Nacionalidad? ")
        self.fecha.dd = input("Dia de nacimiento:(dd) ")
        self.fecha.mm = input("Mes de nacimiento:(mm) ")
        self.fecha.aa = input("Año de nacimiento:(aaaa) ")
