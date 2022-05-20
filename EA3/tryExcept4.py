try:
    c = a / b
    print(f"El resultado es: {c}")
except ZeroDivisionError:
    print("Error de división por cero.")
except :
    print("Error: variables no inicializadas")
finally:
    print("El bloque se ejecutó con éxito")

print("Fin de aplicación")