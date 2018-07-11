#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 17:49:56 2018

@author: ubuntu
"""

from math import pi
from Figura import Figura

class Circulo(Figura):
    
    def __init__(self, color, radio):
        
        self.radio = radio
        super().__init__(color)
        self.forma = "circulo"
        self.area = pi * self.radio * self.radio
        
    def __str__(self):
        return "\n" + "Círculo " + super().__str__() + " con área " + str(self.area)
        