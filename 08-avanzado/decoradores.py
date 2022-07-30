# generar un decorador

def decorador(func):
    """ Es una función decorador """
    def envoltura():
        print('Esta linea de codigo se agrego con ayuda del decorador')
        func()
        
    return envoltura

def saludo():
    print('Hola!')
    
@decorador
def saludo_1():
    print('Hola!')

if __name__ == '__main__':
    saludo()
    
    saludo = decorador(saludo)
    saludo()
    
    saludo_1()