#----Constantes----#
MENSAJE_BIENVENIDA = "Bienvenido al codigo"
MENSAJE_MAYOR_EDAD = "Eres mayor de edad puedes seguir"
MENSAJE_MENOR_EDAD = "Eres menor de edad no puedes seguir"
PREGUNTA_EDAD = "Cuantos años tienes ? :"

#----Entrada al codigo----#
print (MENSAJE_BIENVENIDA)
edad = int (imput(PREGUNTA_EDAD))
isMAYOR = edad >= 18
resultado = ""
if (isMAYOR):
    resultado = MENSAJE_MAYOR_EDAD
else: 
    resultado = MENSAJE_MENOR_EDAD

print (resultado)
