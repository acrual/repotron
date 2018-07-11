#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 16:56:12 2018

@author: ubuntu
"""

class Persona(object):
    
    def __init__(self, dni = "", nombre = ""):
        self.dni = dni
        self.nombre = nombre
        
    def __str__(self):
        return "Nombre: " + str(self.nombre) + "\nDNI: " + str(self.dni) + "\n"
    
    def getDni(self):
        return self.dni
    
    def setDni(self, dni):
        self.dni = dni
    
    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre