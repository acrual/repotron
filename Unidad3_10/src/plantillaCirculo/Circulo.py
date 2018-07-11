# -*- coding: utf-8 -*-
'''
Created on 30 ene. 2017

@author: profesoresi
'''
class Figura(object):
    
    
    def __init__(self, nombre):
        self.nombre = nombre
    
class Circulo(Figura):
    '''
    classdocs
    '''
    pi = 3.14
    superficie = 0.0
    circunferencia = 0.0

    def __init__(self, radio=1, nombre='Círculo'):
        # antes de asignar valores valido los parámetros radio y nombre
        # Si el valor de radio es numérico, podré realizar la asignación
        if isinstance(radio, (int, long, float)):
            # valido que nombre sea igual a circulo
            if nombre == 'Circulo':
                Figura.__init__(self, nombre)
                self.radio = radio
            else:
                raise Exception('El objeto debe tener nombre Círculo')
        else:
            raise Exception('El radio debe ser numérico')
        
        
    def calcularSuperficie(self):
        self.superficie = self.pi * (self.radio ** 2)
        
        if self.superficie%2 == 0:
            print 'El círculo tiene superficie PAR'
        else:
            print 'El círculo tiene superficie IMPAR'
            
            
    def calcularCircunferencia(self):
        self.circunferencia = 2 * self.pi * self.radio
        
        if self.circunferencia > 15:
            print 'El valor de la circunferencia es mayor que 15'
        else:
            print 'El valor de la circunferencia es menor o igual que 15'
            
    
    def __str__(self):
        return 'El círculo de radio ' + str(self.radio) + ' tiene una superficie de ' + str(self.superficie) + ' y una circunferencia de ' + str(self.circunferencia)