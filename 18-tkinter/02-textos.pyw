"""
El objeto Label es el que nos permite crear textos dentro de nuestra ventana

Dispone de muchos aprametros el objeto

configure:
    - fg: font color
    - bg: backgrpund color
    - padx: padding en x
    - pady: padding en y
    - font: tipo de fuente
    -cursor: el tipo de cursor que se pondra cunado pasas por encima del elemento
"""

from tkinter import *


ventana = Tk()
ventana.geometry("750x470")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(fg="white", bg="black", padx=20, pady=30, font=('Consolas', 30))
texto.pack() # metodo para cargarlo dentro de la ventana

texto = Label(ventana, text='David Alberto Casas Amézquita')
texto.pack(anchor=E)

ventana.mainloop()