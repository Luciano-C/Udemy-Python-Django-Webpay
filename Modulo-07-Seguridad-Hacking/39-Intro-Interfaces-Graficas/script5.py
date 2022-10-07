import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import scrolledtext


ventana = tk.Tk()
ventana.title("Hola Mundo!")

etiqueta = tk.Label(ventana, text="Listado de items", font=("Arial", 12, "bold"))
etiqueta.grid(row=0, column=0)

tabla = ttk.Treeview(ventana, columns=("Nombre", "E-mail", "Teléfono"))
tabla.grid(row=3, column=0, sticky="nse")

scroll = ttk.Scrollbar(ventana, orient="vertical", command=tabla.yview)
scroll.grid(row=5, column=4, sticky="nse")

tabla.configure(yscrollcommand=scroll.set)

tabla.heading("#0", text="ID")
tabla.heading("#1", text="Nombre")
tabla.heading("#2", text="E-mail")
tabla.heading("#3", text="Teléfono")

for i in range(100):
    tabla.insert("", 0, text=f"{i}", values=("Cesar Cancino", "yo@cesarcancino.com", "1234566"))

ventana.mainloop()