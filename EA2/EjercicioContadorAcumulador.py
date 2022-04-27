# definir variables
suma = 0
contador = 0

# solicitar  datos al usuario
print("==== Clasificación de números ingresados ====")
n1 = input("Ingrese el número 1:")
n2 = int(input("Ingrese el número 2:"))
n3 = int(input("Ingrese el número 3:"))

n1 = int(n1)

#procesar información
if n1 > 0 and n1 % 2 == 0:
    suma = n1
else:
    contador += 1 # contador = contador + 1

if n2 > 0 and n2 % 2 == 0:
    suma += n2
else:
    contador += 1 

if n3 > 0 and n3 % 2 == 0:
    suma += n3
else:
    contador += 1 

# mostrar resultados

print("LA suma total es:", suma)
print("Cantidad de numeros que no coinciden:", contador)