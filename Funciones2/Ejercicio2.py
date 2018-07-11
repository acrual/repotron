# menú para las operaciones primo, factorial, perfecto, productosumas y potenciaproductos
def esPrimo(num):
    for i in range(2,num-1):
        if num % i == 0:
            return False
    return True

def factorial(num):
    prod = 1
    for i in range(num,1,-1):
        prod = prod*i
    return prod

def esPerfecto(num):
    suma = 0
    for i in range(1,num):
        if num%i==0:
            suma = suma + i
    if suma == num:
        return True
    return False

def productoSumas(num1,num2):
    prodConSum = 0
    for i in range(num2):
        prodConSum = prodConSum + num1
    return prodConSum

def potenciaProducts(num1,num2):
    potConProd = 1
    for i in range(num2):
        potConProd = potConProd * num1
    return potConProd

def leerNumero(mensaje):
    num = int(input(mensaje))
    return num

def sonAmigos(a,b):
    totA = 0
    totB = 0
    for i in range(1,a):
        if a % i == 0:
            totA = totA + i
    for i in range(1,b):
        if b % i == 0:
            totB = totB + i
    if totA == b and totB == a:
        return True
    return False


def leerOpcion():
    print()
    print("1. Calcular si es primo")
    print("2. Calcular el factorial")
    print("3. Calcular si es perfecto")
    print("4. Calcula el producto con sumas")
    print("5. Calcula la potencia con productos")
    print("6. Verifica si dos números son amigos")
    print("0. Salir")
    opc = int(input("Introduce una opción: "))
    print("")
    return opc
    #PROGRAMA PRINCIPAL

opc = leerOpcion()
while opc != 0:     #JAMÁS VA A LLEGAR UN 0

    if opc >= 1 and opc <= 3:
        num1 = leerNumero("Introduce un número: ")
        while num1 < 2:
            num1 = leerNumero("Error. Introduce un número: ")

    elif opc == 4 or opc == 5:
        num1 = leerNumero("Introduce el primer número: ")
        num2 = leerNumero("Introduce el segundo número")
        while num1 < 1 or num2 < 1:
            num1 = leerNumero("Error. Introduce el primer número: ")
            num2 = leerNumero("Introduce el segundo número")

    elif opc== 6:
        num1 = leerNumero("Introduce el primer número: ")
        num2 = leerNumero("Introduce el segundo número")
        while num1 <= 2 or num2 <= 2:
            num1 = leerNumero("Error. Introduce el primer número: ")
            num2 = leerNumero("Introduce el segundo número")

    if opc == 1:
        if esPrimo(num1):
            print(" ")
            print("Es primo")
            print(" ")
        else:
            print(" ")
            print("No es primo")
            print(" ")

    elif opc == 2:
        print(" ")
        print("El factorial es ", factorial(num1))
        print(" ")

    elif opc == 3:
        if esPerfecto(num1):
            print(" ")
            print("Es perfecto")
            print(" ")
        else:
            print(" ")
            print("No es perfecto")
            print(" ")

    elif opc == 4:
        print(" ")
        print("El producto es : ", productoSumas(num1,num2))
        print(" ")

    elif opc == 5:
        print(" ")
        print("La potencia es : ", potenciaProducts(num1,num2))
        print(" ")

    elif opc == 6:
        if sonAmigos(num1,num2):
            print("Son amigos")
        else:
            print("No son amigos")

    else:
        print(" ")
        print("Error. Opción errónea")
        print(" ")

    opc = leerOpcion()
#FIN DEL WHILE
print("Has salido")
