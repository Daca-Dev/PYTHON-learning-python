"""
Las exepciones son piezas de código que nos permiten manejar errores
que sabemos se pueden generar en un código, por ejemplo una conexión
a una base de datos

o la busqueda de un valor que no existe y previamente podemos saber
si no existe

se hace por medio de las palabras clave try - except
"""

# forma básica
try:
    10/0
except Exception as e:
    print("Ocurrió un error", e)
    
print("continuamos")

# Manejo de distintos errores
resultado = None
a = "10"
b = 0

try:
    resultado = a / b
except ZeroDivisionError as e:
    print("Ocurrió un error con ZeroDivisionError", e)  
    print(type(e))  
except TypeError as e:
    print("Ocurrió un error con TypeError", e)  
    print(type(e)) 
except Exception as e:
    print("Ocurrió un error con exception", e)  
    print(type(e)) 
    
print("resultado: ", resultado)    
print("continuamos...")    

# manejo de errores con else y finish
resultado = None
try:
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    resultado = a / b
except ZeroDivisionError as e:
    print("Ocurrió un error con ZeroDivisionError", e)  
    print(type(e))  
except TypeError as e:
    print("Ocurrió un error con TypeError", e)  
    print(type(e)) 
#except ValueError as e:
#    print("Ocurrió un error con ValueError", e)  
#    print(type(e))    
except Exception as e:
    print("Ocurrió un error con exception", e)  
    print(type(e)) 
else:
    print("No hubo ninguna excepción")
finally:
    print("Fin del manejo de excepciones")    
    
print("resultado: ", resultado)    
print("continuamos...")    