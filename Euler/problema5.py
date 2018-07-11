    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:10:57 2018

@author: ubuntu
"""
# con 2520 son todos los divisores 1, 2, 3, (2*2), 5, 7, (2*2*2), (3*3), 2*5
# en LIST hacemos lo mismo, pero desde el 11 hasta el 20.

LIST = [11, 13, 2, 17, 19]

for i in range(100000):
    cont = 0
    for j in range(len(LIST)):
        if i % LIST[j] == 0:
            cont = cont + 1
        if cont == 5:
            res = i
            break

print("resultado es ", res * 2520)
            