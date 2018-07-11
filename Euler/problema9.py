#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 12:23:58 2018

@author: ubuntu
"""

for c in range(10, 999):
    for b in range(c):
        for a in range(b):
            if (a + b + c) == 1000:
                print(a, b, c)
                if (a * a) + (b * b) == (c * c):
                    lape = a
                    lamed = b
                    lagran = c
                    res = a * b * c

print("res es ", res, lape, lamed, lagran)
            
            
           
