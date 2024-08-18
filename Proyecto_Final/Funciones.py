from ConexionCineBD import *

class Persona:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def getNombre(self) -> str:
        return self.nombre

    def getEdad(self) -> int:
        return self.edad

    def getID(self) -> int:
        return getattr(self, 'ID', None)  # Cambiado para evitar AttributeError

class Cliente(Persona):
    def __init__(self, id_cliente, nombre, apellidos, edad):
        super().__init__(nombre, apellidos, edad)
        self.id_cliente = id_cliente

    def getID(self) -> int:
        return self.id_cliente

class Empleado(Persona):
    def __init__(self, nombre: str, edad: int, ID: int, puesto: str, salario: float):
        super().__init__(nombre, ID, edad)
        self.puesto = puesto
        self.salario = salario

    def getPuesto(self) -> str:
        return self.puesto

    def getSalario(self) -> float:
        return self.salario

class Sala:
    def __init__(self, numero: int, capacidad: int, tipo: str, ID_Sala: int):
        self.numero = numero
        self.capacidad = capacidad
        self.tipo = tipo
        self.ID = ID_Sala

    def getNumero(self) -> int:
        return self.numero

    def getCapacidad(self) -> int:
        return self.capacidad

    def getTipo(self) -> str:
        return self.tipo

    def getID(self) -> int:
        return self.ID

class Pelicula:
    def __init__(self, titulo: str, duracion: int, genero: str, director: str, clasificacion: str, ID_Pelicula: int):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero
        self.director = director
        self.clasificacion = clasificacion
        self.ID = ID_Pelicula

    def getID(self) -> int:
        return self.ID

    def getTitulo(self) -> str:
        return self.titulo

    def getDuracion(self) -> int:
        return self.duracion

    def getGenero(self) -> str:
        return self.genero

    def getDirector(self) -> str:
        return self.director

    def getClasificacion(self) -> str:
        return self.clasificacion

class Funcion:
    def __init__(self, hora: str, sala: Sala, pelicula: Pelicula, ID_Funcion: int):
        self.hora = hora
        self.sala = sala
        self.pelicula = pelicula
        self.ID = ID_Funcion
        self.asientos_disponibles = self.generar_asientos()

    def generar_asientos(self):
        asientos = {}
        filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        for fila in filas:
            asientos[fila] = [True] * 10  # 10 asientos por fila
        return asientos

    def mostrar_asientos(self):
        # Método para obtener la representación en texto de los asientos
        resultado = ""
        for fila, asientos in self.asientos_disponibles.items():
            asientos_str = ' '.join('O' if disponible else 'X' for disponible in asientos)
            resultado += f"Fila {fila}: {asientos_str}\n"
        return resultado

    def reservar_asiento(self, fila: str, numero: int) -> bool:
        if fila in self.asientos_disponibles and 1 <= numero <= 10:
            if self.asientos_disponibles[fila][numero - 1]:
                self.asientos_disponibles[fila][numero - 1] = False
                return True
            else:
                return False
        else:
            return False

    def getID(self) -> int:
        return self.ID

    def getHora(self) -> str:
        return self.hora

    def getSala(self) -> Sala:
        return self.sala

    def getPelicula(self) -> Pelicula:
        return self.pelicula

class Boleto:
    def __init__(self, codigo: str, cliente: Cliente, funcion: Funcion, precio: float):
        self.codigo = codigo
        self.cliente = cliente
        self.funcion = funcion
        self.precio = precio

    def getCodigo(self) -> str:
        return self.codigo

    def getCliente(self) -> Cliente:
        return self.cliente

    def getFuncion(self) -> Funcion:
        return self.funcion

    def getPrecio(self) -> float:
        return self.precio


# Funciones adicionales

def mostrar_cartelera(db_manager: DatabaseManager):
    peliculas = db_manager.seleccionar_datos("SELECT * FROM peliculas")
    print("Cartelera de Películas:")
    for pelicula in peliculas:
        print(f"ID: {pelicula[0]}, Título: {pelicula[1]}, Duración: {pelicula[2]} min, Género: {pelicula[3]}, Director: {pelicula[4]}, Clasificación: {pelicula[5]}")

