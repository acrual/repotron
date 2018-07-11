# -*- coding: utf-8 -*-
'''
Created on 16 ene. 2017

@author: profesoresi
'''
import actividadUF3_9.Punto as ap

def main():
    try:
        p0 = ap.Punto()
        print p0.x , ',' ,p0.y
        p1 = ap.Punto(1, 5)
        print p1.x , ',' ,p1.y
        ''' p2 = ap.Punto('a', 4)
        print p2.x , ',' ,p2.y '''
        
        p2 = ap.Punto(3, 4)
        print p2.x , ',' ,p2.y
        
        pr = p2.restar(p1)
        print pr
        print pr.x , ',' , pr.y
        print p2.distancia(p1)
        
        pr2 = p1 - p2
        ps = p1 + p2
        print ps
        print pr2
        
    except TypeError as ex:
        print ex
    
main()  
    