#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 11:52:16 2018

@author: ubuntu
"""

def sumPrimes(n):
    sum, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum

print(sumPrimes(2000000))

def damePrimes(n):
    primos = []
    sum, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            primos.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return primos

print(damePrimes(200))
#142913828922