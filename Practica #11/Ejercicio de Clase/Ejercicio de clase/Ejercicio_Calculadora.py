import os 
from time import sleep
import Modulo_Calculadora as mc

def menu():
    os.system("cls")
    print("\t.:: MENU ::.")
    print("[1] Suma")
    print("[2] Resta")
    print("[3] Multiplicacion")
    print("[4] Division")
    
while True :
    menu()
    opcion = input("Digite la opcion a realizar: ")
        
    if opcion == "1":
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
            
        print(f"El resultado de la suma es: {mc.suma(num1, num2)}")
        sleep(3)
            
    elif opcion == "2":
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
            
        print(f"El resultado de la resta es: {mc.resta(num1, num2)}")
        sleep(3)
    elif opcion =="3":
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
            
        print(f"El resultado de la multiplicacion es: {mc.multiplicacion(num1, num2)}")
        sleep(3)
    elif opcion =="4":
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
    
        print(f"El resultado de la division es: {mc.division(num1, num2)}")
        sleep(3)
        
    else: 
        print("Saliendo del programa.................")
        sleep(3)
            
        