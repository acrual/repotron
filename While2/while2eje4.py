#cociente y resto mediante restas
num1 = int(input("Introduce el primer número : "))
num2 = int(input("Introduce el segundo número : "))

#FORMA 1
conteo = 0
if num2 <= num1:
    for i in range(num2,num1+1,num2):
        conteo = conteo + 1
print("El cociente es ", conteo, " y el resto ", num1%num2)

#FORMA 2
conteo = 0
while num1 >= num2:
    num1 = num1 - num2
    conteo = conteo + 1
print("El cociente es ", conteo, " y el resto ", num1)
#resta  8-6-
#num1   8-8
#num2   2-2
#conteo 0-1
