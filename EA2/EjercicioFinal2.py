# 1.- Definir variables
# 2.- Solicitar la info
print("\n***** Registro de persona *****")
nombre  = input("Ingrese su nombre   : ")
edad    = input("Ingrese su edad     : ")
telefono= input("Ingrese su teléfono : ")
genero  = input("Ingrese su género 1.-Varón 2.-Mujer : ")

# 3.- procesar la info
# 4.- mostrar los resultados

if genero == "1":
    print(f"Su nombre es {nombre} y su edad {edad}")
else:
    print(f"Su nombre es {nombre} y su télefono {telefono}")