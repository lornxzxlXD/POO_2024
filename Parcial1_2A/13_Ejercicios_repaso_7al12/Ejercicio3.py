# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas

lista = []

if not lista:
    print("La lista está vacía. Por favor, añada palabras o frases.")

    while True:
        entrada = input("Ingrese una palabra o frase (o 'salir' para terminar): ")
        if entrada.lower() == 'salir':
            break
        lista.append(entrada)

print("\nContenido de la lista en mayúsculas:")
for elemento in lista:
    print(elemento.upper())

