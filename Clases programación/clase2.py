# Estos son booleans que son variables que solo valen 
# verdadero falso 
pruebaV = True 
pruebaF = False
print("pruebaF")
print("pruebaV")
pruebaV = pruebaF
print ("pruebaV")
edad = 20
estatura = 1.55
peso = 57
NOMBRE = "Maria Paula Suarez V"
print("#"*15,"Mayor Edad", "#"*15)
isMayorEdad = edad  >= 18
print(isMayorEdad)
print("#"*15,"Bajo la Estatura promedio", "#"*15)
isMayorEstatura = estatura < 1.70
print(isMayorEstatura)
# calculando si el peso diferente de 57
isPesoDiferente = peso != 57
print("#"*15, "peso diferente 57", "#"*15)
print(isPesoDiferente)
# vamos a ver si un apellido esta en el nombre completo
apellido = "Suarez"
isApellido = apellido in NOMBRE
print("#"*15, "Esta apellido en el nombre ", "#"*15)
print (isApellido)




