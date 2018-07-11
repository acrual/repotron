# pedir números enteros hasta que el usuario introduzca uno negativo. Calcular la media
# de dichos números (sin tener en cuenta la marca del final)
sum = 0
conteo = 0

num = int(input("Introduce un número : "))
while num >= 0:
    sum = sum + num
    conteo = conteo + 1
    num = int(input("Introduce un número : "))

print("La media es ", sum/conteo)
print("Acabado el proceso")
