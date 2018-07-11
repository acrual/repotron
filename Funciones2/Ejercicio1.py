#sacar si es número primo de manera más eficiente
def esPrimo(num):
    for i in range(2,num-1):
        if num % i == 0:
            return False
    return True

def esPrimo2(num):
    primo = True
    for i in range(2,num-1):
        if num % i == 0:
            primo = False
    if primo == True:
        print("El ",num,"es primo")
    else:
        print("El",num,"NO es primo")

def esPrimo3():
    num = int(input("Introduce número: "))
    for i in range(2,num-1):
        if num % i == 0:
            return False
    return True

numero = int(input("Introduce número :"))

if esPrimo(numero):
    print("Es primo")
else:
    print("No lo es")

esPrimo2(numero)

if esPrimo3():
    print("Es primo")
else:
    print("NO es primo")
