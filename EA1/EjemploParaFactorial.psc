Algoritmo EjemploParaFactorial //   -Determinar la sumatoria de un numero positivo
	
	Definir num Como Entero
	Definir i Como Entero
	Definir fact Como Entero
	
	fact = 1
	Escribir "Ingrese nro positivo"
	Leer num
	
	Si num > 2 y num < 7 Entonces
		Para i=1 Hasta num Hacer
			fact = fact * i
		FinPara
	FinSi
	Escribir "El factorial de ", num, " es: ", fact
FinAlgoritmo
