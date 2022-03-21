Algoritmo trianglos
	// definir variables
	Definir lado1 Como Entero
	Definir lado2 Como Entero
	Definir lado3 Como Entero
	
	// solicitar datos
	Escribir "Ingrese lado 1:"
	Leer lado1
	Escribir "Ingrese lado 2:"
	Leer lado2
	Escribir "Ingrese lado 3:"
	Leer lado3
	
	si lado1 + lado2+ lado3  = 180 Entonces
		// verificar que tipo de triangulo es
		si lado1 = lado2 y lado1 = lado3 Entonces
			Escribir "Es un triangulo equilatero"
		sino
			si lado1 = lado2 o lado1 = lado3 o lado2 = lado3 Entonces
				Escribir "Es un triangulo isoceles"
			FinSi
		FinSi
	SiNo
		Escribir "Valor excede el valor 180"
	FinSi
	
FinAlgoritmo
