def mostrarOperaciones (numero):
    suma = sum(numero)
    resta = rest(numero)
    multiplicacion = multi(numero)
    division = divi(numero)
    potencia = pot(numero)
    for elemento in lista:




def mostrarListas (lista):
animales = ["perro","vaca","gato","caballo"]
formas = ["cuadrado","rectangulo","circulo","ovalo"]
ciudades = ["medellin","bogota","manizales","barranquilla"]

print(animales)
print(formas)
print(ciudades)

def calcularArea (base,altura):
    return (base*altura)/2 
    base = input ("ingrese la base")
    altura = input ("ingrese la altura")
area = calcularArea (base*altura)/2
print (area)

def mostrarNumeros (lista):
    mayor = max(lista)
    menor = min(lista)
    acumulador = 0
    for elemento in lista:
        acumulador += elemento
    tamañoLista = len (lista)
    promedio = acumulador / tamañoLista 
    print (f"el numero maximo de la lista es {mayor}, el minimo {menor} y el promedio {promedio}")
numeros = [21,20,18,17,15,6,3]
mostrarNumeros(numeros)


