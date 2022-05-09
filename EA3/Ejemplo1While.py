# Definir variables
acumulador = 1
contador = 1
numero = 0
# solicitar la info al usuario
print("\n***** Factorial de un número *****")
numero = int(input("ingrese el número: "))
# procesar la información
while contador <= numero:
    acumulador *= contador
    contador += 1  # contador = contador + 1
# mostrar resultados
print("El factorial de el numero", numero, "es", acumulador)