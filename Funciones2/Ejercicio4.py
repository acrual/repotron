#mostrar tabla de multiplicar para cualquier número
N = 10 #la tratamos con constante y global

def tablaMultiplica(num):
    for i in range(1,N+1): #uso global de la N
        print(num," por ", i, " igual a ", num*i)
    return

numero = int(input("De qué número quieres la tabla de multiplicar? : "))
tabla = tablaMultiplica(numero)
