
class Empleado:
    
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    
    def __str__(self):
        return f'Nombre: {self.nombre} y sueldo: $ {str(self.sueldo)}'
        
class Gerente(Empleado):
    
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento
        
    def __str__(self):
        return super().__str__() + f' Departamento: {self.departamento}'


def imprimir_detalles(tipo_padre):
    print(tipo_padre)


if __name__ == '__main__':
    print(__name__)
    empleado = Empleado('David', 2000.00)
    gerente = Gerente('David', 2000.00, 'Martech')
    print(imprimir_detalles(empleado))
    print(imprimir_detalles(gerente))