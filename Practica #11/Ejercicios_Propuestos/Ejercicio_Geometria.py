import os 
from time import sleep
import Modulo_Geometria as mc

def menu():
    os.system("cls")
    print("\t.:: MENU ::.")
    print("[1] Círculo")
    print("[2] Rectangulo")
    print("[3] Triangulo")
 
while True :
    menu()
    opcion = input("Digite la opcion a realizar: ")
        
    if opcion == "1":
        radio = int(input("Digite el radio del círculo: "))
            
        print(f"El area del círculo es: {mc.area_circulo(radio)}cm")
        print(f"El perimetro del círculo es: {mc.perimetro_circulo(radio)}cm")
        sleep(3)
            
    elif opcion == "2":
        alto = int(input("Digite el alto del rectangulo: "))
        ancho = int(input("Digite el ancho del rectangulo: "))
            
        print(f"El area del rectangulo es: {mc.area_rectangulo(alto, ancho)}cm")
        print(f"El perimetro del rectangulo es: {mc.perimetro_rectangulo(alto, ancho)}cm")
        sleep(3)
    elif opcion =="3":
        base = int(input("Digite la base del triangulo: "))
        altura = int(input("Digite la altura del triangulo: "))
            
        print(f"El area del triangulo es: {mc.area_triagulo(base, altura)}cm")
        print(f"El perimetro del triangulo es: {mc.perimetro_triangulo(base, altura)}cm")
        sleep(3)
        
    else: 
        print("Saliendo del programa.................")
        sleep(3)
            
            
            
        
