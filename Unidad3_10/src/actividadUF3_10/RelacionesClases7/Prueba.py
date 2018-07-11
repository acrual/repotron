from Alumno import Alumno
from Asignatura import Asignatura

alumno = Alumno("1111A", "Marta", [Asignatura('Mates', 5.0), Asignatura('Lengua', 5.0), Asignatura('Química', 5.0)])

opcion = 1
while opcion != 0:
    print(alumno)
    print("1. Subir nota al alumno ")
    print("2. Bajar nota al alumno ")
    print("3. Subir todas las notas al alumno")
    print("4. Bajar todas las notas al alumno")
    print("5. Poner nota a un alumno")
    print("6. Calcular nota media del alumno")
    print("7. Calcular nota más alta")
    print("8. Calcular nota más alta")
    print("0. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        posicion = int(input("¿Qué asignatura quieres subir? "))
        val = float(input("¿Cuántos puntos? "))
        alumno.subirNota(posicion-1, val)

    elif opcion == 2:
        posicion = int(input("¿Qué asignatura quieres bajar? "))
        val = float(input("¿Cuántos puntos? "))
        alumno.bajarNota(posicion-1, val)

    elif opcion == 3:
        val = float(input("¿Cuántos puntos? "))
        alumno.subirTodasNotas(val)

    elif opcion == 4:
        val = float(input("¿Cuántos puntos? "))
        alumno.bajarTodasNotas(val)

    elif opcion == 5:
        posicion = int(input("¿A qué asignatura quieres ponerle nota? "))
        val = int(input("Qué nota quieres ponerle? "))
        alumno.ponerNota(posicion-1, val)

    elif opcion == 6:
        alumno.calcularNotaMedia()

    elif opcion == 7:
        print("La nota más alta es: ",alumno.calcularNotaMasAlta())

    elif opcion == 8:
        print("La nota más baja es: ",alumno.calcularNotaMasBaja())

    elif opcion == 0:
        print("muchas gracias")

    else:
        print("Opción incorrecta")
