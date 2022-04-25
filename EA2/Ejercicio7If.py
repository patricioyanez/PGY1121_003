# definir variables
total = 0
# solicitar la info al usuario
print("****** Super Zapatería de Al Bondy")
numeroZapato = input("Ingrese número de zapato")
cantidad = input("Ingrese cantidad")
# procesar la información
cantidad = int(cantidad)
if cantidad < 2:
    total = 23000
else:
    total = cantidad * 20000
# mostrar los resultados
print("El total a pagar es: ", total)
