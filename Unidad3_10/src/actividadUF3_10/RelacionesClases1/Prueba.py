from Alumno import Alumno
from Asignatura import Asignatura

asig1 = Asignatura("Matemáticas", [7.5,5.2,3.9])
alumno1 = Alumno("1111A", "Marta", asig1)
alumno2 = Alumno("2222C", "Raúl", Asignatura("Lengua", [6.5, 7.8, 9.2]))

print(alumno1)
print(alumno2)

alumno1.asignatura.bajarNota(2)
alumno2.asignatura.subirNota(4)

print(alumno1)
print(alumno2)
