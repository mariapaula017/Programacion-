#----Constantes----#
numeroA = 17
numeroB = 20
PREGUNTA_NUMERO_A = "Ingrese un numero A :"
PREGUNTA_NUMERO_B = "Ingrese un numero B :"

#----Mensajes----#
MENSAJE_MAYOR = "El numero A es mayor que el numero B"
MENSAJE_MENOR = "El numero A es menor que el numero B"
MENSAJE_IGUAL = "El numero A y B son iguales"
MENSAJE_DIFERENTE = "El numero A es diferente al numero B"

#----Operaciones----#
sumar = numeroA + numeroB
print ("el resultado de la suma es", sumar)
restar = numeroA - numeroB
print ("el resultado de la resta es", restar)
multiplicar = numeroA * numeroB
print ("el resultado de la muntiplicacion es", multiplicar)
dividir = numeroA / numeroB
print ("el resultado de la division es", dividir)
exponente = numeroA**numeroB
print ("la exponente dio", exponente)

#----Entrada al codigo----#
numeroA = int (input(PREGUNTA_NUMERO_A))
numeroB = int (input(PREGUNTA_NUMERO_B))
isMayor = numeroA > numeroB
isMenor = numeroA < numeroB
isIgual = numeroA == numeroB
isDiferente = numeroA != numeroB 

#----Condicionales----#
if (isMayor):
    print (MENSAJE_MAYOR)
elif (isMenor):
    print (MENSAJE_MENOR)
elif (isIgual):
    print (MENSAJE_IGUAL)
else: (MENSAJE_DIFERENTE)