def registrar_cliente(db_manager: DatabaseManager, nombre: str, apellidos: str, edad: int):
    db_manager.ejecutar_consulta("INSERT INTO clientes (nombre, apellidos, edad) VALUES (%s, %s, %s)", (nombre, apellidos, edad))
    print(f"Cliente registrado: {nombre} {apellidos}, Edad: {edad}")

def comprar_boletos(db_manager: DatabaseManager, cliente_id: int, funcion_id: int):
    cliente = db_manager.seleccionar_datos("SELECT * FROM clientes WHERE id_cliente = %s", (cliente_id,))
    funcion = db_manager.seleccionar_datos("SELECT * FROM funciones WHERE id_funcion = %s", (funcion_id,))
    
    if cliente and funcion:
        cliente_obj = Cliente(cliente[0][0], cliente[0][1], cliente[0][2], cliente[0][3])  # ID, Nombre, Apellidos, Edad
        sala_data = db_manager.seleccionar_datos("SELECT * FROM salas WHERE id_sala = %s", (funcion[0][2],))
        pelicula_data = db_manager.seleccionar_datos("SELECT * FROM peliculas WHERE id_pelicula = %s", (funcion[0][3],))
        sala = Sala(sala_data[0][1], sala_data[0][2], sala_data[0][3], sala_data[0][0])
        pelicula = Pelicula(pelicula_data[0][1], pelicula_data[0][2], pelicula_data[0][3], pelicula_data[0][4], pelicula_data[0][5], pelicula_data[0][0])
        funcion_obj = Funcion(funcion[0][1], sala, pelicula, funcion[0][0])

        nuevo_codigo = f"B{db_manager.seleccionar_datos('SELECT COUNT(*) FROM boletos')[0][0] + 1:03}"
        boleto = Boleto(nuevo_codigo, cliente_obj, funcion_obj, 150.00)

        print("Seleccione un asiento:")
        funcion_obj.mostrar_asientos()
        fila = input("Ingrese la fila (A-G): ").upper()
        numero = int(input("Ingrese el número de asiento (1-10): "))
        
        if funcion_obj.reservar_asiento(fila, numero):
            db_manager.ejecutar_consulta("INSERT INTO boletos (codigo, cliente_id, funcion_id, precio) VALUES (%s, %s, %s, %s)",
                                         (boleto.getCodigo(), boleto.getCliente().getID(), boleto.getFuncion().getID(), boleto.getPrecio()))
            print(f"Boleto comprado. Código: {boleto.getCodigo()}, Cliente: {boleto.getCliente().getNombre()}, Asiento: {fila}{numero}, Función: {boleto.getFuncion().getHora()}")
        else:
            print("Asiento no disponible o inválido. Intente nuevamente.")
    else:
        print("Cliente o función no encontrados.")

def compras_dulceria(db_manager: DatabaseManager, cliente_id: int):
    productos = {"Palomitas": 50, "Refresco": 40, "Nachos": 60, "Icee": 45, "Chocolate": 30}
    total = 0

    print(".::Dulcería::.")
    for producto, precio in productos.items():
        print(f"{producto}: ${precio}")

    while True:
        producto = input("Ingrese el nombre del producto que desea comprar (o 'salir' para terminar): ").capitalize()
        if producto == "Salir":
            break
        elif producto in productos:
            total += productos[producto]
        else:
            print("Producto no disponible.")

    if total > 0:
        db_manager.ejecutar_consulta("INSERT INTO compras_dulceria (cliente_id, total) VALUES (%s, %s)", (cliente_id, total))
        print(f"Compra realizada. Total: ${total}")
    else:
        print("No se realizaron compras.")

# Función para el menú
def mostrar_menu():
    print("\n--- Gestión de Cine ---")
    print("1. Comprar boletos")
    print("2. Ver cartelera de películas")
    print("3. Comprar en dulcería")
    print("4. Registrar nuevo cliente")
    print("5. Salir")

    return int(input("Seleccione una opción: "))
