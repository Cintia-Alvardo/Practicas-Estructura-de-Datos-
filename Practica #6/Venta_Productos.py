class Articulo:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def vender(self, cantidad_vendida):
        if cantidad_vendida > self.cantidad:
            print("No hay suficiente unidades disponible.")
        else:
            self.cantidad -= cantidad_vendida
            print(f"Se vendieron {cantidad_vendida} unidades de {self.nombre}.")
            print(f"Unidades restante: {self.cantidad} unidades.")

articulo = Articulo("Zapatos", 40, 22.70)
articulo.vender(15)

articulo = Articulo("Vestido", 12, 18.99)
articulo.vender(5)

articulo = Articulo("Carteras", 7, 12.00)
articulo.vender(3)


