#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:13:51 2018

@author: ubuntu
"""
def isPrime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def divisores(a):
    for i in range(2,1000000):
        if a % i == 0:
            if isPrime(i):
                print("El divisor primo es, ",i)

print(87625999/1471)
print(divisores(59569))

#600851475143
#
            
        