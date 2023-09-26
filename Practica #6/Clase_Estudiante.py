class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def actualizar_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def actualizar_carnet(self, nuevo_carnet):
        self.carnet = nuevo_carnet

    def actualizar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

estudiante = Estudiante("Cintia", "Alvarado", "U20231421", "Ingeniería Industrial")
estudiante.actualizar_nombre("Cintia Alvarado")
print("Nombre Actual: " + estudiante.nombre)   
estudiante.actualizar_nombre("Lissbeth Robles")
print("Nombre Actualizado:  " + estudiante.nombre)  
estudiante.actualizar_carnet("U20231421")
print("Cambio de Carnet:  " + estudiante.carnet) 
estudiante.actualizar_carrera("Tecnico en desarrollo de software")
print("Cambio de Carrera: " + estudiante.carrera)  