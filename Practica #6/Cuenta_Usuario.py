class CuentaGmail:
    def __init__(self, nombre, apellido, usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.correo = f"{usuario}@gmail.com"
        self.contrasena = None

    def establecer_contrasena(self, contrasena):
        if len(contrasena) >= 8:
            self.contrasena = contrasena
            print("Contraseña establecida con éxito.")
        else:
            print("La contraseña debe tener al menos 8 caracteres.")

    def mostrar_informacion(self):
        print("Información de la cuenta:")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Usuario: {self.usuario}")
        print(f"Correo electrónico: {self.correo}")


nuevo_usuario = CuentaGmail("Cintia", "Alvarado", "cintiaalvarado")


nuevo_usuario.establecer_contrasena("miContrasenaSegura")


nuevo_usuario.mostrar_informacion()

