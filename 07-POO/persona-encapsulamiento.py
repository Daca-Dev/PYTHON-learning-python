""" 
ENCAPSULAMIENTO -> el encapsulamiento lo que busca es que no se acceda directamente a los atributos de una clase 

1. defina el atributo con guion bajo (se peude seguri accediendo, pero si tiene _ significa que es privado)
2. colocar doble guion bajo permite colocar privado o un atributo, aunque no muetsra error el programa, 
    se evidencia que no ejecuta el codigo 

? para accerder a los atributos se usan getters y setters

! si una variable no se quiere modificar simplemente no definimos el atributo de Setter

* Los destructores nos permiten eliminar instaciónde un objeto y liberar memoria

"""

# Clase Persona
class Persona:
    # constructor: en python el constructor esta oculto y este es llamado por el metodo __init__
    def __init__(self, name='Juan', lastname='Perez', age=28, *args, **Kargs): # self: referencia al objetivo mismo
        # Atributos de instancia
        self.__nombre = name
        self.__apellido = lastname
        self.edad = age
        self.args = args
        self.kargs = Kargs
    
    # ! Getter
    @property
    def nombre(self):
        print('llamando metodo Get Nombre')
        return self.__nombre

    # ! Setter
    @nombre.setter
    def nombre(self, nombre):
        print('llamando metodo Set Nombre')
        self.__nombre = nombre

    def mostrarDetalle(self, pre='Hola'):
        print(f'{pre}, {self.__nombre} {self.__apellido}, y tengo {self.edad} años')

    def __del__(self):
        print('eliminando objeto: ', self.__nombre, self.__apellido)


if __name__ == "__main__":
    # INSTANCIA del objeto Persona (dirección de memoria)
    persona1 = Persona()
    persona1.__nombre = 'Hernesto'

    print("Creación".center(30, '-'))
    print(persona1.mostrarDetalle())

    print('A traves del getter: ', persona1.nombre)

    persona1.nombre = 'David'

    print(persona1.mostrarDetalle())

    # Destructores
    print("Eliminación".center(30, '-'))
    del persona1
