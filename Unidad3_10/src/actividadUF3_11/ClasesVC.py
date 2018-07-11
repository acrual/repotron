# -*- coding: utf-8 -*-
'''
Created on 23 de ene. de 2017

@author: maria
'''

class ObjVC(object):
    '''
    Constructor
    '''
    def __init__(self, titulo, precioAlquiler, alquilado=False):
        if isinstance(precioAlquiler, (int, long, float)):
            if isinstance(alquilado, bool):
                self.titulo=titulo
                self.precioAlquiler=precioAlquiler
                self.alquilado=alquilado
            else:
                raise TypeError("El valor del atributo alquilado debe ser booleano")
        else:
            raise TypeError("El precio de alquiler debe ser un valor numérico")
                
    '''
    metodo alquilar:
     Que modifique el atributo correspondiente cada vez que se realice un alquiler del objeto. 
     No se podrán alquilar objetos que ya están alquilados. 
     Devuelve 1 si se ha podido realizar la operación y 0 en caso contrario
    '''
    def alquilar(self):
        res = 1
        if self.alquilado:
            res = 0
        else:
            self.alquilado=True
        
        return res
    
    '''
    metodo devolver:
     Que modifique el atributo correspondiente cada vez que se produzca la devolución de un objeto. 
     No se podrán devolver objetos que no se hayan alquilado. 
     Devuelve 1 si se ha podido realizar la operación y 0 en caso contrario.

    '''    
    def devolver(self):
        res = 1
        if self.alquilado:
            self.alquilado=False
        else:
            res=0
        
        return res
            
    def __str__(self):
        return 'Título: ' + self.titulo + '\n precio de alquiler: ' + str(self.precioAlquiler) + '€\n alquilado: ' + str(self.alquilado) + '\n' 
        
class Pelicula(ObjVC):
    
    '''
    Constructor
    '''
    def __init__(self, titulo, precioAlquiler, genero, anio, director, alquilado=False):
        '''
        el anio debe ser entero positivo y tener 4 digitos
        '''
        if isinstance(anio, (int, long)):
            if anio > 1895:
                ObjVC.__init__(self, titulo, precioAlquiler, alquilado)
                self.genero=genero
                self.anio=anio
                self.director=director
            else:
                raise AssertionError("El año debe ser posterior a 1895")
        else:
            raise TypeError("El año debe ser un valor entero positivo")
        
        
    def __str__(self):
        txt = 'Película: \n' + ObjVC.__str__(self) + ' Género: ' + self.genero + '\n año: ' + str(self.anio) + '\n director: ' + self.director
        return txt
    
       
class Videojuego(ObjVC):
    '''
    Constructor
    '''
    def __init__(self, titulo, precioAlquiler, codPegi, plataforma, alquilado=False):
        '''
        el codigo pegi debe tener como mucho 2 caracteres (AP, 7, 12, 16, 18)
        '''
        if self.es_codPegi(codPegi):
            ObjVC.__init__(self, titulo, precioAlquiler, alquilado)
            self.codPegi=codPegi
            self.plataforma=plataforma
        else:
            raise TypeError("El codigo pegi no es válido")
            
    
    def es_codPegi(self, valor):
        ''' Indica si el codigo pegi es valido. '''
        codigos=['AP', '3', '7', '12', '16', '18']
        return (codigos.count(valor) > 0)   
    
    def __str__(self):
        txt = 'Videojuego: \n' + ObjVC.__str__(self) + ' Cod Pegi: ' + str(self.codPegi) + '\n plataforma: ' + self.plataforma
        return txt
    
def main():
    try: 
        print '--Creamos una película--'
        peli = Pelicula('El Señor de los Anillos: El Retorno del Rey', 4, 'Aventuras', 2003, 'Peter Jackson')
        print peli
        
        print ''
        
        for i in range(1,3):
            if peli.alquilar() == 1:
                print 'Se ha alquilado la película: ' + peli.titulo
            else:
                print 'No se ha podido alquilar la película: ' + peli.titulo
        
        print ''
        
        print '--Creamos un videojuego--'
        vj = Videojuego('Call Of Duty: Black Ops III', 5, '18', 'PS4', True)
        print vj
        
        print ''
        
        for i in range(1,3):
            if vj.devolver() == 1:
                print 'Se ha devuelto el videojuego: ' + vj.titulo
            else:
                print 'No se ha podido devolver el videojuego: ' + vj.titulo
                
    except Exception as ex:
        print ex
    
main()