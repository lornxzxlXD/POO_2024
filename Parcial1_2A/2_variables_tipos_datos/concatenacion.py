#concatenar cadenas.de.caracteres.con.contenido.de variables

nombre="lorenzo alcala fernandez"
especialidad="area de desarrollo de sw multiplataforma"
carrera="ingeniero en gestion y desarrollo de sw"

#primer forma de concatenar
print("mi nombre es: "+nombre,"estoy en la especialidad de: "+especialidad, "estoy en la carrera de: "+carrera )

print("\n")
#segunda forma de concatenar 
print("mi nombre es: ",nombre,"estoy en la especialidad de: ",especialidad, "estoy en la carrera de: ",carrera )

print("\n")
#tercera forma 
print(f"mi nombre es: {nombre} estoy en la especialidad de: {especialidad} estoy en la carrera de: {carrera}" )

print("\n")
#cuarta forma 
print("mi nombre es:{} estoy en la especialidad de:{} estoy en la carrera de:{} ".format(nombre,especialidad,carrera) )
