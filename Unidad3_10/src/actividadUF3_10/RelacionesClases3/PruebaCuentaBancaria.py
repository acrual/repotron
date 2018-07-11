from Persona import Persona
from CuentaBancaria import CuentaBancaria

titular1 = Persona("54321B", "Manolete")
titular2 = Persona("12345A", "Pepito")
cuenta1 = CuentaBancaria("1111111",200, titular1)
cuenta2 = CuentaBancaria("2222222",800, titular2)

opcion = 1
while opcion != 0:
    print("")
    print("1. Deseas hacer un ingreso? ")
    print("2. Deseas retirar dinero? ")
    print("3. Deseas mostrar los datos de la cuenta?")
    print("4. Deseas hacer un traspaso? ")
    print("0. Salir")
    print("")
    opcion = int(input("Introduce tu opción : "))

    if opcion == 1:
        cant =  float(input("Introduce cantidad a ingresar: "))
        if cuenta1.ingresar(cant):
            print("Cantidad ingresada correctamente")
        else:
            print("Cantidad no válida")
        print(cuenta1)

    elif opcion == 2:
        cant = float(input("Introduce cantidad a retirar: "))
        if cuenta1.retirar(cant):
            print("Cantidad retirada correctamente")
        else:
            print("Cantidad no válida o saldo insuficiente")

    elif opcion == 3:
        print(cuenta1.__str__())
        print(cuenta2.__str__())

    elif opcion == 4:
        cant = float(input("Qué cantidad? "))
        if cuenta1.traspaso(cuenta2,cant):
            print("Traspaso realizado correctamente")
        else:
            print("Cantidad no válida o saldo insuficiente")

    elif opcion == 0:
        print("¡Gracias!")

    else:
        print("Opción incorrecta")
