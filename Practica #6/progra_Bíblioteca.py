class Biblioteca:
    def __init__(self, _libros):
        self.libros = _libros

    #mostrar libros
    def mostrarLibros(self):
        for libro in self.libros:
            print(libro)

    def prestarLibros(self, nombreLibro):
        #Verificar si el libro existe
        if nombreLibro in self.libros:
            print("Se presto el libro ", nombreLibro)
            self.libros.remove(nombreLibro)
        else:  
            print("El libro no existe")

    def agregarLibro(self, nombreLibro):
            #Verifica que no exista
            if nombreLibro not in self.libros:
               print("Se añadio el libro ", nombreLibro)
               self.libros.append(nombreLibro)
            else:
                print("El libro ya existe")

libros = ["Clean Code", "Java", "Analisis"]

Biblioteca = Biblioteca(libros) 

while True:
    print("1- Agreagar un libro") 
    print("2- Prestar libro") 
    print("3- Mostrar Libros") 
    print("4- Salir") 

    opción = int(input("Ingresa una opción (1-4): "))

    if opción ==1:
        libro = input("\nIngresa el nombre de el Libro: ")
        Biblioteca.agregarLibro(libro)
    elif opción ==2:
        libro = input("\nIngresa el nombre de el Libro: ")
        Biblioteca.prestarLibros(libro)
    elif opción ==3:
        print("\nMis libros son")
        Biblioteca.mostrarLibros()
    elif opción ==4:
                    break