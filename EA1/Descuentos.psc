Algoritmo Descuento
	Definir totalCompra Como Entero
	Definir totalAPagar como Real
	
	Escribir "Ingrese el total de la compra"
	Leer totalCompra
	
	si totalCompra < 100 Entonces
		Escribir "Total a pagar es:", totalCompra
		Escribir "Ud no tiene descuento :("
	sino	
		si totalCompra >= 500 Entonces
			totalAPagar = totalCompra * .7
			Escribir "Su descuento es: 30"
		SiNo
			si totalCompra < 500 y totalCompra >= 200 Entonces
				totalAPagar = totalCompra * .8
				Escribir "Su descuento es: 20"
			SiNo
				totalAPagar = totalCompra * .9
				Escribir "Su descuento es: 10"
			FinSi
		FinSi
		Escribir "El total a pagar es:", totalAPagar
	FinSi
	
	
FinAlgoritmo
