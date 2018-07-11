# clase fecha

class Fecha(object):

    def __init__(self, dd="1", mm="1", aaaa="2018"):
        self.dd = dd
        self.mm = mm
        self.aa = aaaa

    def __str__(self):
        return str(self.dd) + "/" + str(self.mm) + "/" + str(self.aa) + "\n"
