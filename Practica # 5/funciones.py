# Función para ingresar n datos a una lista
def ingresar_datos():
    n = int(input("Ingrese la cantidad de datos: "))
    datos = []
    for i in range(n):
        valor = float(input(f"Ingrese el dato {i + 1}: "))
        datos.append(valor)
    return datos

# Función para ordenar una lista de menor a mayor utilizando el algoritmo de burbuja
def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Función para calcular la sumatoria de los datos de una lista
def calcular_sumatoria(lista):
    suma = 0
    for dato in lista:
        suma += dato
    return suma

# Función para calcular la media de los datos
def calcular_media(lista):
    suma = calcular_sumatoria(lista)
    n = len(lista)
    media = suma / n
    return media

# Función para calcular la mediana de los datos
def calcular_mediana(lista):
    ordenar_lista(lista)
    n = len(lista)
    if n % 2 == 0:
        medio1 = lista[n // 2 - 1]
        medio2 = lista[n // 2]
        mediana = (medio1 + medio2) / 2
    else:
        mediana = lista[n // 2]
    return mediana

# Función para calcular la moda de los datos
def calcular_moda(lista):
    frecuencias = {}
    for dato in lista:
        if dato in frecuencias:
            frecuencias[dato] += 1
        else:
            frecuencias[dato] = 1

    moda = None
    max_frecuencia = 0
    for dato, frecuencia in frecuencias.items():
        if frecuencia > max_frecuencia:
            moda = dato
            max_frecuencia = frecuencia

    return moda

# Función para calcular la desviación típica o estándar para datos sin agrupar
def calcular_desviacion_estandar(lista):
    media = calcular_media(lista)
    n = len(lista)
    suma_diferencias_cuadradas = 0

    for dato in lista:
        diferencia = dato - media
        suma_diferencias_cuadradas += diferencia ** 2

    desviacion_estandar = (suma_diferencias_cuadradas / n) ** 0.5
    return desviacion_estandar


funciones = ingresar_datos()
print("--------------------------------------------------")
print("Datos ingresados:\n", funciones)
print("--------------------------------------------------")
print("Lista de menor a mayor:\n", funciones)
print("--------------------------------------------------")
print("Sumatoria de datos:\n", calcular_sumatoria(funciones))
print("--------------------------------------------------")
print("Madia de los datos:\n", calcular_media(funciones))
print("--------------------------------------------------")
print("Mediana de los datos:\n", calcular_mediana(funciones))
print("--------------------------------------------------")
print("Calcular la moda:\n", calcular_moda(funciones))
print("--------------------------------------------------")
print("Calcular la desviación típica o estándar para datos sin agrupar:\n", calcular_desviacion_estandar(funciones))
