# -*- coding: utf-8 -*-
'''
Created on 30 ene. 2017

@author: profesoresi
'''
from plantillaCirculo.Circulo import Circulo

def main():
    try:
        circulo = Circulo(2,'Cuadrado')
        
        circulo.calcularSuperficie()
        
        circulo.calcularCircunferencia()
        
        if circulo.superficie%2 != 0 and circulo.circunferencia <= 15:
            print circulo
            
    except Exception as ex:
        print ex
        
    
    
main()
