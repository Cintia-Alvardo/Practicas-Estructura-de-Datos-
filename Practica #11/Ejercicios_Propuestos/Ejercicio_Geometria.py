import os 
from time import sleep
import Modulo_Geometria as mc

def menu():
    os.system("cls")
    print("\t.:: MENU ::.")
    print("[1] Area de Círculo")
    print("[2] Area de Rectangulo")
    print("[3] Area de Trinulo")
 
while True :
    menu()
    opcion = input("Digite la opcion a realizar: ")
        
    if opcion == "1":
        radio = int(input("Digite el radio del círculo: "))
            
        print(f"El area del círculo es: {mc.area_circulo(radio)}cm")
        sleep(3)
            
    elif opcion == "2":
        alto = int(input("Digite el alto del rectangulo: "))
        ancho = int(input("Digite el ancho del rectangulo: "))
            
        print(f"El area del rectangulo es: {mc.area_rectangulo(alto, ancho)}cm")
        sleep(3)
    elif opcion =="3":
        base = int(input("Digite la base del triangulo: "))
        altura = int(input("Digite la altura del triangulo: "))
            
        print(f"El area del triangulo es: {mc.area_triagulo(base, altura)}cm")
        sleep(3)
        
    else: 
        print("Saliendo del programa.................")
        sleep(3)
            
        