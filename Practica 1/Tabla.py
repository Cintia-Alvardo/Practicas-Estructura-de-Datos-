#Ejercicio de practica 1
numero = float(input("Ingrese un número: "))
contador = 1

while contador <= 10:
    producto = numero * contador
    print ("{0} x {1} = {2}".format (numero,contador,producto))
    contador = contador + 1

#Ejercio de practica 2
numero = float (input("Ingresa un numero: "))
minimo = float (input("Desde donde desea mostrar: "))
maximo = float (input("Hasta donde desea mostrar: "))

for contador in range (minimo,maximo + 1):
    producto = numero * contador
    print ("{0} x {1} = {2}".format (numero,contador,producto))
   
