class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    nombre = ""
    edad = 0
    genero = ""

    def saludar(self):
        print("Hola, mi nombre es", self.nombre)


class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, curso):
        Persona.__init__(self, nombre, edad, genero)
        self.curso = curso

    curso = ""


class Profesor(Persona):
    def __init__(self, nombre, edad, genero, materia):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.materia = materia

    materia = ""


class Administrativo(Persona):
    def __init__(self, nombre, edad, genero, salario, antiguedad):
        Persona.__init__(self, nombre, edad, genero)
        self.antiguedad = antiguedad
        self.salario = salario

    antiguedad = 0
    salario = 0
