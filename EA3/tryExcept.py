a = 5
b = 0
try:
    c = a / b
    print(f"El resultado es: {c}")
except ZeroDivisionError:
    print("Error de división por cero.")

print("Fin de aplicación")