from Funciones import *
from ConexionCineBD import *

# Crear instancia de la clase para manejar la base de datos
db_manager = DatabaseManager(host='localhost', user='root', password='', db_name='cinebd.db')

# Menú principal
while True:
    opcion = mostrar_menu()
    
    if opcion == 1:
        cliente_id = int(input("Ingrese su ID de cliente: "))
        funcion_id = int(input("Ingrese el ID de la función: "))
        comprar_boletos(db_manager, cliente_id, funcion_id)
        
    elif opcion == 2:
        mostrar_cartelera(db_manager)
        
    elif opcion == 3:
        cliente_id = int(input("Ingrese su ID de cliente: "))
        compras_dulceria(db_manager, cliente_id)
        
    elif opcion == 4:
        nombre = input("Ingrese el nombre del cliente: ")
        apellidos = input("Ingrese los apellidos del cliente: ")
        edad = int(input("Ingrese la edad del cliente: "))
        registrar_cliente(db_manager, nombre, apellidos, edad)
        
    elif opcion == 5:
        print("Saliendo del sistema. ¡Hasta luego!")
        db_manager.cerrar_conexion()
        break
        
    else:
        print("Opción no válida, intente nuevamente.")
