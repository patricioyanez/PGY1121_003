Algoritmo EjercicioTablaMultiplicar
	//1- crear variables
	Definir numero Como Entero

	
	// pedir datos
	Escribir "Ingrese nro positivo"
	Leer numero
	
	si numero < 1 Entonces
		Escribir "El numero es negativo"
	SiNo
		para num = 1 Hasta 10 Hacer
			Escribir num, " x ", numero, " = ", num * numero
		FinPara
	FinSi
	
	
	
FinAlgoritmo
