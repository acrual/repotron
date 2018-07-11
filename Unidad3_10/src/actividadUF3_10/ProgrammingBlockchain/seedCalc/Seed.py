from Words import Words
import itertools

class Seed(object):
    def __init__(self, list, words = ['w3','w4','w5','w6','w7','w8','w9','w10','w11','w12','w13','w14','w15','w16','w17','w18','w19','w20','w21','w22','w23']):
        self.words = list + words

    def __str__(self):
        cadena = ""
        for i in range(24):
            cadena = cadena + str(self.words[i]) + " "
        return cadena

    def wordposition(self, word):
        for i in range(len(self.words)):
            if self.words[i] == word:
                position = i
        return position

    def checkSeed(self):
        return True

    def moveWord(self, word, positions):
        position = self.wordposition(word)
        while position <= positions:
            aux = self.words[position]
            self.words[position] = self.words[position + 1]
            self.words[position + 1] = aux
            print(self)
            position = position + 1

    def moveBack1(self, position):
        aux = self.words[23]
        for i in range(len(self.words), position, -1):
            self.words[i - 1] = self.words[i - 2]
        self.words[position] = aux

    def moveBack2(self, mov):
        self.words = ['w0','w1','w2','w3','w4','w5','w6','w7','w8','w9','w10','w11','w12','w13','w14','w15','w16','w17','w18','w19','w20','w21','w22','w23']
        self.moveWord('w2', self.wordposition('w2') + mov)
        self.moveWord('w1', self.wordposition('w1') + mov)
        self.moveWord('w0', self.wordposition('w0') + mov)
