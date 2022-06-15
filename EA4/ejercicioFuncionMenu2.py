# importar numpy => pip install numpy
import numpy as nu
casillero = nu.array([["","",""],["","",""],["","",""] ]) # matriz de 3x3

# definir funciones
def arrendar(casillero):
    pass
def mostrarDisponible(casillero):
    pass
def mostrarCliente(casillero):
    pass
def mostrarGanancias(casillero):
    pass
# inicar app
opcion = "0"
listaDeOpciones = ["1","2","3","4","5"]
while opcion != "5":
    print("\n ********* Arriendo de casilleros ********")
    print("==== Menu principal ====")
    print("1.- Arrendar")
    print("2.- Mostrar ubicaciones disponibles") # 1 2 3 ocupadas X X X
    print("3.- Ver los clientes")
    print("4.- Calcular el total de ventas")
    print("5.- Salir")
    opcion = input("Ingrese una opción:")

    if opcion not in listaDeOpciones:
        print("Opción no es válida")
        input("Presione enter para continuar...")
        continue

    if opcion == "5":
        print("Adiós :)")
    else:
        if opcion == "1":
            arrendar(casillero)
        if opcion == "2":
            mostrarDisponible(casillero)
        if opcion == "3":
            mostrarCliente(casillero)
        if opcion == "4":
            mostrarGanancias(casillero)