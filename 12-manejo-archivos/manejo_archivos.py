"""

r: lectura
w: escritura (sobrescribe)
a: escritura (append)

t: tipo texto
b: binario
+: agregar datos 

ejemplo de uso:
r+    w+    wb

! en python el simbolo \ tiene un significado
! por lo que en windows se usa \\ para representar \
! y colocar correctamente el path de una ruta

* el try - except es por buenas practicas

"""

try:
    archivo = open(file=r'./prueba.txt', mode='wt', encoding='utf-8')
    archivo.write("Agregamos información al archivo\n")
    archivo.write("Agregamos información al archivo\n")
    archivo.write("Agregamos información al archivo\n")
    archivo.write("Agregamos información al archivo\n")
    archivo.write("y adios!")
except Exception as e:
    print(e)
finally:
    archivo.close()


try:    
    archivo = open(r"./prueba.txt", "r", encoding='utf-8')
    # print(archivo.read())
    
    # guardado archivo
    archivo_2 = open(r"./copia.txt", 'a', encoding='utf-8')
    archivo_2.write(archivo.read())
    archivo_2.close()
    
    # imprimirmos las filas del archivo
    print(archivo.read(5)) # indicamos el numero de caracteres que queremos leer
    print(archivo.read(8)) # indicamos el numero de caracteres que queremos leer
    print(archivo.readline()) # lee una linea
    print(archivo.readlines()) # devuelve una lista con las lineas del archivo
    
    for linea in archivo:
        print(linea)
    
except Exception as e:
    print(e)
finally:
    archivo.close()