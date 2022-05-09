# Definir variables
contador = 0
numero = 0
resultado = 0
# solicitar la info al usuario
print("\n***** solicitar números ejemplo 2 *****")

# procesar la información
while contador < 5:
    numero = int(input("Ingrese un número: "))
    if numero > 0:
        resultado += numero
        contador += 1  # contador = contador + 1
# mostrar resultados
print("La suma de los 5 numeros es", resultado)