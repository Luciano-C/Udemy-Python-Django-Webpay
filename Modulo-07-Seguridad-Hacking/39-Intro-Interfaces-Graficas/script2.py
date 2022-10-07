import tkinter as tk
from tkinter import messagebox

def procesar():
    texto = campo.get()
    etiqueta2["text"] = texto

ventana = tk.Tk()
ventana.title("Hola Mundo!")
ventana.geometry("400x300")

etiqueta = tk.Label(ventana, text="Ingresa tu nombre")
etiqueta.pack()

etiqueta2 = tk.Label(ventana, text="")

campo = tk.Entry(ventana)
campo.pack()

boton = tk.Button(ventana, text="Enviar", command=procesar)
boton.pack()

etiqueta2.pack()

ventana.mainloop()