def esMayor(cadena1, cadena2):
    #True si la cadena1 es > cadena2
    #False en caso contrario
    if len(cadena1) > len(cadena2):
        return True
    return False

def sonIguales(cadena1, cadena2):
    i = 0

    if esMayor(cadena1, cadena2):
        while i < len(cadena2) and cadena1[i] == cadena2[i]:
            i = i + 1
        if i == len(cadena2):
            return True
        return False

    else:
        while i < len(cadena1) and cadena1[i] == cadena2[i]:
            i = i + 1
        if i == len(cadena1):
            return True
        return False

#PROGRAMA PRINCIPAL

cadena1 = input("Dame la cadena 1: ")
cadena2 = input("Dame la cadena 2: ")

if sonIguales(cadena1, cadena2):
    print("Son iguales")
else:
    print("NO son iguales")
