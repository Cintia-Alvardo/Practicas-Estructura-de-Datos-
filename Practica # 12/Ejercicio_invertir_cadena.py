class CadenaVacia(Exception):
    def _init_(self):
        super()._init_("La cadena está vacía")

def invertir_cadena(cadena):
    if len(cadena) <= 1:
        return cadena
    else:
        return cadena[-1] + invertir_cadena(cadena[1:-1]) + cadena[0]

try:
    cadena_original = "Cintia Alvarado"
    if len(cadena_original) == 0:
        raise CadenaVacia()
    cadena_invertida = invertir_cadena(cadena_original)
    print(f"Cadena original: {cadena_original}")
    print(f"Cadena invertida: {cadena_invertida}")
except CadenaVacia as e:
    print(e)
