import matplotlib.pyplot as plt 
pieLabels = ["python","java","dart","js"] #Nombres de las porciones de torta 
sizes = [50,25,15,10] #Tamaños de la porcion de la torta
pieExplode = [0,0,0.1,0] #Resaltar en el grafico (sobresalir)
acumulador = 0
for elemento in sizes :
    acumulador += elemento

for i in range (len(pieLabels)):
    pieLabels[i] += "->"+str(sizes[i]/acumulador*100)+ "%"

plt.pie(sizes,labels=pieLabels,explode=pieExplode, startangle = 45)
######
plt.title("Uso de lenguajes de programacion en el 2021")
plt.savefig("tortasLenguajes.png")
######
plt.show()
