"""
Las variables son espacios de memoria separados para almacenar datos
estos datos tienen por defecto un tipo de dato y un nombre asignado
el cual es suado para acceder a dicha posición de memoria dentro
del programa.

! para saber la posición de memoria usamos la función id a la cual le pasamos una variable
"""
# Declaramos unas variables
x = 10
y = 2
z = x + y

# Imprimimos el estado de la variable
print('variable X:', x)
print('variable Y:', y)
print('variable Z:', z)

# Imprimimos la posición de memoria
print('posición de memoria x: ', id(x))