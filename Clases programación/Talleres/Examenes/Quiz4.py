snacksFavoritos = input ("Ingrese sus cinco snacks favoritos")
precios = input ("Ingrese el valor de cada uno de sus snacks favoritos")

import matplotlib.pyplot as plt 
snacksFavoritos = []
precios = []
plt.bar(snacksFavoritos,precios, color = "m")
plt.title("Snacks favoritos y su respectivo precio")
plt.xlabel("Snacks favoritos")
plt.ylabel("Precio")
plt.savefig("Graficosnacks.png")
plt.show()

ciudadesFavoritas = input ("Ingrese sus cinco ciudades favoritas en el mundo")
poblaciones = float(input ("Ingrese las poblaciones de cada una de sus ciudades favoritas"))
labels = [ciudadesFavoritas]
sizes = [poblaciones]
pieExplode = []
plt.pie(sizes, labels=ciudadesFavoritas, explode=pieExplode)
plt.title("Ciudades del mundo con sus respectivas poblaciones")
plt.savefig("GraficoCiudades.png")
plt.show()

print ("El ecg es la representación visual de la actividad eléctrica del corazón en función del tiempo")
print("El ppg es una técnica de pletismografía en la cual se utiliza un haz de luz para determinar el volumen de un órgano")

import pandas as pd 
import matplotlib.pyplot as plt 
ecgData =pd.read_csv("ecg.csv",encoding= "UTF-8",header=0,delimiter=";").to_dict()
print(ecgData.keys())
muestras = list(ecgData["muestra"].values())
print(muestras)
tiempo = list(ecgData["valor"].values())
print(tiempo[-8])
plt.plot(muestras,tiempo)
plt.title("ecg")
plt.xlabel("muestras")
plt.ylabel("tiempo")
plt.savefig("Graficoecg.png")
plt.show()

import pandas as pd 
import matplotlib.pyplot as plt 
ppgData =pd.read_csv("ppg.csv",encoding= "UTF-8",header=0,delimiter=";").to_dict()
print(ppgData.keys())
muestras = list(ppgData["muestra"].values())
print(muestras)
volumen = list(ppgData["valor"].values())
print(volumen[-8])
plt.plot(muestras,volumen)
plt.title("ppg")
plt.xlabel("muestras")
plt.ylabel("volumen")
plt.savefig("Graficoppg.png")
plt.show()


