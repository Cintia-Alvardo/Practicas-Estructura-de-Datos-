try:
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo 'archivo.txt' no se encuentra.")
except Exception as e:
    print(f"Se produjo un error: {str(e)}")