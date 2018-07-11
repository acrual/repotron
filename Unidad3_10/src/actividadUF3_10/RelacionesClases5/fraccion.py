class Fraccion(object):

    def __init__(self, numerador = 1, denominador = 1):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return str(self.numerador) + "/" + str(self.denominador)

    def sumar(self, f):
        fSuma = Fraccion()
        fSuma.denominador = self.calcularMCM(self.denominador, f.denominador)
        fSuma.numerador = fSuma.denominador // self.denominador * self.numerador + fSuma.denominador // f.denominador * f.numerador
        fSuma.simplificar()
        return fSuma

    def restar(self, f):
        fResta = Fraccion()
        fResta.denominador = self.calcularMCM(self.denominador, f.denominador)
        fResta.numerador = fResta.denominador // self.denominador * self.numerador - fResta.denominador // f.denominador * f.numerador
        fResta.simplificar()
        return fResta

    def multiplicar(self, f):
        fMultiplicacion = Fraccion()
        fMultiplicacion.denominador = self.denominador * f.denominador
        fMultiplicacion.numerador = self.numerador * f.numerador
        fMultiplicacion.simplificar()
        return fMultiplicacion

    def dividir(self, f):
        fDivision = Fraccion()
        fDivision.denominador = self.denominador * f.numerador
        fDivision.numerador = self.numerador * f.denominador
        fDivision.simplificar()
        return fDivision

    def reducir(self):
        return self.numerador/self.denominador

    def calcularMCM(self,a,b):
        mcm = b
        if a > b:
            mcm = a
            #seguir mientras no sea divisor de alguno
        while mcm % a != 0 or mcm % b != 0:
            mcm = mcm + 1
        return mcm

    def calcularMCD(self,a,b):
        mcd = b
        if a < b:
            mcd = a
        while a % mcd != 0 or b % mcd != 0:
            mcd = mcd - 1
        return mcd

    def esSimplificable(self):
        return self.calcularMCD(self.numerador,self.denominador) > 1

    def esEquivalente(self, f):
        return self.numerador * f.denominador == self.denominador * f.numerador

    def simplificar(self):
        if (self.esSimplificable()):
            mcd = self.calcularMCD(self.numerador, self.denominador)
            self.numerador = self.numerador // mcd
            self.denominador = self.denominador // mcd
