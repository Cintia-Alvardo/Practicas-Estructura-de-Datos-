
productos = {
    "Arroz": 2.0,
    "Frijol": 3.0,
    "Azucar": 5.0,
    "Cereal": 10.0,
    "Aceite": 4.0,
    "Leche": 20.0,
    "Café": 15.0,
    "Avena": 1.0,
    "Cremora": 8.0,

}

nombre_producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad: "))


if nombre_producto in productos:
    precio_unitario = productos[nombre_producto]
    total_pagar = precio_unitario * cantidad
    print(f"El total a pagar por {cantidad} {nombre_producto} es: ${total_pagar}")
else:
    print("El producto no se encuentra disponible en el inventario.")


