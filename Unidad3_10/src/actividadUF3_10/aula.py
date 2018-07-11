from Alumno import Alumno

class Aula(object):

    def __init__(self, nombre = ""):
        self.nombre = nombre
        self.cuentas = []
        self.cantidad = 0

    def __str__(self):
        aux = "Banco " + self.nombre + "\nCuentas:\n"
        # print("self.cantidad es : ",self.cantidad)
        for i in range(self.cantidad):
            aux = aux + self.cuentas[i].__str__() + "\n"
        return aux + "Número de cuentas: " + str(self.cantidad) + "\n"

    def buscar(self, numero):
        enc = False
        i = 0
        while (i < self.cantidad and not enc):
            if self.cuentas[i].numero == numero:
                enc = True
            else:
                i = i + 1
        return i, enc

    def agregarNuevaCuenta(self, cuenta):
        if not self.buscar(cuenta.numero)[1]:
            self.cuentas.append(cuenta)
            self.cantidad = self.cantidad + 1
            return True
        return False

    def ingresar(self, numero, cantidad):
        pos, enc = self.buscar(numero)
        if enc:
            return self.cuentas[pos].ingresar(cantidad)
        return False

    def retirar(self, numero, cantidad):
        pos, enc = self.buscar(numero)
        if enc:
            return self.cuentas[pos].retirar(cantidad)
        return False

    def eliminarCuenta(self, numero):
        pos, enc = self.buscar(numero)
        if enc:
            self.cuentas.pop(pos)
            self.cantidad = self.cantidad - 1
            return True
        return False
