#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 17:04:42 2018

@author: ubuntu
"""
from Persona import Persona

class Profesor(Persona):
    
    def __init__(self, dni = "", nombre = "", departamento = "", sueldo = 0.0):
        #self.dni = dni
        #self.nombre = nombre
    
        super().__init__(dni, nombre)
        self.departamento = departamento
        self.sueldo = sueldo
    
    def __str__(self):
        return super().__str__() + "Departamento: " + str(self.departamento) + "\nSueldo: " + str(self.sueldo)
        
    def getDepartamento(self):
        return self.departamento
    
    def setDepartamento(self, departamento):
        self.departamento = departamento
        
    def getSueldo(self):
        return self.sueldo
    
    def setSueldo(self, sueldo):
        self.sueldo = sueldo