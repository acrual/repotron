def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a//b

def leerOpcion():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplica")
    print("4. Divide")
    print("0. Salir")
    opc = int(input("Introduce una opción: "))
    return opc

opcion = leerOpcion()
while opcion != 0:

    if opcion >= 1 and opcion <=4:
        num1 = int(input("Introduce el primero número: "))
        num2 = int(input("Introduce el segundo número: "))
        if opcion == 4:
            while(num2 == 0):
                print("ERROR. El divisor no puede ser 0")
                num2 = int(input("Introduce el segundo número: "))

    if opcion == 1:
        print(sumar(num1,num2))
    elif opcion == 2:
        print(restar(num1,num2))
    elif opcion == 3:
        print(multiplicar(num1,num2))
    elif opcion == 4:
        print(dividir(num1,num2))
    else:
        print("Opción errónea")

    opcion = leerOpcion()
