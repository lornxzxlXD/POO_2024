#ciclo for estructura que ejecuta x veces

#sintaxis
# for variable in elemppento_interable (lista,rango,etc):
#  bloque de instrucciones


#ejemplo 1 crear un programa que imprima 5 veces el @

contador=1

for contador in range(1,6):
    print("@")


#crear un programa que imprima los numeros del 1 al 5 y los sume y al final imprima la suma 

contador=1

suma=0
for contador in range (1,6):
    print(contador)
    suma+=contador

    print(f"La suma es: {suma}")

#ejemplo 3 crear un programa que imprima la tabla de multiplicar que el usuario desee

tabla=input("ingresa un numero para calcular su table de multiplicar")

i=1
multi=0

for i in range(1,11):
    multi=i*tabla
    print(f"{tabla} x {i} = {multi}")
    