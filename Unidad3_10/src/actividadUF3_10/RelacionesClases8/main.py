from Banco import Banco
from CuentaBancaria import CuentaBancaria
from Persona import Persona

banco = Banco("Santander")

opcion = 1
while opcion != 0:

    print("1. Agregar cuenta ")
    print("2. Eliminar cuenta ")
    print("3. Mostrar Banco ")
    print("4. Ingresar en una cuenta")
    print("5. Retirar de una cuenta")
    print("6. Traspasar entre cuentas")
    print("7. Liquidar intereses")
    print("0. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        numeroCuenta = int(input("Por favor dame el número de cuenta: "))
        dniTitular = input("Por favor dame el DNI del titular: ")
        nombreTitular = input("Por favor dame el nombre del titular: ")
        titular = Persona(dniTitular, nombreTitular)
        cuenta = CuentaBancaria(numeroCuenta, titular)
        if banco.agregarNuevaCuenta(cuenta):
            print("Cuenta agregada")
        else:
            print("Cuenta duplicada")

    elif opcion == 2:
        numeroCuenta = int(input("Dame el número de cuenta a eliminar: "))
        if banco.eliminarCuenta(numeroCuenta):
            print("Cuenta eliminada")
        else:
            print("Cuenta no encontrada")

    elif opcion == 3:
        print(banco)

    elif opcion == 4:
        numero = int(input("Dime en qué cuenta quieres ingresar : "))
        cantidad = float(input("Cuánto quieres ingresar? "))
        if banco.ingresar(numero, cantidad):
            print("Cantidad ingresada en la cuenta ", numero)
        else:
            print("Lo siento, no hemos encontrado esa cuenta")

    elif opcion == 5:
        numero = int(input("Dime en qué cuenta quieres retirar : "))
        cantidad = float(input("Cuánto quieres retirar? "))
        if banco.retirar(numero, cantidad):
            print("Cantidad retirada en la cuenta ", numero)
        else:
            print("Lo siento, no tiene saldo suficiente")

    elif opcion == 6:
        origen = int(input("Dime desde que cuenta quieres transferir"))
        destino = int(input("Dime a qué cuenta quieres transferir"))
        cantidad = int(input("Dime cuánto quieres transferir"))
        if banco.traspasar(origen, destino, cantidad):
            print("Cantidad traspasada entre cuenta ", origen, " y destino ", destino)
        else:
            print("Cuenta no encontrada o saldo insuficiente")

    elif opcion == 7:
        banco.liquidarIntereses()
        print("Intereses liquidados")

    elif opcion == 0:
        print("muchas gracias")

    else:
        print("Opción incorrecta")
