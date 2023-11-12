def suma_lista(lista):
    
    if not lista:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])


mi_lista = [40, 7, 29, 13, 19]
resultado = suma_lista(mi_lista)
print(f"La suma de los números de la lista {mi_lista} es: {resultado}")
