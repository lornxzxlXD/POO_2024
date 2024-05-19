#ciclo while es estructura iteractiva que se ejecuta x veces siempre y cuando la condicion se cumpla
#y se seguira ejecutando tantas veses como sea true la condicion 

#sintaxis
# while variable in elemppento_interable (lista,rango,etc):
#  bloque de instrucciones


#ejemplo 1 crear un programa que imprima 5 veces el @

contador=1

while contador<=5:
    print("@")
    contador+=1


#crear un programa que imprima los numeros del 1 al 5 y los sume y al final imprima la suma 

contador=1

suma=0
while contador <=5 :
    print(contador)
    suma+=contador
    contador+=1

    print(f"La suma es: {suma}")

#ejemplo 3 crear un programa que imprima la tabla de multiplicar que el usuario desee

tabla=input("ingresa un numero para calcular su table de multiplicar")

i=1
multi=0

while i <=10:
    multi=i*tabla
    print(f"{tabla} x {i} = {multi}")
    i+=1
