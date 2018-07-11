# producto escalar de dos vectores. Función para rellenar los vectores solicitando
# al usuario valores entre 1 y 5
N = 3 #uso global porque la uso como si fuese una constante

def rellenarVector():
    numeros = [0,0,0]
    count = 0
    for i in range(N):
        numeros[i] = int(input("Dame valor del vector : "))
        while numeros[i] < 1 or numeros[i] > 5:
            numeros[i] = int(input("Error. Dame valor del vector : "))
    return numeros

def mostrarVector(vector):
    for i in range(N):
        print(vector[i], end = " ")
    print("")

def productoEscalar(vector1,vector2):
    producto = 0
    for i in range(N):
        producto = producto + vector1[i]*vector2[i]
    return producto

#PROGRAMA PRINCIPAL
vector1 = rellenarVector(N)
vector2 = rellenarVector(N)

mostrarVector(vector1)
mostrarVector(vector2)

print("El producto escalar de ambos vectores es ", productoEscalar(vector1, vector2))
