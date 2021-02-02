# arreglo = [2, 3, 4, 56, 1]
# string = "Hola sebitas"

# for elemento in arreglo:
#     print(elemento)

# for char in string:
#     print(char)


# def saludar(nombre, nombre2):
#     print("Hola " + nombre, nombre2)


# saludar("Sebastian", "Paolo")

class Sandwich:
    def __init__(self):
        ingredientes = input("Que ingredientes desea?")
        self.ingredientes = ingredientes.split(" ")

    ingredientes = []

    def calcularPrecio(self):
        return 50 + 10 * len(self.ingredientes)


sandwichPaolo = Sandwich()
sandwichPaolo.calcularPrecio()
