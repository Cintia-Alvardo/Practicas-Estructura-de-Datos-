from collections import deque

class Banco:
   def __init__(self):
       self.cola_clientes = deque()

   def llega_cliente(self, cliente):
       self.cola_clientes.append(cliente)
       print(f"\nEl cliente {cliente} ha llegado y está en la cola.")

   def atender_cliente(self):
       if self.cola_clientes:
           cliente = self.cola_clientes.popleft()
           print(f"\nEl cliente {cliente} ha sido atendido y ha salido de la cola.")
       else:
           print("No hay clientes en la cola.")

banco = Banco()
banco.llega_cliente("Ezequiel Ramos")
banco.llega_cliente("Rafael Flores")
banco.llega_cliente("Sandi Orellana")
banco.llega_cliente("Zulma Paz")
banco.atender_cliente()
