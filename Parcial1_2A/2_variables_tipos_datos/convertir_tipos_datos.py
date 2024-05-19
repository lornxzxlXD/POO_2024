""""
comentario de varias lineas
Nota: a ala hora de concatenar no es posible incluir en
algunas ocaciones contenido de variables que no sean del tipo str
"""

#comentario de una linea

#concatenar un str con str 


texto="soy una cadena de texto"
numero=23
print(texto+" y soy otra cadena ")

#concatenar un int con str 

numero=23
numero_str=str(numero)
print("el numero:"+numero_str)


print("el numero:"+str(numero))

#concatenar un str con int 
n1='23'
n2=33
suma=int(n1)+n2

print("el numero: " +str(numero))

#concatenar un float y int con un str
n1='23'
n2=33.0
suma=int(n1)+n2

print("el numero: " +str(int(numero)))
print(f"el numero : {int(suma)}")

#concatenar un float y float con float 
n1='23.34'
n2='33..99'

suma=float(n1)+float(n2)
print(f"el numero: {suma}")
