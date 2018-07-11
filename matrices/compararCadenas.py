def mismoTamano(cadena1, cadena2):
    if len(cadena1) == len(cadena2):
        return True
    else:
        return False

def sonIguales(cadena1, cadena2):
    i = 0
    while i < len(cadena1) and cadena1[i] == cadena2[i]:
        i = i + 1
    if i == len(cadena1):
        return True
    return False

cadena1 = input("Dame la cadena 1: ")
cadena2 = input("Dame la cadena 2: ")

if mismoTamano(cadena1, cadena2):
    if sonIguales(cadena1, cadena2):
        print("Son iguales")
    else:
        print("NO son iguales")
else:
    print("NO son iguales")
