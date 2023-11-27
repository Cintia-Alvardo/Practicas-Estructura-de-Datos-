import re

pattern = re.compile(r'^\d{5}')

text = "12345 San miguel, San Miguel"
resultado = pattern.match(text)

if resultado:
    print(f"Concidencia encontrada: {resultado.group()}")
else:
    print("No hay concidencia")
