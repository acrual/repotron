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

def esPrimo(num):
    conteo = 0
    for i in range(1,num+1):
        if num%i==0:
            conteo = conteo + 1
    if conteo == 2:
        return True
    return False


num = int(input("Introduce un número :"))
while num < 2:
    print("Error, no puede ser menor que 2 ")
    num = int(input("Introduce un número :"))

if esPerfecto(num):
    print("Es perfecto")
else:
    print("No es perfecto")
print("El factorial de ", num, " es ", factorial(num))
if esPrimo(num):
    print("Es primo")
else:
    print("No es primo")
