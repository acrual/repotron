#el usuario tiene que adivinar un número y debemos ponerle un máximo número de intentos
# añadiéndole una condición al while
numAdivinar = 10
num = int(input("Introduce número : "))
conteo = 0
while num != numAdivinar and conteo <= 4:
    if num < numAdivinar:
        print("Un poco más alto ")
    elif num > numAdivinar:
        print("Un poco más bajo ")
    conteo = conteo + 1
    num = int(input("Introduce número : "))
if conteo == 5:
    print("PERDISTE!!")
else:
    print("ACERTASTE!!")
