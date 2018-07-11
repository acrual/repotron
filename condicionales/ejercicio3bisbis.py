nota = float(input("Dame la nota: "))

if  5 > nota >= 0:
    print("SUSPENSO")

elif 7 > nota >= 5:
    print("APROBADO")

elif 9 > nota >= 7:
    print("NOTABLE")

elif 10 >= nota >= 9:
    print("SOBRESALIENTE")

else:
    print("NOTA ERRÓNEA")
