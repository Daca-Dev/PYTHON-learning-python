"""

"""


class Producto:

    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f'Id: {self._id_producto}, nombre: {self._nombre}, precio: {self._precio}'


class Orden:

    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregarProducto(self, producto):
        self._productos.append(producto)

    def totalOrden(self):
        total = 0
        for item in self._productos:
            total += item.precio
            
        return total
    
    def __str__(self):
        productos_str = ''
        for item in self._productos:
            productos_str += item.__str__() + '\n'
            
        return f'Orden:\n{productos_str}'


if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    producto2 = Producto('Pantalon', 150.00)
    
    print(producto1)
    print(producto2, '\n')
    
    lista_productos = [producto1, producto2 ]
    orden = Orden(lista_productos)
    
    print(orden)
