"""
Título de práctica: Mascotas2

Autor: Esteban Olivero Cubides
<eoliveroc@academia.usbbog.edu.co>
Fecha: 2025-04-28
"""

from datetime import datetime

# Nueva clase Visualizador
class Visualizador:
    def resumen(self):
        clase = "Perro" if isinstance(self, Perro) else "Gato"
        return f"| {clase:<5} | {self.nombre:<8} | {self.edad:<4} años | {self.raza:<12} | {self.fecha_ingreso} |"

# Modificamos la herencia
class Mascota(Visualizador):
    def _init_(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().isoformat()

class Perro(Mascota, Visualizador):
    def _init_(self, nombre, edad, raza):
        super()._init_(nombre, edad, raza)

class Gato(Mascota, Visualizador):
    def _init_(self, nombre, edad, raza):
        super()._init_(nombre, edad, raza)

def registrar_mascota():
    mascotas = []
    num_mascotas = int(input("¿Cuántas mascotas va a ingresar?\n> "))
    
    for i in range(1, num_mascotas + 1):
        tipo = input(f"Mascota {i}, ¿qué clase es (P)erro o (G)ato?\n> ").strip().lower()
        
        while tipo not in ['perro', 'gato', 'p', 'g']:
            print("Opción no válida, intente de nuevo.")
            tipo = input(f"Mascota {i}, ¿qué clase es (P)erro o (G)ato?\n> ").strip().lower()
        
        clase = "Perro" if tipo in ["perro", "p"] else "Gato"
        nombre = input(f"¿Cuál es el nombre del {clase}?\n> ").strip()
        edad = input(f"¿Qué edad tiene '{nombre}'?\n> ").strip()
        raza = input(f"¿De qué raza es '{nombre}'?\n> ").strip()
        
        mascota = Perro(nombre, edad, raza) if tipo in ["perro", "p"] else Gato(nombre, edad, raza)
        mascotas.append(mascota)
        print()
    
    print("Resumen:")
    print("| Clase | Nombre   | Edad  | Raza         | Fecha de ingreso          |")
    print("|-------|---------|-------|-------------|----------------------------|")
    for mascota in mascotas:
        print(mascota.resumen())  # Aquí usamos el método resumen de Visualizador

# Ejecutar la función de registro
registrar_mascota()
