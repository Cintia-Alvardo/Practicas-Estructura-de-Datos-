class NoEsListaError(Exception):
   def init(self, mensaje):
       self.mensaje = mensaje
       super().init(self.mensaje)

def suma_lista(lista):
   if not (lista, list):
       raise NoEsListaError("La entrada no es una lista")
   elif not lista:
       return 0
   else:
       return lista[0] + suma_lista(lista[1:])

mi_lista = [40, 7, 29, 13, 19]
try:
   resultado = suma_lista(mi_lista)
   print(f"La suma de los numeros de la lista es: {resultado}")
except NoEsListaError as e:
 print(e)

