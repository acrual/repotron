import numpy as np

# opcion sin numpy
numeros = []

for i in range(25,36):
    numeros.append(i/3)

print("Sin numpy el resultado es: ",end="")
for i in range(len(numeros)):
    print(numeros[i],end=" ")
print("")
# opcion con numpy

Maxi = 11
j = 25
numeros = np.empty(11, dtype = np.float)

for i in range(Maxi):
    numeros[i] = j/3
    j = j + 1

print("Con numpy el resultado es: ",end="")
for i in range(Maxi):
    print(numeros[i],end=" ")
print("")
