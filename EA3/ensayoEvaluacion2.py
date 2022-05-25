clientes = []
rut = ""
nombre = ""
direccion = ""
comuna = ""
correo = ""
edad = -1
genero = ""
celular =""
tipo =""
suscrito = True

opcion = 0

while opcion != 4:
    print("**************  M E N Ú - JUAN MAESTRO  **************")
    print("1.- Registro")
    print("2.- Suscripción")
    print("3.- Consultar")
    print("4.- Salir")

    try:
        opcion = int(input("Ingrese la opción:"))
    except:
        print("Error en el ingreso de la opción")
        input("Presione enter para continuar......")
        continue

    if opcion == 1:
        print("Seleccionó la opción 1")
        try:
            rut = int(input("Ingrese su rut: "))
        
            if rut < 4000000 or rut > 99999999:
                raise("El rut está fuera del rango")
        except:
            print("El rut no es válido")
            input("Presione enter para continuar......")
            continue
        
        nombre      = input("ingrese su nombre       : ")
        direccion   = input("ingrese su direccion    : ")
        comuna      = input("ingrese su comuna       : ")

        correo      = input("ingrese su correo       : ")

        if correo.count("@") != 1: # cuenta las apariciones del @
            print("El correo no es válido")
            input("Presione enter para continuar......")
            continue

        try:
            edad = int(input("Ingrese su edad: "))
        
            if edad < 0 or edad > 110:
                raise("La edad está fuera del rango")
        except:
            print("El edad no es válido")
            input("Presione enter para continuar......")
            continue

        genero = input("Ingrese su género (F o M):")
        genero = genero.upper()
        if not genero in ['F', 'M']:
            print("El genero no es válido")
            input("Presione enter para continuar......")
            continue
        
        celular = input("ingrese su celular :")
        tipo = input("Ingrese tipo de cliente 1.-Premium 2.-Gold 3.-Silver")
        if not tipo in ['1', '2', '3']:
            print("El tipo no es válido")
            input("Presione enter para continuar......")
            continue

        cliente = [rut, nombre, direccion, comuna, correo, edad,genero,celular,tipo, suscrito]
        clientes.append(cliente)

    elif opcion == 2:
        print("Seleccionó la opción 2")
        try:
            rut = int(input("Ingrese su rut: "))        
            if rut < 4000000 or rut > 99999999:
                raise("El rut está fuera del rango")
        except:
            print("El rut no es válido")
            input("Presione enter para continuar......")
            continue

        fueEncontrado = False
        for cliente in clientes:
            if cliente[0] == rut:
                cliente.append("25-05-2022")
                print("El cliente está suscrito")
                fueEncontrado = True
                break
        
        if not fueEncontrado:
            print("El cliente no fue encontrado :(")
            input("Presione enter para continuar......")

    elif opcion == 3:
        print("Seleccionó la opción 3")

        try:
            rut = int(input("Ingrese su rut: "))        
            if rut < 4000000 or rut > 99999999:
                raise("El rut está fuera del rango")
        except:
            print("El rut no es válido")
            input("Presione enter para continuar......")
            continue

        clienteEncontrado = []
        for cliente in clientes:
            if cliente[0] == rut:
                clienteEncontrado = cliente
                break
        
        if len(clienteEncontrado) == 0:
            print("El cliente no fue encontrado")
            input("Presione enter para continuar......")
        else:
            print("Datos del cliente encontrado") 
            print("Rut              :", clienteEncontrado[0])
            print("Nombre           :", clienteEncontrado[1])
            print("Dirección        :", clienteEncontrado[2])
            print("Comuna           :", clienteEncontrado[3])
            print("Correo           :", clienteEncontrado[4])
            print("Edad             :", clienteEncontrado[5])
            print("Genero           :", clienteEncontrado[6])
            print("Celular          :", clienteEncontrado[7])
            print("Tipo             :", clienteEncontrado[8])
            print("Fecha Suscripción:", clienteEncontrado[10])     


    elif opcion == 4:
        print("Aplicación cerrada")

    
    input("Presione enter para continuar.....")
