#Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?

def calcular_porcentaje(numero, porcentaje):
    resultado = (porcentaje / 100) * numero
    return resultado

try:
    numero = float(input("Introduce el número: "))
    porcentaje = float(input("Introduce el porcentaje (%): "))

    resultado = calcular_porcentaje(numero, porcentaje)
    print(f"{porcentaje}% de {numero} es {resultado}")

except ValueError:
    print("Por favor, introduce números válidos.")