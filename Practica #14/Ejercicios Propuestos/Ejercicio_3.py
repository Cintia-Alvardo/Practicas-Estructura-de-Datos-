import re

def palabras_minusculas(texto):
    pattern = r'\b[a-z]+\b'

    palabras_encontradas = re.findall(pattern, texto)

    return palabras_encontradas

texto = "Este ES un EJEMPLO de TEXTO con PALABRAS en minúsculas y Mayúsculas."
palabras_en_minusc = palabras_minusculas(texto)

print("Palabras encontradas en minúsculas:")
print(palabras_en_minusc)
