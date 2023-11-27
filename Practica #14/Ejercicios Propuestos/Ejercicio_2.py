import re

def contiene_fecha_valida(cadena):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'

    coincidencia = re.search(pattern, cadena)

    return coincidencia is not None

text = "Hoy es 26/11/2023 y mañana será 27/11/2023."
if contiene_fecha_valida(text):
    print("Se encontró al menos una fecha válida.")
else:
    print("No se encontraron fechas válidas.")
