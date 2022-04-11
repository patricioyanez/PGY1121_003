Algoritmo EjemploRepetirPromedio
	Definir num Como Entero
	Definir i Como Entero
	Definir prom Como real
	Definir suma Como Entero
	
	i = 1
	prom = 0
	suma = 0
	
	Repetir
		Escribir "Ingrese numero: ", i
		Leer num
		suma = suma + num
		i = i + 1
	Hasta Que i = 7
	prom = suma / 6
	Escribir prom
	prom = trunc(prom)
	Escribir "El promedio es: ", prom
FinAlgoritmo
