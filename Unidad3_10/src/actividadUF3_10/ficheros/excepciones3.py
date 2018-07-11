
dividir = False
while not dividir:
    correcto = False
    while not correcto:
        try:
            numero1 = float(input("Dame primer número: "))
            numero2 = float(input("Dame segundo número: "))
            correcto = True

        except:
            print("ERROR. Tipos incorrectos")

    try:
        print("La división es ",numero1/numero2)
        dividir = True
    except:
        print("No se puede hacer esta división. Vuelve a introducir nuevos datos")
