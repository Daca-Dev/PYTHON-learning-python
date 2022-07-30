"""
Tkinter es un modulo para crear interfaces graficas de usuario
"""

from tkinter import *
import os


class Programa:

    def __init__(self):
        self.title = "Master en Python"
        self.icon_path = './images/d.ico'
        self.icon_path_alt = './10-tkinter/images/d.ico'
        self.size = "770x450"
        self.resiable = False
        self.ventana = Tk()

    def cargar(self):
        """ muestra la ventana de la aplicación principal """

        ruta_icono = os.path.abspath(self.icon_path)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_path_alt)

        self.ventana.iconbitmap(ruta_icono)

        # titulo de la self.ventana
        self.ventana.title(self.title)

        # cambiar tamaño
        self.ventana.geometry(self.size)

        # bloquear el tamaño de la self.ventana
        # (eje x, eje y) True: permite cambiar tamaño
        self.ventana.resizable(self.resiable, self.resiable)

    def addTexto(self, text):
        texto = Label(self.ventana, text=text)
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la self.ventana hasta que se cierre
        self.ventana.mainloop()


if __name__ == '__main__':

    programa = Programa()
    programa.cargar()
    programa.addTexto('Hola desde mi metodo')
    programa.addTexto('Varias líneas')
    programa.addTexto('desde el metodo de la clase')
    programa.addTexto('Programa')
    programa.mostrar()
