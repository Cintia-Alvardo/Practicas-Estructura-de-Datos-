class Perro:
    def sonido(self):
        print("Guauuuuuuuu!!!")

class Gato:
    def sonido(self):
        print("Miauuuuuuuu!!!")

class Vaca:
    def sonido(self):
        print("Muuuuuuuuu!!!")

misPersonajes = []

for i in range(0,10):
    if i%2==0:
        misPersonajes.append(Perro())
    elif (i + 1)%3==0:
        misPersonajes.append(Gato())
    else:
        misPersonajes.append(Vaca())

for animal in misPersonajes:
    animal.sonido()

