# importar numpy => pip install numpy
import numpy as nu
casillero = nu.array([["","",""],["","",""],["","",""] ], dtype=object) # matriz de 3x3

# definir funciones
def arrendar(casillero):
    print("**** Arriendo de casilleros *****")
    print("Ingrese tipo de casillero:")
    print("1.- Nivel 1 $10000")
    print("2.- Nivel 2 $5000")
    print("3.- Nivel 3 $2000")
    try:
        opcion = int(input("Ingrese tipo de casillero  : "))
        fila = opcion - 1
        mostrarCasillerosDisponibles(casillero, fila)
        nroCasillero = int(input("Ingrese número de casillero: "))
        columna = nroCasillero - 1
        nombre = input("Ingrese nombre del cliente : ")
        casillero[fila, columna] = nombre
        print(casillero)
    except:
        print("Error en el ingreso de opción")
        input("Presione enter para volver al menú...")
        return

def mostrarCasillerosDisponibles(casillero, fila):
    nroCasillero = 1
    print("Casilleros disponibles de la fila", fila+1 )
    for columna in casillero[fila]:
        if columna == "":
            print("", nroCasillero)
        nroCasillero +=1
        


def mostrarDisponible(casillero):
    print("*** Disponibilidad de casilleros ***")
    listado = ""
    nroCasillero = 1
    valor = ""
    for filas in casillero:
        for columna in filas:
            if columna == "":
                valor = str(nroCasillero)
            else:
                valor = "X"
            listado += valor + " " # "acumulador"
            nroCasillero+=1
        listado += "\n"
    print(listado)
    input("Presione enter para volver al menú...")



def mostrarCliente(casillero):
    print("Clientes de los casilleros")
    listado = ""
    nroCasillero = 1
    for fila in casillero:
        for columna in fila:
 #           if columna != "":
            print("casillero: ", nroCasillero, "nombre:", columna)
            nroCasillero += 1
    input("Presione enter para volver al menú...")
def mostrarGanancias(casillero):
    print("Ganancias")
    total = 0
    fil = 1
    for fila in casillero:
        for columna in fila:
            if columna != "":
                if fil == 1:
                    total += 10000
                elif fil == 2:
                    total += 5000
                elif fil == 3:
                    total += 2000            
        fil += 1
    print("Total de ganancias:", total)
    input("Presione enter para volver al menú...")
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