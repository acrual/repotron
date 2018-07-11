# dni, nombre,  y edad

class Persona(object):

    # def __init__(self):
    #     self.dni = ""
    #     self.nombre = ""
    #     self.edad = 0

    def __init__(self, dni, nombre, edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Esta persona se llama " + str(self.nombre) + " tiene dni " + str(self.dni) + " y tiene una edad de " + str(self.edad)

    def incrementarEdad(self, valor):
        self.edad = self.edad + valor
