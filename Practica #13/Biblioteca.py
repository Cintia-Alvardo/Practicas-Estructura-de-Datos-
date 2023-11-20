class Biblioteca:
   def __init__(self):
       self.pila_libros = []

   def prestar_libro(self, libro):
       self.pila_libros.append(libro)
       print(f"\nEl libro {libro} se a prestado.")

   def devolver_libro(self, libro):
       if libro in self.pila_libros:
           self.pila_libros.remove(libro)
           print(f"\nEl libro {libro} se a devuelto.")
       else:
           print(f"\nEl libro {libro} no está en la pila.")

   def mostrar_libros(self):
       print("Los libros en la pila son:")
       for libro in self.pila_libros:
           print(libro)

biblioteca = Biblioteca()
biblioteca.prestar_libro("Cien años de soledad")
biblioteca.prestar_libro("Don Quijote de la Mancha")
biblioteca.mostrar_libros()
biblioteca.devolver_libro("Cien años de soledad")
biblioteca.mostrar_libros()