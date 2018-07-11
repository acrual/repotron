#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 17:40:28 2018

@author: ubuntu
"""

from Persona import Persona

class Alumno(Persona):
    
    def __init__(self, dni = "", nombre ="", nota = 0.0, curso = 0):
        
        super().__init__(dni, nombre)
        self.nota = nota
        self.curso = curso
        
    def __str__(self):

        return "\n" + super().__str__() + "Nota: " + str(self.nota) + "\nCurso: " + str(self.curso)
    
    def getNota(self):
        return self.nota
    
    def setNota(self, nota):
        self.nota = nota
        
    def getCurso(self):
        return self.curso
    
    def setCurso(self, curso):
        self.curso = curso