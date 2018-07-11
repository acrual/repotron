class Alumno(object):

    MAX = 3
    cont = 1

    def __init__(self, nombre = "", edad = 0.0):
        self.dni = Alumno.cont
        Alumno.cont = Alumno.cont + 1
        self.nombre = nombre
        self.edad = edad
        self.notas = []
        self.media = 0.0

    def __str__(self):
        cadena = "DNI: " + str(self.dni) + "\nNombre: " + str(self.nombre) + "\nEdad: " + str(self.edad) + "\nNotas: "
        for i in range(len(self.notas)):
            cadena= cadena + str(self.notas[i]) + " "
        cadena = cadena + "\nMedia: " + str(self.media)
        return cadena + "\n"

    def calcularMedia(self):
        suma = 0
        for i in range(len(self.notas)):
            suma = suma + self.notas[i]
        self.media = suma/len(self.notas)

    def ponerNota(self, nota):
        if len(self.notas) < Alumno.MAX and nota >= 0.0 and nota <= 10.0:
            self.notas.append(nota)
            self.calcularMedia()
            return True
        return False

    def subirNotas(self, nota):
        for i in range(len(self.notas)):
            self.notas[i] = self.notas[i] + nota
            if self.notas[i] + nota >= 10:
                self.notas[i] = 10
        self.calcularMedia()

    def bajarNotas(self, nota):
        for i in range(len(self.notas)):
            self.notas[i] = self.notas[i] - nota
            if self.notas[i] - nota <= 0:
                self.notas[i] = 0
        self.calcularMedia()

    def devolverNotaMayor(self):
        mayor = 0.0
        for i in range(len(self.notas)):
            if self.notas[i] > mayor:
                mayor = self.notas[i]
        return mayor

    #def devolverNotaMenor(self):
