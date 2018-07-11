
class Words(object):
    def __init__(self, word):
        self.name = word
        if self.name == w0 or self.name == w1 or self.name == w2:
            self.known = False
        else:
            self.known = True

    def __str__(self):
        return self.name
