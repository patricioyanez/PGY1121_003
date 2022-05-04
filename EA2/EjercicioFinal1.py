# 1.- Definir variables
# 2.- Solicitar la info

print("\n***** Conocer mayor de tres números *****")
n1 = int(input("Ingrese el nro 1: "))
n2 = input("Ingrese el nro 2: ")
n3 = input("Ingrese el nro 3: ")

# 3.- procesar la info
# 4.- mostrar los resultados

n2 = int(n2)
n3 = int(n3)

if n1 > n2 and n1 > n3:
    print("El 1er nro es mayor")
elif n2 > n3:
    print("El 2do nro es mayor")
else:
    print("El 3er nro es mayor")

