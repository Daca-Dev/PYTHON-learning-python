"""
HERENCIA
Es un concepto de POO que consiste en 'heredar' los atributos y metodos a una clase padre
"""

class Persona:
    # constructor: en python el constructor esta oculto y este es llamado por el metodo __init__
    def __init__(self, name='Juan', lastname='Perez', age=28, *args, **Kargs): # self: referencia al objetivo mismo
        # Atributos de instancia
        self.nombre = name
        self.apellido = lastname
        self.edad = age
        self.args = args
        self.kargs = Kargs

    def mostrarDetalle(self, pre='Hola'):
        print(f'{pre}, {self.nombre} {self.apellido}, y tengo {self.edad} años')

class Empleado(Persona):
    
    def __init__(self, name, lastname, age, puesto, *args, **Kargs):
        super().__init__(name=name, lastname=lastname, age=age, *args, **Kargs)
        self.puesto = puesto

    # sobreescribimos el metodo
    def mostrarDetalle(self, pre='Hola'):
        print(pre, self.puesto)
        return super().mostrarDetalle(pre=pre)

if __name__ == '__main__':
    empleado = Empleado('David', 'Casas', 25,'Desarrollador Backend')

    empleado.mostrarDetalle()