numero = input("Ingrese un número:")
try:
    if not type(numero) is int:
        raise("No es un número")
except:
    print("No es el valor esperado")
finally:
    print("El bloque try ha finalizado")