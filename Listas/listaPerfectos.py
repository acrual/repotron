# lista de los 5 primeros números perfectos con y sin append

N = 4

def perfectosAppend():
    perfectos = []
    count = 0
    i = 1
    while count < N:
        i = i + 1
        sum = 0
        for j in range(1, i):
            if i % j == 0:
                sum = sum + j
            #print(j, end=" ")
        if sum == i:
            #print(i," es perfecto ")
            count = count + 1
            perfectos.append(i)
    return perfectos

def perfectosSinAppend():
    perfectos = [0,0,0,0]
    i = 1
    count = 0
    while count < N:
        i = i + 1
        sum = 0
        for j in range(1, i):
            if i % j == 0:
                sum = sum + j
            #print(j, end=" ")
        if sum == i:
            #print(i," es perfecto ")
            perfectos[count] = i
            count = count + 1

    return perfectos

res = perfectosAppend()
print(res)
res2 = perfectosSinAppend()
print(res2)
