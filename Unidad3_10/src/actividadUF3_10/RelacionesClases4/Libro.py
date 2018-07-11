from Fecha import Fecha
from Autor import Autor

class Libro(object):
    def __init__(self, titulo="", paginas=100, precio=10, autor = Autor()):
        self.titulo = titulo
        self.paginas = paginas
        self.precio = precio
        self.autor = autor

    def __str__(self):
        return "\nTitulo: " + str(self.titulo) + "\nPáginas: " + str(self.paginas) + "\nPrecio: " + str(self.precio) + "\nAutor: " + self.autor.__str__() + "\n"

    def calcularPrecioPagina(self):
        return self.precio/self.paginas

    def ponerEnOferta(self, porcentaje):
        self.precio = self.precio * (1 - (porcentaje/100))
