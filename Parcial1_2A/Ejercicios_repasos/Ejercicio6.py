#Mostrar todas las tablas del 1 al 10. 
#Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
def mostrar_tablas():
    for i in range(1, 11):
        print(f"Tabla del {i}")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print("")  # Línea en blanco para separar las tablas

# Llamada a la función para mostrar las tablas
mostrar_tablas()