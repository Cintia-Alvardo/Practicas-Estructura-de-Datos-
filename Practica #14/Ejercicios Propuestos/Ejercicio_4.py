import re

def encontrar_ocurrencias(texto, palabra_a_buscar):

    pattern = re.compile(r'\b' + re.escape(palabra_a_buscar) + r'\b', re.IGNORECASE)

    coincidencias = pattern.finditer(texto)

    ubicaciones = [coincidencia.span() for coincidencia in coincidencias]

    return ubicaciones

texto_palabra = "Este es un ejemplo de texto. Ejemplo de prueba en este ejemplo."
palabra_a_buscar = "ejemplo"

ocurrencias = encontrar_ocurrencias(texto_palabra, palabra_a_buscar)

print(f"Ubicaciones de la palabra '{palabra_a_buscar}':")
for inicio, fin in ocurrencias:
    print(f"Inicio: {inicio}, Fin: {fin}")
