from random import randint


N = 3
def rellenaVector(vector):
    for i in range(N):
        vector.append(randint(1,5))

def muestraVector(vector):
    for i in range(len(vector)):
        print(vector[i], end = " ")
    print("")

def sumaVectores(vector1,vector2, vectorSuma):
    for i in range(N):
        vectorSuma.append(vector1[i] + vector2[i])

vector1 = []
vector2 = []
vRes=[]
rellenaVector(vector1)
rellenaVector(vector2)
muestraVector(vector1)
muestraVector(vector2)
sumaVectores(vector1,vector2,vRes)
muestraVector(vRes)
