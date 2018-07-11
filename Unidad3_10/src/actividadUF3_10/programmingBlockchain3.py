from itertools import *

#first we move w2 to the end. Then we do the same but when w2 moves one position, w1 moves one too
#then when both w1 and w2 reach the end, we start again and move both one position to the right
#once we move both to the right, we move w0 one position to the right too.
def checkSeed(seed):
    # check that the seed is right
    return True

def knowPositions(list, word1, word2, word3):
    for i in range(len(list)):
        if list[i] == word1:
            position1 = i
        if list[i] == word2:
            position2 = i
        if list[i] == word3:
            position3 = i
    return position1, position2, position3

def moveNewWordIn(sequence):
    if sequence[0] != w0:
        print("calidad")

def listas():
    knownwords = []
    for i in range(3,24):
        knownwords.append('w'+str(i))
        # print(knownwords)
    missingwords = ['w0', 'w1', 'w2']
    return missingwords, knownwords

def permutations(missingwords, knownwords):
    seed = list(permutations(missingwords,3))
    # seed = list(seed)
    for i in range(len(seed)):
        seed[i] = list(seed[i])
        complete = seed[i] + knownwords
    return(complete)

print(listas())
print(permutations(listas()[0],listas()[1]))
