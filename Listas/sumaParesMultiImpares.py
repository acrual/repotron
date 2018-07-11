from random import randint

N = 6

def rellenaVector(vector):
    for i in range(N):
        vector.append(randint(-3,3))

def muestraVector(vector):
    for i in range(len(vector)):
        print(vector[i], end = " ")
    print("")

def vectorResultado(vector1, vector2, vectorRes):
    for i in range(N):
        if i % 2 == 0:
            vectorRes.append(vector1[i] + vector2[i])
        else:
            vectorRes.append(vector1[i] * vector2[i])
    return vectorRes

vector1 = []
vector2 = []
vectorRes = []

rellenaVector(vector1)
rellenaVector(vector2)
muestraVector(vector1)
muestraVector(vector2)
vectorResultado(vector1, vector2, vectorRes)
print(vectorRes)
