from fraccion import Fraccion

numerador1 = int(input("Dame el numerador de la primera fracción : "))
denominador1 = int(input("Dame el denominador de la primera fracción : "))
numerador2 = int(input("Dame el numerador de la segunda fracción : "))
denominador2 = int(input("Dame el denominador de la segunda fracción : "))

f1 = Fraccion(numerador1,denominador1)
f2 = Fraccion(numerador2,denominador2)

print("Primera fracción es ",f1)
print("Primera fracción es ",f2)

opcion = 1
while opcion != 0:

    print("1. Hacer la suma de las dos fracciones")
    print("2. Hacer la resta de las dos fracciones")
    print("3. Hacer la multiplicación de las dos fracciones")
    print("4. Hacer la división de las dos fracciones")
    print("5. Calcular real de la primera fracción")
    print("6. Calcular real de la segunda fracción")
    print("7. Saber si ambas fracciones son equivalentes")
    print("0. Salir")

    opcion = int(input("Elige opción : "))
    if opcion == 1:
        print("La suma es ",f1.sumar(f2))

    elif opcion == 2:
        print("La resta es ",f1.restar(f2))

    elif opcion == 3:
        print("La multiplicación es ",f1.multiplicar(f2))

    elif opcion == 4:
        print("La division es ",f1.dividir(f2))

    elif opcion == 5:
        print("El resultado de la fracción f1 es ",f1.reducir())

    elif opcion == 6:
        print("El resultado de la fracción f2 es ",f2.reducir())

    elif opcion == 7:
        if f1.esEquivalente(f2):
            print("Son equivalentes")
        else:
            print("NO SON equivalentes")

    elif opcion == 0:

        print("Gracias por usar mi aplicación")

    else:
        print("Opción incorrecta")
