try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo 'archivo_inexistente.txt' no se encuentra.")
except Exception as e:
    print(f"Se produjo un error: {str(e)}")