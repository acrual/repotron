#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 18:43:52 2018

@author: ubuntu
"""

for i in range(1001):
    sum = 0
    print(i, 2**i, end = " ")
    for j in range(len(str(2**i))):
        sum = sum + int(str(2**i)[j])
    print(sum)