import tkinter as tk
from tkinter import messagebox

def saludo():
    messagebox.showinfo("Pepito","Hola Mundo")

def saludo_2(nombre):
    messagebox.showinfo("Pepito",f"Hola {nombre}")


ventana = tk.Tk()
ventana.title("Hola Mundo!")
ventana.geometry("400x300")


etiqueta = tk.Label(ventana, text="Título de la ventana", bg="#ff0000", fg="white")
#etiqueta.pack(fill=tk.X, expand=True)
etiqueta.pack()

#boton = tk.Button(ventana, text="Presiona aquí", command=saludo)
boton = tk.Button(ventana, text="Presiona aquí", command=lambda: saludo_2("Juanito"))
boton.pack()

img = tk.PhotoImage(file="black-hole.png")
label_img = tk.Label(ventana, image=img)
label_img.pack()


ventana.mainloop()