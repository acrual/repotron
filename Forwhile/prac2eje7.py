dia = int(input("Introduce el día :"))
mes = int(input("Introduce el mes :"))
año = int(input("Introduce el año :"))

if dia < 31 and dia > 0 and mes < 13 and mes > 0 and año <= 2018 and año >= 1975:
    print("La fecha es correcta")
else:
    print("La fecha no es correcta")
