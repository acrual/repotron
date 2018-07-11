nota = float(input("Dame la nota: "))

if nota >= 0 and nota < 5:
    print("SUSPENSO")

elif nota >= 5 and nota < 7:
    print("APROBADO")

elif nota >= 7 and nota < 9:
    print("NOTABLE")

elif nota >= 9 and nota <= 10:
    print("SOBRESALIENTE")

else:
    print("NOTA ERRÓNEA")
