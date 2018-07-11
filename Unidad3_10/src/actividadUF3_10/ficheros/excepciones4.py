
try:
    numero1 = int(input("Dame primer número: "))
    numero2 = int(input("Dame segundo número: "))
    print("La división es ",numero1 // numero2)

except ValueError:
    print("Tipo de dato erróneo")
except ZeroDivisionError:
    print("No se puede dividir por cero")
