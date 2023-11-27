from ast import pattern
import re
pattern = re.compile(r'\b\w{2}\b')

text = "Hola, soy un texto co algunas palabras cortas"
resultado = pattern.findall(text)

print("Todas las concidencias encontradas: ")
for palabra in resultado:
    print(palabra)