num1 = int(input("Dame el número 1:"))
num2 = int(input("Dame el número 2:"))
num3 = int(input("Dame el número 3:"))
if num3 >= num1 and num3 <= num2:
    print ("Está entre los dos números")

elif num3 < num1:
    print("Es inferior al primer número")

else:
    print("Es superior al segundo número")
