import matplotlib.pyplot as plt
mes = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
ingresos = ["350.000","780.00","230.000","650.000","500.00","800.00","150.000","450.000","900.000","750.000","970.00","450.000"]
plt.bar(mes,ingresos, width = 0.8, color = "m")

plt.title("Ingresos durante el 2020")
plt.xlabel("Mes")
plt.ylabel("Ingresos")
plt.savefig("GraficoIngresos.png")

plt.show()

pieLabels = ["medellin","bogota","cali","pereira","barranquilla"] 
sizes = [23,25,17,14,21]
pieExplode = [0,0.3,0,0,0]

plt.pie(sizes,labels=pieLabels, explode = pieExplode)
plt.title("Ciudades de colombia")
plt.savefig("TortaCiudades.png")

plt.show()

