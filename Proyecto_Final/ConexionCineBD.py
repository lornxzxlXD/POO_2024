import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, db_name):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        self.cursor = self.connection.cursor()

    def seleccionar_datos(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        return self.cursor.fetchall()

    def ejecutar_query(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        self.connection.commit()

    def cerrar_conexion(self):
        self.cursor.close()
        self.connection.close()


    def ejecutar_consulta(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        self.connection.commit()

    def seleccionar_datos(self, consulta, parametros=()):
        self.cursor.execute(consulta, parametros)
        return self.cursor.fetchall()
