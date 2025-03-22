#Título de práctica: Tienda1


#Autor: Esteban Olivero Cubides
#<eoliveroc@academia.usbbog.edu.co>




class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"|{self.nombre.ljust(10)}|{str(self.cantidad).ljust(12)} unidades|{str(self.precio).ljust(8)} pesos|"

def obtener_producto(numero):
    nombre = input(f"Producto {numero}, ¿cuál es el nombre?\n> ")
    precio = int(input(f"¿Cuál es el precio de '{nombre}'?\n> "))
    cantidad = int(input(f"¿Qué cantidad hay de '{nombre}'?\n> "))
    return Producto(nombre, precio, cantidad)

def main():
    productos = [obtener_producto(i + 1) for i in range(3)]
    
    print("\nResumen:")
    print("|Producto  |Cantidad     |Precio     |")
    print("-" * 36)
    for producto in productos:
        print(producto)
