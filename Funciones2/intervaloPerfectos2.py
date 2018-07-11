# lo mismo que intervaloPerfectos pero con función esPerfecto()
def esPerfecto(num):
    suma = 0
    for i in range(1,num):
        if num % i == 0:
            suma = suma + i
    if suma == num:
        return True
    return False

def esPrimo(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        return True
    return False

def mostrarPerfectos(a,b):
    print("PERFECTOS:",end = " ")
    for i in range(a,b+1):
        if esPerfecto(i):
            print(i,end = " ")

def mostrarPrimos(a,b):
    print("PRIMOS: ", end = "")
    for i in range(a,b+1):
        if esPrimo(i):
            print(i, end = " ")

#fuerzo a que entre la primera vez
num1 = 2
num2 = 1
while num1 >= num2:
    num1 = int(input("Dame el primer número: "))
    while num1 < 2:
        num1 = int(input("Error, debe ser mayor o igual que 2. Dame el primer número: "))
    num2 = int(input("Dame el segundo número: "))
    while num2 < 2:
        num2 = int(input("Error, debe ser mayor o igual que 2. Dame el segundo número: "))
    if num1 >= num2:
        print("Error. El primero debe ser menor que el segundo")

print("")
mostrarPerfectos(num1,num2)
print("")
mostrarPrimos(num1,num2)
print("")
