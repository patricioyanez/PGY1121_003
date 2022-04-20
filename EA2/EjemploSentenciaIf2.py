nota1 = input("Ingrese nota 1: ")
nota2 = input("Ingrese nota 2: ")
nota3 = input("Ingrese nota 3: ")

# convertir a numero decimal (float)

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)

if nota1 < 1 or nota1 > 7:
    print("Nota 1 no esta dentro del rango de notas")
elif nota2 < 1 or nota2 > 7:
    print("Nota 2 no esta dentro del rango de notas")
elif nota3 < 1 or nota3 > 7:
    print("Nota 3 no esta dentro del rango de notas")
else: # las notas son válidas
    promedio = (nota1 + nota2 + nota3) / 3
    print("Su promedio es:", "{:0.1f}".format(promedio))

    if promedio < 4:
        print("Reprobó, no vimo el otro semestre")
    else:
        print("Aprobó")

print("***** programa cerrado")