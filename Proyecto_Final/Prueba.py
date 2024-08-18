import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cinebd.db"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes WHERE ID_Cliente = 2")
cliente = cursor.fetchone()
print(cliente)

conn.close()
