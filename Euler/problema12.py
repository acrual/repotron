#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 12:42:56 2018

@author: ubuntu
"""

# números triángulos: 1+2+3+4+5+6+7+8+9...=> 1,3,6,10,15,21,28,36,45,55..

def obtenerDivisores(n):
    divisores = []
    #print("n es ", n)
    for i in range(1, n+1):
        if n % i == 0:
            divisores.append(i)
    return len(divisores)

def triangleNumbers(n):
    naturales = []
    triangles = []
    suma = 0
    for i in range(1, n):
        naturales.append(i)
        suma = suma + i
        triangles.append(suma)
    return triangles

def damePrimes(n):
    primos = []
    sum, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            primos.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return primos

# ME RINDO