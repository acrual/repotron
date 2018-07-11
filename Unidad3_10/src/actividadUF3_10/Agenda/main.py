from Agenda import Agenda
from Contacto import Contacto

agenda = Agenda()

opcion = 1
while opcion != 0:
    print("1. Añadir contacto")
    print("2. Eliminar contacto")
    print("3. Consultar contacto")
    print("4. Modificar contacto")
    print("5. Mostrar listado")
    print("0. Salir")
    try:
        opcion = int(input("Escoger opcion: "))
        while opcion < 0 or opcion > 5:
            opcion = int(input("Opción incorrecta. Escoger opcion: "))
    except ValueError:
        print("Tipo de dato erróneo")
        opcion = int(input("Escoger opcion: "))
        while opcion < 0 or opcion > 5:
            opcion = int(input("Opción incorrecta. Escoger opcion: "))
            
        
    

    if opcion == 1:
        tel = int(input("Introduce el número de teléfono del nuevo contacto: "))
        nombre = input("Introduce el nombre del contacto: ")
        email = input("Introduce el email del contacto: ")
        nuevoContacto = Contacto(tel,nombre,email)
        if agenda.agregarContacto(nuevoContacto):
            print("Contacto añadido con éxito")
        else:
            print("Contacto ya existente.")

    elif opcion == 2:
        tel = int(input("Dime el teléfono del contacto que quieras eliminar: "))
        if agenda.eliminarContacto(tel):
            print("Contacto eliminado con éxito")
        else:
            print("Lo siento, ese contacto ya existe")

    elif opcion == 3:
        tel = int(input("Dime el teléfono del contacto que quieras consultar: "))
        posContactoABuscar = agenda.buscarPosicionTelefono(tel)
        if posContactoABuscar != -1:
            print(agenda.contactos[posContactoABuscar])
        else:
            print("Lo siento, no existe este contacto")

    elif opcion == 4:
        tel = int(input("Dime el teléfono del contacto que quieras modificar: "))
        contactillo = agenda.modificarContacto(tel)

    elif opcion == 5:
        print(agenda)

print("Agenda grabada en el fichero")
fichero = open("agenda.txt", "w")
fichero.write(agenda.__str__())
fichero.close()
