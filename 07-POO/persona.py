""" 
    La palabra reservada SELF hace referencia a la posición de memoria en que se almacena la instancia
    del objeto creado, es decir que las instancias de un objeto apuntan a una posición de memoria

    * metodos dunder (double underline, por ejemplo __init__)
    * UML: permite realizar diagramas de la forma en que se relacionan los elementos de una clase
    * podemos agregar nuevos atributos a una instacia de un objeto, pero estos no se comparten con los demas objetos

    ! el nombre de la varible self no es mandatoria, puedes usar el nombre que quieras como THIS,
    ! pero la documentación recomienda SELF

    ? *args -> pasa argumentos adicionales como lista
    ? **kargs -> pasa argumentos adicionales como diccionario

    primero se pasan las tuplas y despues los diccionarios

"""

# Clase Persona
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

# INSTANCIA del objeto Persona (dirección de memoria)
persona1 = Persona()
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('David', 'Casas', 25)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)

# MODIFICAR VALORES de un objeto
persona1.nombre = 'Camilo'
persona1.apellido = 'Perencejo'
persona1.edad = 21
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

# USO DE METODOS de un objeto
persona1.mostrarDetalle('que mas?')
persona2.mostrarDetalle()
Persona.mostrarDetalle(persona1, 'soy yo otra vez!')


# CREAR NUEVOS ATRIBUTOS en una instancia de un objeto
persona1.telefono = 112233445566
print(persona1.telefono)