# pedir N números enteros y mostrar los 2 mayores
N = 5

primero = int(input("Introduce un número : "))
segundo = int(input("Introduce un número : "))
if primero<segundo:
    aux = segundo
    segundo = primero
    primero = aux

for i in range(N-2): #0..N-3
    num = int(input("Introduce un número : "))
    if num>primero:
        segundo = primero
        primero = num
    elif num>segundo:
        segundo = num
print("El primero es ", primero)
print("El segundo es ", segundo)
