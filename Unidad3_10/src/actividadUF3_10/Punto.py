
class Punto(object):

    #def __init__(self):
    #    self.x = 0
    #    self.y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Punto (" + str(self.x) + "," + str(self.y) + ")"

    def incrementarX(self, valor):
        self.x = self.x + valor

    def incrementarY(self, valor):
        self.y = self.y + valor

p1 = Punto(2,3)
p2 = Punto(1,-1)

print (p1)
print (p2)

p1.incrementarX(1)
p2.incrementarY(1)

print (p1)
print (p2)
