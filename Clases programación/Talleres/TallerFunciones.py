def mostrarLista (lista):
    for elemento in lista:
        print (elemento)

frutas = ["fresa","kiwi","piña"]
colores = ["rojo","verde","amarillo"]
mostrarLista(frutas)
mostrarLista(colores)


def mostrarNumeros (lista):
    mayor = max(lista)
    menor = min(lista)
    acumulador = 0
    for elemento in lista:
        acumulador += elemento
    tamañoLista = len (lista)
    promedio = acumulador / tamañoLista 
    print (f"el numero mayor de la lista es {mayor}, el menor {menor} y el promedio {promedio}")
numeros = [21,20,18,17,15,6,3]
mostrarNumeros(numeros)


def saludar (cantidad = 0):
    print ("hola"*cantidad)
saludar(8)

def devolverNumerosPares (lista):
    pares = []
    for elemento in lista:
        if elemento % 2 == 0 :
            pares.append (elemento)
    return pares

numeros = [21,20,18,17,15,6,3]
numerosPares = devolverNumerosPares(numeros)
print (numerosPares)


def listaMayores (lista):
    mayores = []
    for elemento in lista:
        if elemento > 24 :
            mayores.append (elemento)
    return mayores
numeros = [21,20,18,17,15,6,3]
numerosMayores = listaMayores(numeros)
print (numerosMayores)

def calcularIMC (peso, altura):
    return peso / (altura**2)
imc = calcularIMC(56,1.55)
print (imc)


def despedir():
    print("hasta pronto")
despedir()

