#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 17:51:26 2018

@author: ubuntu
"""
from math import pi

class Figura(object):
    
    def __init__(self, color):
        self.color = color
        
    def __str__(self):
        return " de color " + str(self.color)
    
    def getColor(self):
        return self.color
    
    