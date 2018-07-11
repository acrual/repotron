class Persona(object):

    def __init__(self, dni="", nombre=""):
        self.dni = dni
        self.nombre = nombre

    def __str__(self):
        return "\nDNI: " + self.dni + "\nNombre: " + self.nombre + "\n"
