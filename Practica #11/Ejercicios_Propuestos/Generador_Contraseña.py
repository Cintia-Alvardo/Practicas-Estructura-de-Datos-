import random

def generar_contraseña(longitud):
  caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  contraseña = ""
  for _ in range(longitud):
    contraseña += caracteres[random.randint(0, len(caracteres) - 1)]
  return contraseña




