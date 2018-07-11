# -*- coding: utf-8 -*-
'''
Created on 16 ene. 2017

@author: profesoresi
'''

class Alumno(object):
    '''
    Crear clase Alumno con dos atributos, nombre y deportes, 
    deportes será una  lista de los deportes que practica cada Alumno
    '''

    '''
    Constructor
    Que le asigne el valor al atributo nombre e 
    inicialice el atributo deportes a una lista vacía
    '''
    def __init__(self, nombre):
        self.nombre=nombre
        self.deportes=[]
        
        
    def __str__(self):
        valor = 'El alumno ' + self.nombre + ' practica:'
        for dep in self.deportes:
            valor = valor + ' ' + dep
        return valor 
      
    