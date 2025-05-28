"""
Esteban Olivero Cubides
eoliveroc@academia.usbbog.edu.co
"""


from datetime import datetime

class InfoAnimal:
    """Clase base para visualizar información"""
    def mostrar_resumen(self):
        datos = self.obtener_datos()
        print(f"{datos[0]:<10} {datos[1]:<15} {datos[2]:<10} {datos[3]:<18} {datos[4]:<25}")

class Animal(InfoAnimal):
    def __init__(self, nombre, edad, raza):
        super().__init__()
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def obtener_datos(self):
        return [self.tipo, self.nombre, f"{self.edad} años", self.raza, self.fecha_registro]

class Canino(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)
        self.tipo = "Perro"

class Felino(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)
        self.tipo = "Gato"

# Lista para almacenar objetos animales
registro_animales = []

cantidad = int(input("¿Cuántos animales desea registrar?\n> "))

for n in range(cantidad):
    print(f"\nRegistro {n + 1}")
    categoria = input("¿Es un (P)erro o un (G)ato?\n> ").lower().strip()

    while categoria not in ["p", "g", "perro", "gato"]:
        print("Entrada no válida. Intente con 'Perro' o 'Gato'.")
        categoria = input("> ").lower().strip()

    nombre = input("Nombre del animal:\n> ").strip()
    edad = int(input(f"Edad en años de {nombre}:\n> ").strip())
    raza = input(f"Raza de {nombre}:\n> ").strip()

    if categoria.startswith("p"):
        animal = Canino(nombre, edad, raza)
    else:
        animal = Felino(nombre, edad, raza)

    registro_animales.append(animal)

print("\n--- Resumen de animales registrados ---\n")
for a in registro_animales:
    a.mostrar_resumen()
