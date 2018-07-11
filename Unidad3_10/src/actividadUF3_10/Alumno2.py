# -*- coding: utf-8 -*-
'''
Created on 16 ene. 2017

@author: profesoresi
'''

class Alumno2(object):
    '''
    Crear clase Alumno con dos atributos, nombre y deportes, 
    deportes será una  lista de los deportes que practica cada Alumno
    '''

    '''
    Constructor
    '''
    def __init__(self, nombre, *arbitrarios):
        self.nombre=nombre
        self.deportes=[]
        for parametro in arbitrarios:
            self.deportes.append(parametro)
                
    def __str__(self):
        valor = 'El alumno ' + self.nombre + ' practica:'
        for dep in self.deportes:
            valor = valor + ' ' + dep
        return valor 
      
    