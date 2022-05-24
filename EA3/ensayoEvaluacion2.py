listadoCliente = []
rut = 0
nombre = ""
direccion = ""
comuna = ""
correo = ""
edad = -1
genero = ""
celular = ""
tipoCliente = ""
suscrito = True

opcion = 0

while opcion != 4:
    print("****** M E N Ú - J U A N  M A E S T R O *******")
    print("1.- Registrar cliente")
    print("2.- Suscripción")
    print("3.- Consulta de datos")
    print("4.- Salir")

    try:
        opcion = int(input("Ingrese opción:"))
    except:
        print("Error en el ingreso de datos")
        input("Presione enter para continuar....")
        continue
    
    if opcion == 1:
        print("Ingreso a la opción 1")
        listadoCliente.append([1,2,3,4,5])
    elif opcion == 2:
        print("Ingreso a la opción 2")
    elif opcion == 3:
        print("Ingreso a la opción 3")
    elif opcion == 4:
        print("Aplicación cerrada")
    input("===== Presione enter para continuar...")
