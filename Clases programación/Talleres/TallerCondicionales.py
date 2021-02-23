#----Constantes----#
INGRESE_NUMERO_A = "Ingresar numero A: "
INGRESE_NUMERO_B = "Ingresar numero B: "
MENSAJE_MAYOR = "El numero A es mayor que el numero B,  A > B"
MENSAJE_IGUAL ="El numero A y B son iguales, A == B"

#----Entrada al codigo----#
numeroA = int (input(INGRESE_NUMERO_A))
numeroB = int (input(INGRESE_NUMERO_B))
isMayorA = numeroA > numeroB
isMayorB = numeroB > numeroA
isIgual = numeroA == numeroB
resultado = ""

#----Condicionales----#
if (isMayorA):
    resultado = MENSAJE_MAYOR
elif (isMayorB):
    resultado = MENSAJE_MAYOR
else:
    resultado = MENSAJE_IGUAL


print(resultado)


#----Constantes----#
INGRESE_EDAD = "Ingresar edad: "
MENSAJE_MENOR_EDAD = "Tienes menos de 18 años eres menor de edad"
MENSAJE_JOVEN = "Eres joven"
MENSAJE_ADULTO = "Eres adulto"
MENSAJE_ADULTO_MAYOR = "Eres un adulto mayor"

#----Entrada al codigo----#
edad = int (input(INGRESE_EDAD))
isMenor = edad < 18
isJoven = edad >=  18 and edad < 26
isAdulto = edad >= 26 and edad < 61
IsAdultoMayor = edad > 61
resultado = ""

#----Condicionales----#
if (isMenor):
    resultado = MENSAJE_MENOR_EDAD
elif (isJoven):
    resultado = MENSAJE_JOVEN
elif (isAdulto):
    resultado = MENSAJE_ADULTO
else:
    resultado = MENSAJE_ADULTO_MAYOR

print (resultado)


#----Constantes----#
INGRESE_AÑO_ACTUAL = "Ingresae el año actual: "
INGRESE_AÑO_CUALQUIERA = "Ingrese un año cualquiera: "
MENSAJE_IGUALES = "Los años ingresados son iguales"
MENSAJE_AÑOS_PASADOS = "Han pasado, resta"
MENSAJE_AÑOS_FALTANTES = "Faltan, resta"

#----Entrada al codigo----#
añoAcutual = int (input(INGRESE_AÑO_ACTUAL))
añoCualquiera = int (input(INGRESE_AÑO_CUALQUIERA))
isMayorActual = añoAcutual > añoCualquiera
isMayorCualquiera = añoCualquiera > añoActual
resultado = ""

#----Condicionales----#
if (isMayorActual):
resta = añoAcutual - añoCualquiera
    resultado = MENSAJE_AÑOS_PASADOS
elif (isMayorCualquiera):
resta = añoCualquiera - añoAcutual
    resultado = MENSAJE_AÑOS_FALTANTES
else: 
    resultado (MENSAJE_IGUALES)

print(resultado)


#----Constantes----#
INGRESE_DISTANCIA_CENTIMETROS = "Ingrese la distancia en centimetros :"
INGRESE_UNIDAD_DESEADA = "Ingrese la unidad que desea : K- Kilometros, M- Metros :"
MENSAJE_ERROR = "Unidad incorrecta"
#----Entrada al codigo----#
medida = float (input(INGRESE_DISTANCIA_CENTIMETROS))
unidad = input(INGRESE_UNIDAD_DESEADA) 

#----Conversiones----#
metros = medida *10**-2
kilometros = medida*10**-5

resultado = ""
#----Condicionales----#
if (unidad == "K"):
    resultado = kilometros 
elif (unidad == "M"):
    resultado = metros 
else:
    resultado = MENSAJE_ERROR

Print (resultado)