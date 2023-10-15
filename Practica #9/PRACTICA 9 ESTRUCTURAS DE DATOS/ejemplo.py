
class Persona:
    nombre = ''
    edad = ''
    OrientacionSexual = ''
    linaje = ''

    def __init__(self, nombre, edad, OrientacionSexual, linaje):
        self.nombre = nombre
        self.edad = edad
        self.OrientacionSexual = OrientacionSexual
        self.linaje = linaje


    def saltar(self):
        print("la persona esta saltando")

persona = Persona("Ariel", "20", "Hetero", "Familia Real")

persona.saltar()

