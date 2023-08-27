def obtener_nombre_mes(numero_mes):
    meses = (
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    )

    if 1 <= numero_mes <= 12:
        return meses[numero_mes - 1]
    else:
        return "Mes inválido"

# Le pedimos al usuario que ingrese un número para mandar el mes
numero_mes = int(input("Ingresa el número de mes: "))

nombre_mes = obtener_nombre_mes(numero_mes)
print("El mes es según el número ingresado:", nombre_mes)