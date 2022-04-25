from pydoc import describe


print("**********  Cine Duoc *********")

print("UD es de DUOC UC PLAZA OESTE de CERRILLOS de Americo Vespucio 1501")
esDuonino = input("presione 1.- SI  2.- No")

print("Tipo de entrada")
print("1.- Estreno")
print("2.- Normal")
tipoEntrada = input("Seleccione el tipo de entrada: ")
cantidadEntrada = input("Ingrese la cantidad a comprar: ")


print("Tamaño de las palomitas")
print("1.- Pequeña")
print("2.- Mediana")
print("3.- Grande")
tamanoPalomitas = input("Seleccione el tamaño:")
cantidadPalomitas = input("Ingrese la cantidad a comprar: ")


print("Tamaño de la Bebida")
print("1.- Pequeña")
print("2.- Mediana")
print("3.- Grande")
tamanoBebida = input("Seleccione el tamaño:")
cantidadBebida = input("Ingrese la cantidad a comprar: ")

## agregar los if para hacer el cobro
subTotal = 0
valor = 0

if tipoEntrada == "1":
    valor = 4800
else:
    valor = 2800

subTotal = valor * int(cantidadEntrada)

if tamanoPalomitas == "1":
    valor = 2500
elif tamanoPalomitas == "2":
    valor = 4500
else:
    valor = 7800

subTotal = subTotal + valor * int(cantidadPalomitas)

if tamanoBebida == "1":
    valor = 1000
elif tamanoBebida == "2":
    valor = 1250
else:
    valor = 2000

subTotal = subTotal + valor * int(cantidadBebida)

descuento = 0
if esDuonino == "1":
    descuento = subTotal * .3
    
print("---------------------------------------")
print("Subtotal     : ", subTotal)
print("Descuento    : ", descuento)
print("Total a pagar: ", (subTotal - descuento))
print("---------------------------------------")