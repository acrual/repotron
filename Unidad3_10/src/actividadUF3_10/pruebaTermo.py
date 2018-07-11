'''
Created on 23 ene. 2017

@author: profesoresi
'''
import Termo as t

def main():
    try:
        termo = t.Termo(7)
        
        for i in range(1,4):
            termo.beber()
    
        termo.rellenar(3)
        print termo
        
        termo.rellenar(7)
        
    except Exception as ex:
        print ex  
        
main()  