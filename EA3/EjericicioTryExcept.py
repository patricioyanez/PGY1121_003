# Ejercicios:
# agregar Try Except a menú de ejercicio Menú Panadería.
opcion = 0
total = 0

while opcion != 6:
    print("===== Menú Principal =====")
    print("1.- Pan Amasado")
    print("2.- Pan Molde")
    print("3.- Pan Baguette")
    print("4.- Pan Integral")
    print("5.- Total de compra")
    print("6.- Salir del programa")
    try:
        opcion = int(input("Ingrese opción: "))
    except:
        input("Tipo de dato no es válido. Presione enter para continuar")
        continue
    
    if opcion < 1 or opcion > 6:
        print("///////////// E R R O R")
        input("Opción no válida. Presione enter para continuar")
    elif opcion == 6:
        print("Aplicación cerrada")
    elif opcion == 5:
        if total < 5000:
            total *= 1.1
        else:
            print("El envio es gratis")
        print("El total a pagar es:", int(total))
        input("Presione enter para continuar")
        total = 0
    else:
        try:
            cantidad = int(input("Ingrese cantidad de producto: "))
        except:
            input("Tipo de dato no es válido. Presione enter para continuar")
            continue
        
        if opcion == 1:
            total += cantidad * 1500
        elif opcion == 2:
            total += cantidad * 1000
        elif opcion == 3:
            total += cantidad * 2000
        elif opcion == 4:
            total += cantidad * 3000





