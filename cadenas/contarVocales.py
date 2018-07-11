
def contarVocales(cad):

    cont = 0
    for i in range(len(cad)):
        if (cad[i] == 'a' or cad[i] == 'e' or cad[i] == 'i' or
        cad[i] == 'o' or cad[i] == 'u'):
            cont = cont + 1
    return cont

frase = input("Escribe una frase: ")
print("La frase ",frase,"tiene",contarVocales(frase),"letras vocales")
