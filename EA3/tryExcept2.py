a = 5
b = 2
try:
    c = a / b
    print(f"El resultado es: {c}")
except ZeroDivisionError:
    print("Error de división por cero.")
else:
    print("Se ingreso al TRY sin excepciones")

print("Fin de aplicación")