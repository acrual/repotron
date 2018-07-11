# calcular el factorial de un número
num = int(input("Introduce un número : "))
prod = 1
for i in range(num,1,-1):
    prod = prod*i
    
print(prod)
