# -*- coding: utf-8 -*-
'''
Created on 16 ene. 2017

@author: profesoresi
'''

class Punto(object):
    '''
    Representación de un punto en el plano, los atributos
    son x e y que representan los valores de las coordenadas
    cartesianas.
    '''
    
    '''
    Constructor
    '''
    def __init__(self, x=0, y=0):
        # Constructor de Punto, x e y deben ser numéricos
        if self.es_numero(x) and self.es_numero(y):
            self.x=x
            self.y=y
        else:
            raise TypeError("x e y deben ser valores numéricos")

    def es_numero(self, valor):
        ''' Indica si un valor es numérico o no. '''
        return isinstance(valor, (int, float, long, complex))
    
    
    def restar(self, otro):
        ''' Devuelve un nuevo punto, con la resta entre dos puntos. '''
        return Punto(self.x - otro.x, self.y - otro.y)


    def norma(self):
        ''' Devuelve la norma del vector que va desde el origen
        hasta el punto. '''
        return (self.x*self.x + self.y*self.y)**0.5
    
        
    def distancia(self, otro):
        ''' Devuelve la distancia entre ambos puntos. '''
        pr = self.restar(otro)
        n = pr.norma()
        return n


    def __add__(self, otro):
        """ Devuelve la suma de ambos puntos. """
        return Punto(self.x + otro.x, self.y + otro.y)
 
    
    def __sub__(self, otro):
        """ Devuelve la resta de ambos puntos. """
        return Punto(self.x - otro.x, self.y - otro.y)


    def __str__(self):
        """ Muestra el punto como un par ordenado. """
        return"(" + str(self.x) + ", " + str(self.y) + ")"
        