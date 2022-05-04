# 1.- Definir variables
total = 0
# 2.- Solicitar la info
print("\n***** Venta de artículos *****")
mascarilla = int(input("Ingrese cantidad de mascarillas : "))
guantes = int(input("Ingrese cantidad de guantes     : "))
delantal = int(input("Ingrese cantidad de delantal    : "))
amonio = int(input("Ingrese cantidad de amonio      : "))
descuento = int(input("Ingrese cantidad de descuento     : "))

# 3.- procesar la info
total += mascarilla * 1000
total += guantes * 1000
total += delantal * 2000
total += amonio * 3000 # total = total + amonio * 3000

if descuento > 0:
    total -= total * descuento / 100
# 4.- mostrar los resultados

print("El total a pagar: ", total)