import os 
from time import sleep
import Generador_Contraseña as mc

contraseña = mc.generar_contraseña(8)
print(contraseña)