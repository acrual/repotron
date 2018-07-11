contPares = 0
contImpares = 0
contCeros = 0
for i in range(5):
    num = int(input("Dame un número : "))
    if num % 2 == 0 and num!=0:
        contPares = contPares + 1

    elif num%2==1:
        contImpares = contImpares + 1
    else:
        contCeros = contCeros + 1
print("Hay : ", contPares, " pares ", contImpares, " impares y ", contCeros, " ceros ")
