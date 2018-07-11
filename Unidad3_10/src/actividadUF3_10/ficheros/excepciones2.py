todobien = False
while not todobien:
    try:
        numero1 = float(input("Dame primer número: "))
        numero2 = float(input("Dame segundo número: "))
        print("La suma es ",numero1 + numero2)
        todobien = True
    except:
        print("Tipo de dato erróneo")
