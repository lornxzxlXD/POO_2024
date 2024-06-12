# Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

mi_lista = [1, 2, 3]
mi_cadena = "Hola, mundo"
mi_entero = 42
mi_logico = True

def imprimir_mensaje(variable):
    if isinstance(variable, list):
        print("Esta variable es una lista.")
    elif isinstance(variable, str):
        print("Esta variable es una cadena.")
    elif isinstance(variable, int):
        print("Esta variable es un entero.")
    elif isinstance(variable, bool):
        print("Esta variable es un valor lógico.")
    else:
        print("Tipo de dato desconocido.")

imprimir_mensaje(mi_lista)
imprimir_mensaje(mi_cadena)
imprimir_mensaje(mi_entero)
imprimir_mensaje(mi_logico)
