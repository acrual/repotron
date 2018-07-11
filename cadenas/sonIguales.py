
def devolverMenor(f1,f2):
    if len(f1) < len(f2):
        cadenaMenor = f1
    elif len(f1) == len(f2):
        cadenaMenor = f1
        

def sonIguales(f1,f2):
    i = 0
    while f2[i] == f1[i] and i < len :
        i = i + 1
        if i == len(f1):
            return True
    return False

frase1 = input("Dime la primera frase: ")
frase2 = input("Dime la segunda frase: ")
if sonIguales(frase1,frase2):
    print("Son iguales")
else:
    print("No son iguales")
