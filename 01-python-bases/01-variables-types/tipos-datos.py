"""
Existen varios tipos de datos primitivos (built-in) dentro
de Python, estos son:

- numericos compuestos por los tipos
    - integer
    - complex number
    - float
- boolean
- diccionarios
- set
- sequence type
    - string
    - list
    - tuple
"""

# numericos
entero = 1
flotante = 1.0
complejo = 1 + 1j

print(type(entero))
print(type(flotante))
print(type(complejo))

# sequence type
cadena_caracter = "hola mundo"
lista = [1, 2, True, "hola"]
tupla = (1, 2, True, "hola")

print(type(cadena_caracter))
print(type(lista))
print(type(tupla))

# bolean
booleano = True # False
print(type(booleano))

# diccionarios
diccionario = {
    'name': 'David',
    'apellido': 'Casas'
}
print(type(diccionario))