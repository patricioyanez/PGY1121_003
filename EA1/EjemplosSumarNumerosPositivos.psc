Algoritmo EjemplosSumarNumerosPositivos
	Definir numero Como Entero
	Definir indice Como Entero
	Definir total Como Entero
	
	indice = 1
	total = 0
	
	Mientras indice <= 5 Hacer
		Escribir "Ingrese un n�mero positivo"
		Leer numero
		
		si numero > 0 Entonces
			total = total + numero
			indice= indice + 1
		SiNo
			Escribir "El n�mero ingresado es negativo, vuelva a intentar."
		FinSi		
	FinMientras
	Escribir "El total es: ", total
	
FinAlgoritmo
