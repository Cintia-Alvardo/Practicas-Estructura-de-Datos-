try:
    with open("nombres.txt", "w") as archivo:
        while True:
            nombre = input("Ingresa un nombre (o 'salir' para terminar): ")
            if nombre.lower() == "salir":
                break
            archivo.write(nombre + "\n")
    print("Nombres escritos en 'nombres.txt'.")
except Exception as e:
    print(f"Error: {str(e)}")
