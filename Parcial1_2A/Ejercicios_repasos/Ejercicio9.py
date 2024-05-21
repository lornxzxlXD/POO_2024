#Hacer un programa que solicite 
#numeros indefinidamente hasta que se introduzca el 111 y salir del programa
def solicitar_numeros():
    while True:
        numero = int(input("Introduce un número (o 111 para salir): "))
        if numero == 111:
            print("Saliendo del programa...")
            break

# Llamar a la función para solicitar números
solicitar_numeros()