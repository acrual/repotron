N = 20

def esPrimo(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count = count + 1
    return count == 2

primos = []
posicion = 0
posiblePrimo = 2
while posicion < N:
        if esPrimo(posiblePrimo):
            primos.append(posiblePrimo)
            posicion = posicion + 1
        posiblePrimo = posiblePrimo + 1

print(primos)
