 #Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado
# 


# Solicitar dos números al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Realizar las operaciones básicas
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Verificar si el segundo número es diferente de cero para evitar la división por cero
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir por cero"

# Mostrar los resultados por pantalla
print(f"Suma: {numero1} + {numero2} = {suma}")
print(f"Resta: {numero1} - {numero2} = {resta}")
print(f"Multiplicación: {numero1} * {numero2} = {multiplicacion}")
print(f"División: {numero1} / {numero2} = {division}")
