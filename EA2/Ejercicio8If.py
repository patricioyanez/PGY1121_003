total = 0
print("****  Convertidor a Pesos chilenos")
pesos = input("Ingrese cantidad de moneda a convertir")
pesos = int(pesos)
print("Monedas")
print("1-. Dolar Australianos")
print("2-. Pesos Argentinos")
print("3-. Yen")
opcion = input("Ingrese opción: ")

if opcion == "1":
    total = pesos * 700
elif opcion == "2":
    total = pesos * 30
elif opcion == "3":
    total = pesos * 500

print("El total es: ", int(total))