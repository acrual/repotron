#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 13:08:32 2018

@author: ubuntu
"""
    
def isPalindrome(x):
    x = str(x)
    if len(x) == 6:
        if x[2] == x[3] and x[1] == x[4] and x[0] == x[5]:
            return x
    elif len(x) == 7:
        if x[0] == x[6] and x[1] == x[5] and x[2] == x[4]:
            return x

palindromes = []

for i in range(100,1000):
    for j in range(100, 1000):
        if isPalindrome(i * j):
            palindromes.append(i * j)

palindromes.sort(reverse = True)
print(palindromes, palindromes[0])
        


        
