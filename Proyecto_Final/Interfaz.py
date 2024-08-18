import tkinter as tk
from tkinter import messagebox
from Funciones import *
from ConexionCineBD import *
import decimal



class CineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Cine")

        # Variable para verificar si se ha iniciado sesión
        self.logged_in = False

        # Inicia la pantalla de inicio de sesión
        self.inicio_sesion()

    def inicio_sesion(self):
        self.clear_window()
        tk.Label(self.root, text="--- Inicio de Sesión ---", font=("Arial", 55)).pack(pady=50)
        
        tk.Label(self.root, text="Usuario:").pack(pady=50)
        self.usuario_entry = tk.Entry(self.root)
        self.usuario_entry.pack(pady=50)
        
        tk.Label(self.root, text="Contraseña:").pack(pady=50)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=50)
        
        tk.Button(self.root, text="Iniciar Sesión", command=self.validar_sesion).pack(pady=50)

    def validar_sesion(self):
        # Permite el acceso sin validar usuario y contraseña
        self.logged_in = True
        
        # Configura la conexión a la base de datos
        self.db_manager = DatabaseManager(
            host='localhost',
            user='root',
            password='',
            db_name='cinebd.db'
        )
        
        self.total_dulceria = 0.0
        # Crear el menú principal
        self.main_menu()

    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="--- Menú Principal ---", font=("Arial", 50)).pack(pady=50)
        
        tk.Button(self.root, text="Comprar Boletos", command=self.comprar_boletos_menu).pack(pady=50)
        tk.Button(self.root, text="Ver Cartelera", command=self.ver_cartelera).pack(pady=50)
        tk.Button(self.root, text="Comprar en Dulcería", command=self.compras_dulceria).pack(pady=50)
        tk.Button(self.root, text="Registrar Nuevo Cliente", command=self.registrar_cliente_menu).pack(pady=50)
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=50)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def comprar_boletos_menu(self):
        self.clear_window()
        tk.Label(self.root, text="--- Comprar Boletos ---", font=("Arial", 55)).pack(pady=50)

        tk.Label(self.root, text="ID del Cliente:").pack(pady=50)
        self.cliente_id_entry = tk.Entry(self.root)
        self.cliente_id_entry.pack(pady=50)
        
        tk.Label(self.root, text="ID de la Función:").pack(pady=50)
        self.funcion_id_entry = tk.Entry(self.root)
        self.funcion_id_entry.pack(pady=50)

        tk.Button(self.root, text="Confirmar Compra", command=self.comprar_boletos).pack(pady=50)
        tk.Button(self.root, text="Regresar", command=self.main_menu).pack(pady=50)

    def ver_cartelera(self):
        self.clear_window()
        tk.Label(self.root, text="--- Cartelera de Películas ---", font=("Arial", 55)).pack(pady=50)

        peliculas = self.db_manager.seleccionar_datos("SELECT * FROM peliculas")
        for pelicula in peliculas:
            tk.Label(self.root, text=f"ID: {pelicula[0]}, Título: {pelicula[1]}, Duración: {pelicula[2]} min, Género: {pelicula[3]}, Director: {pelicula[4]}, Clasificación: {pelicula[5]}").pack(pady=5)

        tk.Button(self.root, text="Regresar", command=self.main_menu).pack(pady=10)

    def registrar_cliente_menu(self):
        self.clear_window()
        tk.Label(self.root, text="--- Registrar Nuevo Cliente ---", font=("Arial", 55)).pack(pady=10)

        tk.Label(self.root, text="ID (opcional):").pack(pady=10)
        self.id_cliente_entry = tk.Entry(self.root)
        self.id_cliente_entry.pack(pady=10)
        
        tk.Label(self.root, text="Nombre:").pack(pady=10)
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.pack(pady=10)
        
        tk.Label(self.root, text="Apellidos:").pack(pady=10)
        self.apellidos_entry = tk.Entry(self.root)
        self.apellidos_entry.pack(pady=10)
        
        tk.Label(self.root, text="Edad:").pack(pady=10)
        self.edad_entry = tk.Entry(self.root)
        self.edad_entry.pack(pady=10)

        tk.Button(self.root, text="Registrar Cliente", command=self.registrar_cliente).pack(pady=10)
        tk.Button(self.root, text="Regresar", command=self.main_menu).pack(pady=10)

    def registrar_cliente(self):
        id_cliente = self.id_cliente_entry.get()  # Obtiene el ID ingresado por el usuario
        nombre = self.nombre_entry.get()
        apellidos = self.apellidos_entry.get()
        edad = self.edad_entry.get()

        if nombre and apellidos and edad:
            try:
                edad = int(edad)
                if id_cliente:  # Si el usuario ingresa un ID
                    id_cliente = int(id_cliente)
                    self.db_manager.ejecutar_query(
                        "INSERT INTO clientes (id_cliente, nombre, apellidos, edad) VALUES (%s, %s, %s, %s)",
                        (id_cliente, nombre, apellidos, edad)
                    )
                else:  # Si no se ingresa un ID, la base de datos lo genera automáticamente
                    self.db_manager.ejecutar_query(
                        "INSERT INTO clientes (nombre, apellidos, edad) VALUES (%s, %s, %s)",
                        (nombre, apellidos, edad)
                    )
                messagebox.showinfo("Éxito", "Cliente registrado exitosamente.")
                self.main_menu()
            except ValueError:
                messagebox.showerror("Error", "La edad y el ID deben ser números.")
            except mysql.connector.errors.IntegrityError as e:
                messagebox.showerror("Error", f"Error de integridad en la base de datos: {e}")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    def compras_dulceria(self):
        self.clear_window()
        tk.Label(self.root, text="--- Compra en Dulcería ---", font=("Arial", 55)).pack(pady=10)

        try:
            productos = self.db_manager.seleccionar_datos("SELECT * FROM productos")
            
            if productos:
                tk.Label(self.root, text="Selecciona un producto:", font=("Arial", 55)).pack(pady=10)
                
                for producto in productos:
                    nombre_producto, precio_producto = producto[1], producto[2]
                    tk.Button(self.root, text=f"{nombre_producto} - ${precio_producto:.2f}",
                              command=lambda n=nombre_producto, p=precio_producto: self.agregar_a_compra(n, p)).pack(pady=10)
                    
                # Etiqueta para mostrar el total
                self.total_label = tk.Label(self.root, text=f"Total: ${self.total_dulceria:.2f}", font=("Arial", 55))
                self.total_label.pack(pady=50)
                
                tk.Button(self.root, text="Regresar", command=self.main_menu).pack(pady=10)
            else:
                tk.Label(self.root, text="No hay productos disponibles.", font=("Arial", 55)).pack(pady=10)
                tk.Button(self.root, text="Regresar", command=self.main_menu).pack(pady=10)
                
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al cargar productos: {str(e)}")
            tk.Button(self.root, text="Regresar", command=self.main_menu).pack(pady=10)

    def agregar_a_compra(self, nombre, precio):
    # Convierte el precio a float si es Decimal
        if isinstance(precio, decimal.Decimal):
            precio = float(precio)
    
        self.total_dulceria += precio
        self.total_label.config(text=f"Total: ${self.total_dulceria:.2f}")
        messagebox.showinfo("Compra", f"Producto seleccionado: {nombre}\nPrecio: ${precio:.2f}")


    def comprar_boletos(self):
        cliente_id = self.cliente_id_entry.get()
        funcion_id = self.funcion_id_entry.get()

        if cliente_id and funcion_id:
            try:
                cliente_id = int(cliente_id)
                funcion_id = int(funcion_id)
                
                cliente = self.db_manager.seleccionar_datos("SELECT * FROM clientes WHERE id_cliente = %s", (cliente_id,))
                funcion = self.db_manager.seleccionar_datos("SELECT * FROM funciones WHERE id_funcion = %s", (funcion_id,))

                if cliente and funcion:
                    cliente_obj = Cliente(cliente[0][0], cliente[0][1], cliente[0][2], cliente[0][3])  # ID, Nombre, Apellidos, Edad
                    sala_data = self.db_manager.seleccionar_datos("SELECT * FROM salas WHERE id_sala = %s", (funcion[0][2],))
                    pelicula_data = self.db_manager.seleccionar_datos("SELECT * FROM peliculas WHERE id_pelicula = %s", (funcion[0][3],))
                    sala = Sala(sala_data[0][1], sala_data[0][2], sala_data[0][3], sala_data[0][0])
                    pelicula = Pelicula(pelicula_data[0][1], pelicula_data[0][2], pelicula_data[0][3], pelicula_data[0][4], pelicula_data[0][5], pelicula_data[0][0])
                    funcion_obj = Funcion(funcion[0][1], sala, pelicula, funcion[0][0])

                    self.clear_window()
                    tk.Label(self.root, text="--- Selección de Asiento ---", font=("Arial", 55)).pack(pady=50)

                    # Mostrar los asientos disponibles
                    asientos_frame = tk.Frame(self.root)
                    asientos_frame.pack(pady=50)

                    for fila, asientos in funcion_obj.asientos_disponibles.items():
                        fila_label = tk.Label(asientos_frame, text=f"Fila {fila}:")
                        fila_label.pack()
                        for numero, disponible in enumerate(asientos, start=1):
                            text = f"{numero}" if disponible else f"X{numero}"
                            state = tk.NORMAL if disponible else tk.DISABLED
                            button = tk.Button(asientos_frame, text=text, state=state,
                                               command=lambda f=fila, n=numero: self.seleccionar_asiento(f, n, funcion_obj))
                            button.pack(side=tk.LEFT, padx=2)

                    tk.Label(self.root, text="Ingrese la fila (A-G):").pack(pady=50)
                    self.fila_entry = tk.Entry(self.root)
                    self.fila_entry.pack(pady=5)

                    tk.Label(self.root, text="Ingrese el número de asiento (1-10):").pack(pady=50)
                    self.numero_entry = tk.Entry(self.root)
                    self.numero_entry.pack(pady=50)

                    tk.Button(self.root, text="Confirmar Asiento", command=lambda: self.confirmar_asiento(funcion_obj, cliente_obj)).pack(pady=50)
                    tk.Button(self.root, text="Regresar", command=self.main_menu).pack(pady=50)

                else:
                    messagebox.showerror("Error", "Cliente o función no encontrados.")
            except ValueError:
                messagebox.showerror("Error", "ID debe ser un número.")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    def seleccionar_asiento(self, fila, numero, funcion_obj):
        if funcion_obj.reservar_asiento(fila, numero):
            messagebox.showinfo("Éxito", "Asiento reservado exitosamente.")
            self.comprar_boletos()  # Refresca la pantalla para mostrar el estado actualizado de los asientos
        else:
            messagebox.showerror("Error", "Asiento no disponible o inválido.")

    def confirmar_asiento(self, funcion_obj, cliente_obj):
        fila = self.fila_entry.get().upper()
        numero = self.numero_entry.get()

        if fila and numero:
            try:
                numero = int(numero)
                if funcion_obj.reservar_asiento(fila, numero):
                    messagebox.showinfo("Éxito", "Asiento reservado exitosamente.")
                    self.main_menu()
                else:
                    messagebox.showerror("Error", "Asiento no disponible o inválido.")
            except ValueError:
                messagebox.showerror("Error", "Número de asiento debe ser un número.")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CineApp(root)
    root.mainloop()
