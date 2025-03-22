#Práctica de clase: Tienda2

#Este programa maneja el inventario de una tienda.

#Esteban Olivero Cubides
#<eoliveroc@academia.usbbog.edu.co>

class Producto:
    """Clase para manejar productos en un inventario"""
    
    def _init_(self, nombre, precio_unitario, cantidad, descripcion, clasificacion):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificacion = clasificacion

def solicitar_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor ingrese un número válido.")

def solicitar_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor ingrese un número válido.")

def mostrar_resumen(productos):
    print("\n> Resumen del Inventario:")
    print("-" * 60)
    print("| Producto    | Cantidad | Precio  | Clasificación  |")
    print("-" * 60)
    for p in productos:
        print(f"| {p.nombre:<11} | {p.cantidad:>4} unidades | {p.precio_unitario:>5,.0f} pesos | {p.clasificacion:<13} |")
    print("-" * 60)

def mostrar_resumen_por_clasificacion(productos):
    resumen = {}
    for p in productos:
        subtotal = p.precio_unitario * p.cantidad
        if p.clasificacion in resumen:
            resumen[p.clasificacion] += subtotal
        else:
            resumen[p.clasificacion] = subtotal
    
    print("\n> Resumen por Clasificación:")
    print("-" * 40)
    for clasificacion, total in resumen.items():
        print(f"| {clasificacion:<15} | Total: {total:,.0f} pesos |")
    print("-" * 40)

def run():
    productos = []
    cantidad_productos = solicitar_int("¿Cuántos productos desea ingresar? ")
    
    for i in range(1, cantidad_productos + 1):
        print(f"\nIngrese los datos del producto {i}:")
        nombre = input("Nombre del producto: ")
        precio_unitario = solicitar_float("Precio unitario: ")
        cantidad = solicitar_int("Cantidad disponible: ")
        descripcion = input("Descripción del producto: ")
        clasificacion = input("Clasificación del producto: ")
        
        producto = Producto(nombre, precio_unitario, cantidad, descripcion, clasificacion)
        productos.append(producto)
    
    mostrar_resumen(productos)
    mostrar_resumen_por_clasificacion(productos)

if "_name_" == "_main_": run()
