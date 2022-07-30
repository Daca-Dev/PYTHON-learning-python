from tkinter import *
from PIL import Image, ImageTk


ventana = Tk()
ventana.geometry("700x500")

Label(ventana, text="Hola, soy David").pack(anchor=W)

imagen = Image.open('./10-tkinter/images/halo.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack(anchor=E)

ventana.mainloop()