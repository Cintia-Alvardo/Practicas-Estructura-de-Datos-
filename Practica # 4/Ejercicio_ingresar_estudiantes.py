
cantidad = int(input("Cuantos estudiantes desea ingresar: "))


resultados = {}

for i in range(0 , cantidad):
    print("---------Ingresando datos del estudiante----------")
    nombre = input("Ingrese el nombre del estudiante {0}: ".format(i + 1))
    notas = []

    for j in range (0,3):
        nota = float(input("Ingrese la nota {0}°: ".format(j + 1)))
        notas.append(nota)

    resultados.setdefault(nombre, notas)


for nombre, notas in resultados.items():
    print("-"*60)
    fila = nombre.ljust(10)
    for nota in notas:
        fila += "| "+str(nota).ljust(10)

    fila += "| "+str(round((sum(notas) / len(notas)), 2)).ljust(10)

    print(fila)

    