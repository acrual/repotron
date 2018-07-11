# pedir dos números al usuario, el primero debe ser menor que el segundo y ambos >=2

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
#mostrar perfectos en el rango
print("")
print("PERFECTOS")
print("")

for i in range(num1,num2+1):
    sumaDivisores = 0
    for j in range(1,i):
        if i % j == 0:
            sumaDivisores = sumaDivisores + j
    if sumaDivisores == i:
        print(i," ")

#mostrar primos en el rango
print("")
print("PRIMOS")
print("")

for i in range(num1,num2+1):
    count = 0
    for j in range(2,i):
        if i % j == 0:
            count = count + 1
    if count == 0:
        print(i," ")
