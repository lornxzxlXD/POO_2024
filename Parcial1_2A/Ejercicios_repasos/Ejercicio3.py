# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for
#


for numero in range(1, 61):
    # Calcular el cuadrado del número
    cuadrado = numero * numero
    # Mostrar el número y su cuadrado
    print(f"El cuadrado de {numero} es {cuadrado}")



    numero = 1

# Usar un bucle while para iterar desde 1 hasta 60
while numero <= 60:
    cuadrado = numero * numero
    # Mostrar el número y su cuadrado
    print(f"El cuadrado de {numero} es {cuadrado}")
    # Incrementar el contador
    numero += 1