print("Señalar digitos de un numero")
numero = int(input("Ingrese un numero:"))

if numero > 999:
    print("Numero no valido")
elif numero > 99:
    print("El numero tiene 3 digitos")
elif numero > 9:
    print("El numero tiene 2 digitos")
else:
    print("El numero tiene 1 digitos")