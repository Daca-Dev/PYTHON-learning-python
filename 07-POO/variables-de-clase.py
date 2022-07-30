"""
VARIABLES DE CLASE

Las variables de clase, se van a asociar con la clase en si misma y no con los objetos
es decir que es un valor que se van a compartir entre las instancias.

* cualqueri variable que se defina fuera del __init__ es una variable de clase
* variables de clase al vuelo, es decir que se agregan en cualqueri momento

"""

class MiClase:
    
    varibales_clase = 'Valor variable de clase'

    def __init__(self):
        self.variable_instancia = 'variable de instancia'
        
if __name__ == "__main__":
    
    clase = MiClase()
    
    MiClase.variable_al_vuelo = 'Variable al vuelo'
    
    print(clase.variable_al_vuelo)