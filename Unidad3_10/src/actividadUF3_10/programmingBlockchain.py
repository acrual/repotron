# there are 22 possible positions for each missing word, taken 1 by 1, 2 by 2 and 3 by 3
# let's assume that the words start with a 'w' followed by a position in the list

def checkSeed(seed):
    # check that the seed is right
    return True

# first we take each of the 3 missing words and iterate them in every single position possible
# one by one. Let's assume that the missing words are w0, w1 and w2 and that they may not be
# in that particular order (may be w0,w1,w2 or w2,w1,w0 or w1,w2,w0, etc...)
for i in range(3):
    seed = ['w0','w1','w2','w3','w4','w5','w6','w7','w8','w9','w10','w11','w12','w13','w14','w15','w16','w17','w18','w19','w20','w21','w22','w23']
    if i == 0:
        if checkSeed(seed):
            print("0 this is the right seed: ",seed)
    for j in range(i, len(seed) - 1):
        print("La i es ",i," y la j es ",j)
        aux = seed[j]
        seed[j] = seed[j+1]
        seed[j+1] = aux
        if checkSeed(seed) or checkSeed(shuffle(seed[1:])):
            print("1- this is the right seed: ",seed)

# then two by two

for i in range(2):
    seed = ['w0','w1','w2','w3','w4','w5','w6','w7','w8','w9','w10','w11','w12','w13','w14','w15','w16','w17','w18','w19','w20','w21','w22','w23']
    for j in range(i, len(seed) - 2):
        if j == 0:
            print(seed)
            checkSeed(seed)
        print("la i es ", i, " la j es ",j)
        aux = seed[j+2]
        seed[j+2] = seed[j+1]
        seed[j+1] = seed[j]
        seed[j] = aux
        print(seed)
        checkSeed(seed)

# then three by three

seed = ['w0','w1','w2','w3','w4','w5','w6','w7','w8','w9','w10','w11','w12','w13','w14','w15','w16','w17','w18','w19','w20','w21','w22','w23']
for j in range(len(seed) - 3):
    if j == 0:
        print(seed)
        checkSeed(seed)
    print("la j es ",j)
    aux = seed[j+3]
    seed[j+3] = seed[j+2]
    seed[j+2] = seed[j+1]
    seed[j+1] = seed[j]
    seed[j] = aux
    print(seed)
    checkSeed(seed)
