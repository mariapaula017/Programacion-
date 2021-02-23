#----Constnates----#
TRIGLICERIDOS = "Ingrese su nivel de trigliceridos"
HOMOCISTEINA = "Ingrese su nivel de homocisteina"

trigliceridos = float (input (TRIGLICERIDOS))
homocisteina = float (input (HOMOCISTEINA))

if (homocisteina >=2 and homocisteina <15):
    print("El nivel de su homocisteina es optimo")
elif (homocisteina >=15 and homocisteina < 30):
    print("El nivel de su homocisteina es sobre el limite optimo")
elif (homocisteina >=30 and homocisteina < 100):
    print("El nivel de su homocisteina es alto")
else:
    print("El nivel de su homocisteina es muy alto")


if (trigliceridos < 150):
    print("El nivel de su trigliceridos es optimo")
elif (trigliceridos>=150 and trigliceridos < 199):
    print("El nivel de su trgliceridos es sobre el limite optimo")
elif ( trigliceridos>=200 and trigliceridos< 499):
    print("El nivel de su trigliceridos es alto")
else:
    print("El nivel de su trigliceridos muy alto")

