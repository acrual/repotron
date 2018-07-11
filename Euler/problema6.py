#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 17:10:42 2018

@author: ubuntu
"""
suma = 0
for i in range(1, 101):
    suma = suma + i
primerasuma = suma * suma
print(primerasuma)

suma2 = 0
for i in range(1,101):
    suma2 = suma2 + (i * i)

print(primerasuma - suma2)
    