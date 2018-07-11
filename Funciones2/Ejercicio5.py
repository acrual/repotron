# una función en la que se piden N números al usuario y devuelve cuantos han sido pares e impares
# el cero no se tiene en cuenta pq python lo cuenta como par
# otra función que pide N números y te devuelven cuántos son positivos, cuántos negativos y ceros
N = 5 #hacemos uso global de ella

def contarParesImpares():
    contPares = 0
    contImpares = 0
    for i in range(N):
        num = int(input("Introduce número :"))
        if num % 2 == 0 and num != 0:
            contPares = contPares + 1
        elif num % 2 == 1:
            contImpares = contImpares + 1
    return contPares, contImpares


def contarPositivosNegativosCeros():
    contPos = 0
    contNeg = 0
    contCeros = 0
    for i in range(N):
        num = int(input("Introduce número :"))
        if num > 0:
            contPos = contPos + 1
        elif num < 0:
            contNeg = contNeg + 1
        else:
            contCeros = contCeros + 1
    return contPos, contNeg, contCeros

pares,impares = contarParesImpares()
print("Hay ", pares, " pares y ", impares, " impares ")
pos, neg, ceros = contarPositivosNegativosCeros()
print("Hay ", pos, " positivos ", neg, " negativos ", ceros, " ceros ")
