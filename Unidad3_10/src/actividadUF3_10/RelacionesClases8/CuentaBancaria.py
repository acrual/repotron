from Persona import Persona
from random import randint

class CuentaBancaria(object):

    comision = 2

    def __init__(self, numero=0, titular = Persona(), saldo=0.0, interes =0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.interes = randint(1,5)

    def __str__(self):
        return "Numero: " + str(self.numero) + "\nSaldo: " + str(self.saldo) + "euros\nTitular:" + self.titular.__str__() + "\nInterés:" + str(self.interes)

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

    def traspasar(self, destino, cantidad):
        if cantidad > 0 and (self.saldo - cantidad) >= 0:
            self.saldo = self.saldo - cantidad
            self.saldo = self.saldo - (self.saldo * CuentaBancaria.comision) / 100
            destino.saldo = destino.saldo + cantidad
            return True
        return False

    def pagarIntereses(self):
        self.saldo = self.saldo + (self.saldo * self.interes)/100
