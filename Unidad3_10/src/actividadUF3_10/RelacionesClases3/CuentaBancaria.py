from Persona import Persona

class CuentaBancaria(object):

    def __init__(self, numero=0, titular = Persona(), saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return "Numero: " + str(self.numero) + "\nSaldo: " + str(self.saldo) + "euros\nTitular:" + self.titular.__str__()

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo = self.saldo + cantidad
            return True
        return False

    def retirar(self, cantidad):
        if cantidad > 0 and self.saldo - cantidad >= 0:
            self.saldo = self.saldo - cantidad
            return True
        return False

    def traspaso(self, destino, cantidad):
        if cantidad > 0 and (self.saldo - cantidad) >= 0:
            self.saldo = self.saldo - cantidad
            destino.saldo = destino.saldo + cantidad
            return True
        return False
