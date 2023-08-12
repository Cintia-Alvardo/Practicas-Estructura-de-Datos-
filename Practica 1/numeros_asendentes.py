numeros = []

for i in range (0,5):
    numero = int(input("Ingresa un numero: "))
    numeros.append(numero)

for i in range (0, len(numeros)):
   for j in range (0,len(numeros)-1):
       if numeros [j] > numeros [j+1]:
           aux = numeros[j]
           numeros[j] = numeros[j+1]
           numeros[j+1] = aux
           
print (numeros)




