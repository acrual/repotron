from Seed import Seed
from Words import Words
import itertools

sequence = ['w0', 'w1', 'w2']
permutaciones = list(itertools.permutations(sequence))
print(permutaciones)

for k in range(len(list(itertools.permutations(sequence)))):
    seed = Seed(list(permutaciones[k]))
    for i in range(2, len(seed.words) - 1):
        for j in range(i, len(seed.words) - 1):
            seed.moveWord(seed.words[j], len(seed.words) - 2)
            seed.moveBack1(j+1)
            seed.moveWord(seed.words[j-1],j-1)
        seed.moveBack2(i-2)
