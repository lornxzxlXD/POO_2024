#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

inicio = int(input("Por favor, ingrese el primer número: "))
fin = int(input("Por favor, ingrese el segundo número: "))

# Verificar que el primer número sea menor que el segundo número
if inicio < fin:
    # Mostrar todos los números entre el primer y el segundo número
    print(f"Los números entre {inicio} y {fin} son:")
    for num in range(inicio + 1, fin):
        print(num, end=" ")
    print()  # Agregar una nueva línea al final
elif inicio > fin:
    # Mostrar todos los números entre el segundo y el primer número
    print(f"Los números entre {fin} y {inicio} son:")
    for num in range(fin + 1, inicio):
        print(num, end=" ")
    print()  # Agregar una nueva línea al final
else:
    print("Los números son iguales, no hay números entre ellos.")
    
