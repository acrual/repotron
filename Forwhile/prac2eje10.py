num1 = int(input("Introduce el primer número :"))
num2 = int(input("Introduce el segundo número :"))
num3 = int(input("Introduce el tercer número :"))

if num3 > num1 and num3 > num2:
    print(num3)
elif num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)

else:
    print("te has equivocado en algo")
