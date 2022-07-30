"""
Las estructuras ciclicas nos permiten ejecutar una o mas veces
ciertos pedazos de códigos.

existen la sentencia 

- while: mientras que
- for: durente

"""

a = True
b = False

contador = 0
print('While comun')
while (a != b):
    contador += 1
    print("dentro del bucle, contador: ", contador)
    if contador == 10:
        a = False


a = True
contador = 0
print("while con break")
while (a != b):
    contador += 1
    print("dentro del bucle, contador: ", contador)
    if contador == 10:
        break

a = True
contador = 0
print("while con continue")
while (a != b):
    contador += 1
    if contador == 10:
        a = False
    if ((contador % 2) != 0):
        print('continue', contador)
        continue
    print("dentro del bucle, contador: ", contador)


lista = [1,2,3,4,5]

for item in lista:
    print(item)

for i in range(10): 
    print(i)