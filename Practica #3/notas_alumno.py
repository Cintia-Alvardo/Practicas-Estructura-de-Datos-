# Inicializar una lista vacía para almacenar las notas
notas = []

# Leer las 5 notas del usuario y asegurarse de que estén dentro del rango válido
print("\n----------- Capturación de las 5 notas -----------")
for i in range(5):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i+1}: "))
            if 0 <= nota <= 10:
                break
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Ingrese un valor numérico válido.")
    notas.append(nota)
print("----------- Fin de la capturación de las 5 notas -----------\n")

# Mostrar todas las notas
print("\n----------- Las 5 notas capturadas -----------")
for i, nota in enumerate(notas, start=1):
    print(f"Nota {i}: {nota}")
print("----------- Fin de las 5 notas capturadas -----------\n")

# Encontrar la nota más alta
nota_maxima = max(notas)
# Calcular la nota media
nota_media = sum(notas) / len(notas)
# Encontrarla nota más baja
nota_minima = min(notas)
print("\n----------- La nota alta, media y baja son: -----------")
print(f"Nota más alta: {nota_maxima}")
print(f"\nNota media: {nota_media:.2f}")
print(f"\nNota más baja: {nota_minima}")
print("----------- Fin de impresion de notas -----------\n")