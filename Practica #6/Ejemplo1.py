#Creando una clase
class personas:
        nombre = ""
        apellido = ""
        genero = ""
        edad = ""
        estado_civil = ""

        def __init__(self, _nombre, _apellido, _genero):
            self.nombre = _nombre
            self.apellido = _apellido
            self.genero = _genero

    #metodo
def hablar(self, mensaje):
        print(mensaje)

    #creando un objeto
    #objeto es una instancia de la clase
    # instanciar es crea un objeto apartir de una clase

persona1 = personas("Cintia", "Alvarado", "Femenino")
persona2 = personas("Lissbeth", "Robles", "Femenino")   

print(f"{persona1.nombre} {persona1.apellido}")
print(f"{persona2.nombre} {persona2.apellido}")