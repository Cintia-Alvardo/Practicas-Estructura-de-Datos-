class Biblioteca:
    def __init__(self, lista_libros):
        self.libros = lista_libros

    def mostrarLibros(self):
        for libro in self.libros:
            print(f"- {libro}")


    def PrestarLibros(self,libro):
        if libro in self.libros:
           print(f"se presto el libro {libro}")
           self.libros.remove(libro)

        else:
          print("No se encontro el libro: {libro}")

    def agregarLibros(self, libro):
        if libro not in self.libros:
         print(f"Se ha añadido el libro: {libro}")
         self.libros.append(libro)

        else:
         print("El libro ya existe")

lista_libros = ["Aprender Python", "Aprender Java", "Aprender JavasScript"]

biblioteca = Biblioteca(lista_libros)

while True:
    print(".:: MENU  ::.")
    print("1) Mostrar Libros")
    print("2) Prestar Libros")
    print("3) Agregar Libros")
    print("4) Salir")
    opcion = int(input("Que accion desea realizar: "))

    if opcion == 1:
        print(".:: Lista de libros ....")
        biblioteca.mostrarLibros()
    elif opcion == 2:
        libro_prestar = input("Digite el nombre del libro: ")
        biblioteca.PrestarLibros(libro_prestar)
    elif opcion == 3:
        libro_agregar = input("Digite el nombre del libro: ")
        biblioteca.agregarLibros(libro_agregar)
    elif opcion == 4:
        break


