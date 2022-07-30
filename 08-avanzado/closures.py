# Nested functions

""" 
Nested funtions son funciones que retornan funciones
especificas, es decir que a apartir de unos parámetros
creamos una función cuya referencia será retornada
"""

def main():
    a = 1
    def nested():
        print(a)
        
    nested()
    
if __name__ == '__main__':
    main()
    
    
# Closures
def divide_bty(n):
    """ Return a function that divide x number by n"""
    
    def divide(x):
        assert type(x) == int, "No es un número entero"
        return x / n
    
    return divide

if __name__ == '__main__':
    closure = divide_bty(3)
    print(closure(18))
    closure = divide_bty(5)
    print(closure(100))
    closure = divide_bty(18)
    print(closure(54))