#Título de práctica: GUIHello
#Autor: Esteban Olivero Cubides
#<eoliveroc@academia.usbbog.edu.co>

import tkinter as tk
from tkinter import messagebox

class AplicacionSaludo:
    def __init__(self, master):
        self.master = master
        master.title("tk")
        
        # Etiqueta
        self.label = tk.Label(master, text="Como te llamas?")
        self.label.grid(row=0, column=0, padx=5, pady=10)
        
        # Campo de entrada
        self.entrada = tk.Entry(master)
        self.entrada.grid(row=0, column=1, padx=5)
        
        # Botón de saludo
        self.boton_saludo = tk.Button(master, text="Saludo", command=self.saludar)
        self.boton_saludo.grid(row=1, column=0, pady=10)
        
        # Botón de salir
        self.boton_salir = tk.Button(master, text="Salir", command=master.quit)
        self.boton_salir.grid(row=1, column=1)

    def saludar(self):
        nombre = self.entrada.get()
        mensaje = f"Hola {nombre}!"
        messagebox.showinfo("...", mensaje)

# Crear ventana raíz e iniciar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionSaludo(root)
    root.mainloop()
