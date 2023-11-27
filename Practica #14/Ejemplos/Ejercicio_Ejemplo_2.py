import re
pattern = re.compile(r'\bpython\w*', re.IGNORECASE)

text = 'Python3 es un lenguaje de programación poderoso.'
resultado = pattern.search(text)

if resultado:
    print(f"Concidencia encontrada en cualquier lugar: {resultado.group()}")
else:
    print("No hay concidencias encontradas")
    
    