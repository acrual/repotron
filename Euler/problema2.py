#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:57:31 2018

@author: ubuntu
"""
a = 1
b = 2
c = a + b
print(a)
print(b)
suma = 0
while c < 4000000:
    a = b
    b = c
    #print(c)
    c = a + b
    if c % 2 == 0:
        print(c)
        suma = suma + c
        print(suma)

print("la suma es ",suma + 2)


    