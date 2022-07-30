from tkinter import *

ventana = Tk()
ventana.title = "David Casas"
ventana.geometry("700x700")


marco_padre = Frame(ventana, width=250, height=250) # unidades en pixeles
marco_padre.config(
    bg="blue",
    relief="solid"
)
marco_padre.pack(side=TOP, fill=X, expand=YES, anchor=N)

# MArcos normales
marco = Frame(marco_padre, width=250, height=250) # unidades en pixeles
marco.config(
    bg="red",
    relief="solid"
)
marco.pack(side=LEFT, anchor=SW)

marco = Frame(marco_padre, width=250, height=250) # unidades en pixeles
marco.config(
    bg="green",
    relief="solid"
)
marco.pack(side=RIGHT, anchor=SE)

marco_padre = Frame(ventana, width=250, height=250) # unidades en pixeles
marco_padre.config(
    bg="yellow",
    relief="solid"
)
marco_padre.pack(side=TOP, fill=X, expand=YES, anchor=S)
marco_padre.pack_propagate(False)

texto = Label(marco_padre, text="Hola Mundo desde Tkinter()")
texto.config(
    bg="yellow",
    font=('Arial', 20),
    bd=3,
    relief=SOLID
)
texto.pack(anchor=CENTER, fill="both", expand=YES)

ventana.mainloop()