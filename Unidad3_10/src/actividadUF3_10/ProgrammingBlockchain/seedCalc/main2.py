missingwords = ['w0','w1','w2']
knownwords = ['w3','w4','w5','w6','w7','w8','w9','w10','w11','w12','w13','w14','w15','w16','w17','w18','w19','w20','w21','w22','w23']
positions = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
res = [((x,a),(y,b),(z,c)) for x in missingwords
                            for y in missingwords if y != x
                            for z in missingwords if z != x and z != y
                            for a in positions
                            for b in positions if b != a
                            for c in positions if c != a and c != b]

def posicionMissingWords(sequence):
    seed = []
    for i in range(len(sequence)):
        if sequence[i][0] == 'w0':
            pos0 = sequence[i][1]
        elif sequence[i][0] == 'w1':
            pos1 = sequence[i][1]
        elif sequence[i][0] == 'w2':
            pos2 = sequence[i][1]
    return pos0,pos1,pos2

def ordenarPosiciones(pos0,pos1,pos2):
    lista = [(pos0, missingwords[0]), (pos1, missingwords[1]), (pos2, missingwords[2])]
    lista.sort()
    return lista

def crearSeed(posmenor, posintermedio, posmayor):
    seed = []
    contador = 0
    for i in range(24):
        if i < posmenor[0]:
            seed.append(knownwords[i-contador])
        elif i == posmenor[0]:
            seed.append(posmenor[1])
            contador = contador + 1
        elif i < posintermedio[0]:
            seed.append(knownwords[i-contador])
        elif i == posintermedio[0]:
            seed.append(posintermedio[1])
            contador = contador + 1
        elif i < posmayor[0]:
            seed.append(knownwords[i-contador])
        elif i == posmayor[0]:
            seed.append(posmayor[1])
            contador = contador + 1
        else:
            seed.append(knownwords[i-contador])
    return seed
conteo = 0

def checkSeed(outcome):

    if outcome == ['w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9', 'w10', 'w2', 'w11', 'w12', 'w13', 'w0', 'w14', 'w15', 'w16', 'w17', 'w18', 'w19', 'w1', 'w20', 'w21', 'w22', 'w23']:
        return True
    return False

for i in range(len(res)):
    pos0 = posicionMissingWords(res[i])[0]
    pos1 = posicionMissingWords(res[i])[1]
    pos2 = posicionMissingWords(res[i])[2]
    lista = ordenarPosiciones(pos0,pos1,pos2)
    seed = crearSeed(lista[0],lista[1],lista[2])
    print(seed)
    if seed[8] == 'w2' and seed[12] == 'w0' and seed[19] == 'w1':
        for j in range(len(seed)):
            print(seed[j], end = " ")
        break
    conteo = conteo + 1
print("")
print(conteo)
