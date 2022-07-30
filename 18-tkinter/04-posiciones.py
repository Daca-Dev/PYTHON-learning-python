
from tkinter import *


ventana = Tk()
# ventana.geometry("750x470")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(fg="white", bg="black", padx=20, pady=30, font=('Consolas', 30))
texto.pack(side=TOP) # metodo para cargarlo dentro de la ventana

texto = Label(ventana, text='David Alberto Casas Amézquita')
texto.config(height=3, bg="yellow", padx=20, pady=30, cursor="spider")
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text='David Alberto Casas Amézquita')
texto.config(height=3,fg="white", bg="blue", padx=20, pady=10)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text='David Alberto Casas Amézquita')
texto.config(height=3, bg="red", padx=20, pady=10)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text='David Alberto Casas Amézquita')
texto.config(height=3, bg="green", padx=20, pady=10)
texto.pack(side=RIGHT, fill=X)

ventana.mainloop()