
Temperatuta=[36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

preguntaNumero = '''Ingrese alguna de estas opciones
    1.Hacer conversión a fahrenhint o kelvin 
    2.Estado del paciente 
    3.Mostrar temperatura maxima,temperatura minima.
    4. Salir
    '''

preguntaTemperatura = '''
    C- Mostrar original en celcius
    F- Mostrar en Fahrenheit
    K- Mostrar en kelvin
'''
Temp=[]
for i in (Temperatuta):
    if (i<=36):
        Hip="hipotermia" 
        Temp.append (Hip)
    elif (i>37.6):
        Fi="Fiebre"
        Temp.append(Fi)
    elif (i>36 and i<=37):
        N="Normal"
        Temp.append(N)
print(Temp)





listakelvin = []
for i in Temperatuta:
    conversor1 =(i+273.15)
    listakelvin.append(conversor1)
listaf = []
for k in Temperatuta:
    conversor = (k*1.8+32)
    listaf.append(conversor)

opcionEscogida = int(input(preguntaNumero))

while (opcionEscogida !=4):
    if (opcionEscogida == 1):
        opciont = input(preguntaTemperatura)
        if (opciont == 'C'):
            print("No se realizo conversion no es necesaria")
            print(Temperatuta)
        elif (opciont== 'F'):
            print("conversion en fahrenheit")
            print(listaf)
        elif (opciont== 'k'):
            print("conversion kelvin")
            print(listakelvin)
        else:
            print("Error en la entrada")
    elif (opcionEscogida == 2):
        print(Temp)  
    elif (opcionEscogida == 3):
        print("La temperatura maxima es", max(Temperatuta))
        print("la temperatura minima es", min(Temperatuta))
    else:
        print("Error en la entrada")
    opcionEscogida = int(input(preguntaNumero))

print ("Muchas gracias")



        

