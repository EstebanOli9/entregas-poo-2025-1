from datetime import datetime


"""
Práctica de clase: Tienda1

Este programa maneja el inventario de una tienda.

Heyder Ivan Ramos Rodriguez
<hiramosr@academia.usbbog.edu.co
 heydercolegious@gmail.com>
2025-04-26
"""


class Visualizador:
    """Agregamos la clase visualizador"""
    def resumen(self):
        datos = self.mostrar_datos()
        print(
            f"{datos[0]:<8} {datos[1]:<12} {datos[2]:<8}"
            f"{datos[3]:<20} {datos[4]:<20}"
            )


class Mascotas(Visualizador):
    def __init__(self, nombre, edad, raza):
        super().__init__()
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().isoformat()

    def mostrar_datos(self):
        return [self.especie, self.nombre, str(self.edad) + " años",
                self.raza, self.fecha_ingreso]


class Perro(Mascotas):
    """Clases que heredan de Mascotas"""
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)
        self.especie = "Perro"


class Gato(Mascotas):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, raza)
        self.especie = "Gato"


mascotas = []  # Lista que almacena las mascotas ingresadas

numero_mascotas = int(input("> ¿Cuantas mascotas va a ingresar? \n"))

for i in range(1, numero_mascotas + 1):
    print(f"> Mascota {i}, que clase es? (P)erro o (G)ato")
    tipo = input("< ").strip().lower()  # Toma de igual manera
    # mayusculas y minusculas

    while tipo not in ("p", "g", "perro", "gato"):
        # Si no es ninguno no validara
        print("> Opción invalida. ¿Perro o Gato?")
        tipo = input("< ").strip().lower()

    if tipo in ("p", "perro"):
        clase = "Perro"
    else:
        clase = "Gato"

    print(f"> ¿Cual es el nombre del {clase}?")
    nombre = input("< ").strip()

    print(f"> ¿Que edad tiene {nombre}?")
    edad = int(input("< ").strip())

    print(f"> ¿Que raza es {nombre}?")
    raza = input("< ").strip()

    if clase == "Perro":
        mascota = Perro(nombre, edad, raza)
    else:
        mascota = Gato(nombre, edad, raza)

    mascotas.append(mascota)

for mascota in mascotas:
    mascota.resumen()
