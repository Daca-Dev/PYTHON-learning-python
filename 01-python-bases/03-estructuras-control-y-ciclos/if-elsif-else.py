"""
esta estructura nos permite tomar desiciones basado en los 
resultados booleanos obtenidos ciertos operandos.
"""

# variables
a = True
b = False

# Estructura if
if a == b:
    print('Sentencia verdadera')
elif a <= b:
    print('Segunda sentencia Verdadera')
else:
    print("No se cumplio ninguna sentencia")

# if terniario
c = "condicion verdadera" if a != b else "Condicion falsa"
print(c)