edad = input("Ingrese su edad: ")
edad = int(edad)
if edad < 18:
    print("Es menor de edad")
elif edad < 65: # permite evaluar otra condicion de una variable
     print("Es mayor de edad")
else: # sino
    print("Adulto mayor")

print("************ app cerrada")