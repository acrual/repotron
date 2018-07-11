#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:30:54 2018

@author: ubuntu
"""
contar = 2
for i in range(110000):
    j = 2
    while i % j != 0 and j < i:
        if j == i - 1:
            print(i, contar)
            contar = contar + 1
        j = j + 1


        