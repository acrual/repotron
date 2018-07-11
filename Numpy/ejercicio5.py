import numpy as np

letras = []
for i in range(ord('A'), ord('Z') + 1):
    letras.append(chr(i))

datos = input("Dame una secuencia de letras: ")
# opcion sin numpy
resultado = []
j = 0
for i in range(len(datos)):
    if datos[i] in letras:
        if i == 0:
            resultado.append(datos[0])
        elif ord(datos[i]) > ord(resultado[j]):
            resultado.append(datos[i])
            j = j + 1

print("El resultado es ", resultado)

#TAL COMO INDICA EL ENUNCIADO, CON VALOR CENTINELA
#PIDIENDO LAS LETRAS DE UNA EN UNA
resultado2 = []
i = 1
aux = input("Introduce letra")
letra = aux[0]
if letra != '$':
    resultado2.append(letra)

while letra != '$':
    aux = input("Introduce letra")
    letra = aux[0]
    if letra >= 'A' and letra <= 'Z':
        if letra > resultado2[i - 1]:
            resultado2.append(letra)
            i = i + 1
print(resultado2)
