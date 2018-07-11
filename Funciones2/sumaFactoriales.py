#pedir número y hacer la suma de los factoriales desde cero hasta ese número
def calcularFactorial(a):
    prod = 1
    for i in range(1,a+1):
        prod = prod * i
    return prod

num = int(input("Pedir número: "))
while num < 0:
    num = int(input("Error. Pedir número: "))

sumaFactorial = 0

for i in range (num + 1):
    sumaFactorial = sumaFactorial + calcularFactorial(i)
print(sumaFactorial)
