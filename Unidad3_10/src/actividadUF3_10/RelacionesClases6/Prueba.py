from Alumno import Alumno

alumno = Alumno("1111A", "Marta", [6,7,8])

opcion = 1
while opcion != 0:
    print(alumno)
    print("")
    print("1. Subir una nota ")
    print("2. Bajar una nota ")
    print("3. Subir todas las notas")
    print("4. Bajar todas las notas")
    print("0. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        pos = int(input("¿Qué nota quieres subir? "))
        val = int(input("¿Cuántos puntos?"))
        alumno.subirNota(pos,val)

    elif opcion == 2:
        pos = int(input("¿Qué nota quieres bajar? "))
        val = int(input("¿Cuántos puntos?"))
        alumno.bajarNota(pos,val)

    elif opcion == 3:
        val = int(input("¿Cuántos puntos? "))
        alumno.subirTodasNotas(val)

    elif opcion == 4:
        val = int(input("¿Cuántos puntos? "))
        alumno.bajarTodasNotas(val)

    elif opcion == 0:
        print("muchas gracias")

    else:
        print("Opción incorrecta")
