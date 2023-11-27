import  re
pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

text = "Contacta conmigo en correo@example.com o en otro.correo@dominio.com"
resultado = pattern.finditer(text)

print("Direcciones de correo electronico encontradas: ")
for match in resultado:
    print(match.group())