# rear una lista y un diccionario con el contenido de esta tabla: 

# ACCION              TERROR        DEPORTES
# MAXIMA VELOCIDAD    LA MONJA       ESPN
# ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
# RAPIDO Y FURIOSO I  LA MALDICION   ACCION

# imprimir la información

categorias = ["ACCION", "TERROR", "DEPORTES"]

peliculas_y_programas = [
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]

tabla_diccionario = {
    "ACCION": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO I"],
    "TERROR": ["LA MONJA", "EL CONJURO", "LA MALDICION"],
    "DEPORTES": ["ESPN", "MAS DEPORTE", "ACCION"]
}

print("Contenido de la lista:")
for fila in peliculas_y_programas:
    print(fila)

print("\nContenido del diccionario:")
for categoria, items in tabla_diccionario.items():
    print(f"{categoria}: {items}")
