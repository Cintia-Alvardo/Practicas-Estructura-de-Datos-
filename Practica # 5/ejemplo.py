# 1. Crear una función 
# Palabra reservada def segido del nombre de la función


import re


def miFunción():
    print("Este es un mensaje")

miFunción()

# 2. Funciones con parametros 
def miFunción2(nombre, apellido):
    print(f"Hola{nombre}{apellido}!!")
    miFunción2('Cintia','Alvarado')

# 3. Retormnar valores a traves de la función
def sumar (a,b):
    return a + b

resultado = sumar(4,6)
print(f"El resultado es {resultado}")
print(f"El resultado es {sumar(4,6)}")

# 4. Parametros (parametros por nombre y por posición)
def areaTriangulo(base, altura):
    return(base * altura)/ 2


alturaTriangulo = 20
baseTriangulo = 20

# Por posición 
print(areaTriangulo(alturaTriangulo, baseTriangulo))

#Por nombre
print(
    areaTriangulo(
        altura= alturaTriangulo,
        base = baseTriangulo
    )
)

# 5. Valores por defecto
def multiplicar(a,b = 1):
    return a * b

print(f"La multiplicación es: {multiplicar(2,5)}")
print(f"La multiplicación es: {multiplicar(2)}")


# 6. Argumentos indeterminados por posición

def multipllicarMuchos (a, *numeros):
    for num in numeros:
        a *= num
    return a

print(multipllicarMuchos(2))
print(multipllicarMuchos(2,5))
print(multipllicarMuchos(2,3,4))

# 7. Otra forma de argumentos indeterminados por nombre
def mostrarInformación(**Persona):
    información = Persona.items()
    for clave , valor in información:
        print(f"{clave}: {valor}")

mostrarInformación(
    Nombre = 'Cintia Lissbeth',
    Apellido = 'Alvarado Robles'
)

# 8. Retorno de multiples valores 
def datos():
    nombre = "Cintia"
    apellido = "Alvarado"
    return nombre , apellido , 19 , "Femenino"

misDatos = datos()
print(misDatos[0])