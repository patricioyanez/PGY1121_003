
try:
    numero = int(input("Ingrese un número:"))
except ValueError:
    print("Debe ingresar un valor entero")
except:
    print("No es el valor esperado")
finally:
    print("El bloque try ha finalizado")