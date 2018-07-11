# pedir N números y controlar que estén en el rango 1-5
N = 4
for i in range(1,N + 1):
    num = int(input("Pedir número: "))
    while num > 5 or num < 1:
        num = int(input("Error. Introduce nuevo número: "))
print("Éxito")
