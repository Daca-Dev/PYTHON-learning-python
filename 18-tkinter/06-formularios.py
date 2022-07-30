from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter | David Casas")

# Texto de encabezado
encabezado = Label(ventana, text="Formularios con Tkinter - David Casas")
encabezado.config(
    bg="black",
    fg="white",
    font=('Open Sans', 18),
    pady=10,
    padx=10
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

# label para el campo NOMBRE
label = Label(ventana, text='Nombre')
label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

# campo de texto
campo_texto = Entry(ventana)
campo_texto.config(
    justify=CENTER
)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)

# label para el campo APELLIDO
label = Label(ventana, text='Apellido')
label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

# campo de texto
campo_texto = Entry(ventana)
campo_texto.config(
    justify=RIGHT,
    state="disabled"
)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# label para el campo Descripción (cText area)
label = Label(ventana, text='Descripción')
label.grid(row=3, column=0, padx=5, pady=5, sticky=N)

campo_grande = Text(ventana)
campo_grande.config(
    height=5,
    width=30,
    font=('Arial', 12),
    padx=15,
    pady=15
)
campo_grande.grid(row=3, column=1, padx=5, pady=5)

# botones
Label(ventana).grid(row=4,column=1)

boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)

ventana.mainloop()