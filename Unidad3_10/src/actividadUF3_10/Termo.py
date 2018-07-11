'''
Created on 23 ene. 2017

@author: profesoresi
'''

class Termo(object):
    '''
    Constructor
    '''   
    def __init__(self, cantidad=0):
        if self.es_entero(cantidad):            
            if cantidad > 0 and cantidad <= 10:
                self.cantidad=cantidad
                self.estado='lleno'
            elif cantidad == 0:
                self.cantidad=cantidad
                self.estado='vacio'
            else:
                raise AssertionError("la capacidad debe ser un valor entre 0 y 10 dl")
        else:
            raise TypeError("La cantidad debe ser un valor entero")

    def es_entero(self, valor):
        ''' Indica si un valor es numérico o no. '''
        return isinstance(valor, (int, long))
        
    def beber(self):
        if self.cantidad > 0:
            self.cantidad = self.cantidad - 1
        else:
            raise Exception('¡El termo está vacío!')
    
    def rellenar(self, c):
        if self.cantidad + c <= 10:
            self.cantidad = self.cantidad + c
        else:
            raise Exception('¡Cuidado! ¡Se desbordará!')
          
    def __str__(self):
        return 'La cantidad del termo es ' + str(self.cantidad) + ', está ' + self.estado 