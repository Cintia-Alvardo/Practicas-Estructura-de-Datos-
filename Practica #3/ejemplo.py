#almacena los numeros

lista = []

def menu():
    print("A)Agregar un numero a la lista")
    print("B) Agregar un numero a la lista segun la posicion")
    print("C) Ver longitud de la lista")
    print("D)Eliminar el último número")
    print("E)Eliminar un numero")
    print("F)Contar repeticiones de un numero")
    print("G)Salir.")

#ejecuta una opcion del menu
def seleccionarOpcion(opcion):
    print("\n")
    opcion = opcion.upper()

    if opcion == "A":
        numero = int(input("\nIngresa un numero "))
        lista.append(numero)


    elif opcion == "B":
        numero = int(input("Ingresar un numero "))
        lista.append(numero)
    
    elif opcion =="C":
        print("Longitud de la lista es de {0}". format(len(lista)))

    elif opcion == "D":
        numero = lista.pop()
        print("Se borro el numero {0}".format(numero))

    elif opcion == "E":
        print("De la lista que numero desea borrar", lista)
        numero = int(input("Ingrese el numero al borrar: "))
        lista.remove(numero)

    elif opcion =="F":
        print("En la lista{0} se repite {1}".format(numero, lista))

    elif opcion =="G":
        print("Gracias por usar nuestro programa")

    else:
        print("Esta opcion no es valida!!!")

while True:
    menu()
    opcion = input("Ingresa una opcion A-G: ")
    seleccionarOpcion(opcion)
    
    print("Lista de datos", lista)

    if opcion.upper() == "G":
        break
           
