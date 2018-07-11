# lista dinámica de primoas entre 2 y 100

N = 100

def esPrimo(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count = count + 1
    return count == 2

def rellenar(lista):
    for i in range(2,N):
        if esPrimo(i):
            lista.append(i)

def mostrar(lista):
    for i in range(len(lista)):
        print(lista[i], end =" ")

primos = []
rellenar(primos)
mostrar(primos)
