#Título de práctica: CalcMat


#Autor: Esteban Olivero Cubides
#<eoliveroc@academia.usbbog.edu.co>

class Matriz:
    def __init__(self, elementos):
        if len(elementos) != 2 or any(len(fila) != 2 for fila in elementos):
            raise ValueError("La matriz debe ser de tamaño 2x2.")
        self.valores = elementos

    def __add__(self, otra):
        resultado = [
            [self.valores[i][j] + otra.valores[i][j] for j in range(2)]
            for i in range(2)
        ]
        return Matriz(resultado)

    def __sub__(self, otra):
        resultado = [
            [self.valores[i][j] - otra.valores[i][j] for j in range(2)]
            for i in range(2)
        ]
        return Matriz(resultado)

    def __mul__(self, otra):
        resultado = [
            [
                self.valores[i][0] * otra.valores[0][j] + self.valores[i][1] * otra.valores[1][j]
                for j in range(2)
            ]
            for i in range(2)
        ]
        return Matriz(resultado)

    def mostrar(self):
        print(f"|{self.valores[0][0]}  {self.valores[0][1]}|")
        print(f"|{self.valores[1][0]}  {self.valores[1][1]}|")


def ingresar_matriz(num):
    print(f"> Matriz {num}:")
    elementos = []
    for i in range(2):
        fila = []
        for j in range(2):
            valor = int(input(f"> Matriz {num}: elemento {i},{j}\n< "))
            fila.append(valor)
        elementos.append(fila)
    return Matriz(elementos)


def main():
    matriz1 = ingresar_matriz(1)
    matriz2 = ingresar_matriz(2)

    print("> Matriz 1:")
    matriz1.mostrar()
    print("> Matriz 2:")
    matriz2.mostrar()

    print("> Escriba 1 para suma, \n>         2 para resta, \n>         3 para multiplicación")
    opcion = int(input("< "))

    if opcion == 1:
        resultado = matriz1 + matriz2
        print("> La suma de las dos matrices es:")
    elif opcion == 2:
        resultado = matriz1 - matriz2
        print("> La resta de las dos matrices es:")
    elif opcion == 3:
        resultado = matriz1 * matriz2
        print("> La multiplicación de las dos matrices es:")
    else:
        print("Opción no válida.")
        return

    resultado.mostrar()


if __name__ == "__main__":
    main()
