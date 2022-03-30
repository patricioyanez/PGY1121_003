Algoritmo EjemploParaSumatoria //   -Determinar la sumatoria de un numero positivo
	
	Definir num Como Entero
	Definir i Como Entero
	Definir sumatoria Como Entero
	
	sumatoria = 0
	Escribir "Ingrese nro positivo"
	Leer num
	
	Si num > 0  Entonces
		Para i=1 Hasta num Hacer
			sumatoria = sumatoria + i
		FinPara
		Escribir "La sumatoria de ", num, " es: ", sumatoria
	SiNo
		Escribir "Numero no es valido"
	FinSi
FinAlgoritmo
