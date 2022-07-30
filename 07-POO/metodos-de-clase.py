"""
METODOS ESTATICOS -> no recibe información de la clase, no tiene relación con la clase

METODOS DE CLASE -> 

"""


class MiClase:
    
    varibales_clase = 'Valor variable de clase'

    def __init__(self):
        self.variable_instancia = 'variable de instancia'
        
    # los metodos estaticos no reciben el parametro self y
    # no acceden a las variables de instancia
    @staticmethod
    def metodo_estatico():
        print('Hola desde el metodo estatico')
        
    @classmethod
    def metodo_clase(cls):
        print(cls.varibales_clase)
    
if __name__ == "__main__":
    
    MiClase.metodo_estatico()
    
    MiClase.metodo_clase()
    
    clase = MiClase()
    MiClase.variable_al_vuelo = 'Variable al vuelo'
    print(clase.variable_al_vuelo)