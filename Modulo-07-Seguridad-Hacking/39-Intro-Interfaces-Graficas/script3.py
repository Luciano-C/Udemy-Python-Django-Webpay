import tkinter as tk
from tkinter import messagebox, ttk


ventana = tk.Tk()
ventana.title("Hola Mundo!")
ventana.geometry("400x300")

frame = ttk.LabelFrame(ventana, text="Título del frame", width=385, height=200, borderwidth=5, relief="raised")
frame.grid(row=1, column=0)

etiqueta = tk.Label(frame, text="Título", font=("Arial", 12, "bold"))
etiqueta.grid(row=3, column=0)

img = tk.PhotoImage(file="black-hole.png")
label_img = tk.Label(ventana, image=img)
label_img.grid(row=5, column=2)

ventana.mainloop()