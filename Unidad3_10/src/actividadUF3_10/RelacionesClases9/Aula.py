from Alumno import Alumno

class Aula(object):

    def __init__(self, nombre = ""):
        self.nombre = nombre
        self.alumnos = []
        self.cantidad = 0

    def __str__(self):
        aux = "Aula " + self.nombre + "\nAlumnos:\n"
        # print("self.cantidad es : ",self.cantidad)
        for i in range(self.cantidad):
            aux = aux + self.alumnos[i].__str__() + "\n"
        return aux + "Número de alumnos: " + str(self.cantidad) + "\n"

    def buscar(self, dni):
        enc = False
        i = 0
        while (i < self.cantidad and not enc):
            if self.alumnos[i].dni == dni:
                enc = True
            else:
                i = i + 1
        return i, enc

    def agregarNuevoAlumno(self, alumno):
        if not self.buscar(alumno.dni)[1]:
            self.alumnos.append(alumno)
            self.cantidad = self.cantidad + 1
            return True
        return False

    def eliminarAlumno(self, dni):
        pos, enc = self.buscar(dni)
        if enc:
            self.alumnos.pop(pos)
            self.cantidad = self.cantidad - 1
            return True
        return False

    def ponerNota(self, dni, nota):
        pos, enc = self.buscar(dni)
        if enc:
            return self.alumnos[pos].ponerNota(nota)
        return False

    def subirNotasAlumno(self, dni, puntuacion):
        pos, enc = self.buscar(dni)
        if enc:
            self.alumnos[pos].subirNotas(puntuacion)
        return enc

    def bajarNotasAlumno(self, dni, puntuacion):
        pos, enc = self.buscar(dni)
        if enc:
            self.alumnos[pos].bajarNotas(puntuacion)
        return enc

    def devolverNombreAlumno(self, dni):
        pos, enc = self.buscar(dni)
        if enc:
            return self.alumnos[pos].nombre
        else:
            return "ERROR."

    def calcularNotaMedia(self):
        suma = 0.0
        for i in range(self.cantidad):
            suma = suma + self.alumnos[i].media
        return suma/self.cantidad

    def devolverNotaMayor(self):
        mayor = 0.0
        for i in range(self.cantidad):
            if self.alumnos[i].devolverNotaMayor() > mayor:
                mayor = self.alumnos[i].devolverNotaMayor()
        return mayor

    def subirTodasNotas(self, puntuacion):
        for i in range(self.cantidad):
            self.alumnos[i].subirNotas(puntuacion)
