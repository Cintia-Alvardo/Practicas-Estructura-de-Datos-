class Perro:
    def Sonido(self):
        print("Guuuuuuuuuuu !!!!!")
    pass

class Gato:
    def Sonido(self):
        print("Miauuuuuuuuuuu !!!!")
    pass

class Vaca:
    def Sonido(self):
        print("Muuuuuuuuuuuuuuu !!!!")
    pass

perro = Perro()
gato = Gato()
vaca = Vaca()

animales =[perro, gato, vaca, gato, perro, vaca]

for animal in animales:
    animal.Sonido()