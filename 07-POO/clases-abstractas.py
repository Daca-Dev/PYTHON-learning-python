"""
CLASES ABSTRACTAS

algunas clases que heredan de su padre, van a sobreescribir un metodo, y muchas veces definir este metodo
en la clase padre, no es necesario, pero si podemos definir que las clases que hereden de las clases hijas
tengan que definirlo

* las clases abstractas no se puede instanciar, solo se usan para crear una clase hija
* si una clase tiene un metodo abstracto, ya la hace una clase abstracta

"""

# ABC = Abstract Base Clase
from ABC import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self.__validar_valor(ancho):
            self.__ancho = ancho
        else:
            self.__ancho = 0
            print(f'Valor de ancho erroneo: {ancho}')
            
        if self.__validar_valor(alto):
            self.__alto = alto
        else:
            self.__alto = 0
            print(f'Valor de alto erroneo: {alto}')
    
    #! Metodo abstracto!!
    @abstractmethod
    def calcular_area(self):
        pass