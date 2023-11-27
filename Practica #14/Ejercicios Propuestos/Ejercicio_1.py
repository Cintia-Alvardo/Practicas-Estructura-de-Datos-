import re

def es_codigo_empleado_valido(codigo):
    pattern = r'^EMP\d{3}$'

    coincidencia = re.match(pattern, codigo)

    return coincidencia is not None and coincidencia.group() == codigo

text = "EMP297"
if es_codigo_empleado_valido(text):
    print("El código de empleado es válido.")
else:
    print("El código de empleado no es válido.")