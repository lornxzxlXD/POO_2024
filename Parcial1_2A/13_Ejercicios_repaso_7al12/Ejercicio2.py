# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for

lista = []

valor = 1  
while len(lista) < 120:
    lista.append(valor)
    valor += 1  

print("Lista con valores añadidos:")
for numero in lista:
    print(numero)