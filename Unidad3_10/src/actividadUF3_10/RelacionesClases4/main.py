from Autor import Autor
from Fecha import Fecha
from Libro import Libro

libro1 = Libro("TBS", 200, 30, Autor("Saifedean", "Libanés", Fecha(1,1,1980)))
libro2 = Libro("Theory of Money", 500, 20, Autor("Ludwig von Mises", "Austriaco", Fecha(1,1,1880)))
libro3 = Libro("Libro inventado", 1000, 50, Autor("Autor inventado", "Nacionalidad inventada", Fecha(1,1,1900)))

print(libro1)
print(libro2)
print(libro3)

print("precio por página del libro 1: ", libro1.calcularPrecioPagina())
print("precio por página del libro 2: ", libro2.calcularPrecioPagina())
print("precio por página del libro 3: ", libro3.calcularPrecioPagina())

libro2.ponerEnOferta(int(input("Qué porcentaje quieres bajar el segundo libro? ")))

print(libro1)
print(libro2)
print(libro3)

print("precio por página del libro 1: ", libro1.calcularPrecioPagina())
print("precio por página del libro 2: ", libro2.calcularPrecioPagina())
print("precio por página del libro 3: ", libro3.calcularPrecioPagina())
