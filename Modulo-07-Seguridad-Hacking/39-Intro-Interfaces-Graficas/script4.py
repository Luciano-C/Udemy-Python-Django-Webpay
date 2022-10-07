import tkinter as tk
from tkinter import messagebox, ttk


ventana = tk.Tk()
ventana.title("Hola Mundo!")
ventana.geometry("400x300")

boton_1 = tk.Button(ventana, text="Botón 1", width=10, height=5)
boton_2 = tk.Button(ventana, text="Botón 2", width=10, height=5)
boton_3 = tk.Button(ventana, text="Botón 3", width=10, height=5)

img = tk.PhotoImage(file="black-hole.png")
label_img = tk.Label(ventana, image=img)

boton_1.grid(row=0, column=0)
boton_2.grid(row=0, column=1)
boton_3.grid(row=0, column=2)
label_img.grid(row=0, column=4)

ventana.mainloop()