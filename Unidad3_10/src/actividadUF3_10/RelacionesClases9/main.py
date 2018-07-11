from Aula import Aula
from Alumno import Alumno
#
aula = Aula("1A")

opcion = 1
while opcion != 0:
    print("1. Agregar alumno ")
    print("2. Eliminar alumno ")
    print("3. Mostrar aula ")
    print("4. Poner nota a alumno")
    print("5. Subir todas las notas")
    print("6. Bajar todas las notas")
    print("7. Obtener nombre introduciendo DNI")
    print("8. Calcular nota media del aula")
    print("9. Dame la máxima nota del aula")
    print("10. Subir todas las notas de todos los alumnos")
    print("0. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        nombre = input("Dame el nombre del alumno: ")
        edad = int(input("Dame su edad: "))
        alumno = Alumno(nombre, edad)
        if aula.agregarNuevoAlumno(alumno):
            print("Alumno agregado")
        else:
            print("ERROR. Alumno duplicado")

    elif opcion == 2:
        dni = int(input("Dame el dni del alumno a eliminar: "))
        if aula.eliminarAlumno(dni):
            print("Alumno eliminado")
        else:
            print("ERROR. Alumno no encontrado")

    elif opcion == 3:
        print(aula)

    elif opcion == 4:
        dni = int(input("Introduce el dni del alumno al quieres poner nota : "))
        nota = float(input("¿Qué nota quieres ponerle? "))
        if aula.ponerNota(dni, nota):
            print("Nota agredada a ", aula.devolverNombreAlumno(dni))
        else:
            print("ERROR. No hemos encontrado nota/alumno o has alcanzado el max núm de notas")

    elif opcion == 5:
        dni = int(input("Introduce el dni del alumno al quieres subir las notas : "))
        subida = int(input("¿Cuántos puntos? "))
        if aula.subirNotasAlumno(dni, subida):
            print("Notas subidas ", subida, " puntos")
        else:
            print("ERROR. Alumno no encontrado")

    elif opcion == 6:
        dni = int(input("Introduce el dni del alumno al quieres subir las notas : "))
        bajada = int(input("Cuántos puntos?"))
        if aula.bajarNotasAlumno(dni, bajada):
            print("Notas subidas ", bajada, " puntos")
        else:
            print("ERROR. Alumno no encontrado")

    elif opcion == 7:
        dni = int(input("Introduce el dni del alumno del que quieres obtener el nombre : "))
        print(aula.devolverNombreAlumno(dni))

    elif opcion == 8:
        print(aula.calcularNotaMedia())

    elif opcion == 9:
        print("La mayor nota del aula es ",aula.devolverNotaMayor())

    elif opcion == 10:
        puntuacion = float(input("Cuántos puntos? "))
        aula.subirTodasNotas(puntuacion)

    elif opcion == 0:
        print("muchas gracias")

    else:
        print("Opción incorrecta")
