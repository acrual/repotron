
# -*- coding: utf-8 -*-
'''
Created on 16 ene. 2017

@author: profesoresi
'''
from actividadUF3_10.Alumno import Alumno
from actividadUF3_10.Alumno2 import Alumno2

def main():
    alumno = Alumno('Luis')
    alumno2 = Alumno2('Pablo', 'fútbol', 'natación', 'baloncesto')
    alumno3 = Alumno2('Roberto')

    print alumno
    print alumno2
    print alumno3

main()
