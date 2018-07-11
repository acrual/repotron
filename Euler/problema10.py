#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 15:21:11 2018

@author: ubuntu
"""
def sumaPrimos(n):
    suma, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            suma += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return suma
            
            
print(sumaPrimos(2000000))
        