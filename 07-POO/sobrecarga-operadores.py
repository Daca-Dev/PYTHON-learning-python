"""
SOBRECARGA DE OPERADORES

significa que un mismo operador puede comportarse de diferentes formas
un ejemplo de esto es el operador suma, el cual se comporta distinto en función de los
operandos

"""

class Persona:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __add__(self, other):
        return self.nombre + ' ' + other.nombre
    

objeto1 = Persona('David')
objeto2 = Persona('Casas')

# objeto1.__add__(objeto2)
print(objeto1 + objeto2)
