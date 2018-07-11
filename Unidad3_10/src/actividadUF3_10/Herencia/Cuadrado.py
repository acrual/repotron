#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 17:49:43 2018

@author: ubuntu
"""
from math import pi
from Figura import Figura

class Cuadrado(Figura):
    
    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado
        self.area = self.lado * self.lado
        
    def __str__(self):
        return "\n" + "Círculo " + super().__str__() + " con área " + str(self.area) 
        