"""
HERENCIA MULTIPLE

La herencia multiple nos permite crear una uneva clase a partir de dos o mas clases
esto permite encapsular de manera mas eficiente nuestros objetos y aplicar la filosofia de

Don't repeat yourself

MRO - Method Resolution Order
* Metodo que nos permite conocer la jerarquia de clases en un objeto que tiene herencia
* el orden define el orden en que se buscaran métodos y atributos.

"""

class FiguraGeometrica:
    
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto
        
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho
        
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, ancho):
        self.__ancho = ancho
        
class Color:
    
    def __init__(self, color):
        self.__color = color
        
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color
        
#! Clase con herencia multiple
# El orden en que se aplica la herencia afecta el resultado
class Cuadrado(FiguraGeometrica, Color):
    
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        
    def area(self):
        return self.alto ** self.ancho
    

if __name__ == "__main__":
    
    cuadrado = Cuadrado(2, 'azul')
    
    print('ancho: ', cuadrado.ancho)
    print('alto: ', cuadrado.alto)
    print('color: ', cuadrado.color)
    
    print('area: ', cuadrado.area())
    
    print(Cuadrado.mro())