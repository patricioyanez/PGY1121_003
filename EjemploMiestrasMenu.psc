Algoritmo EjemploMiestrasMenu
	Definir opcion Como Entero
	
	opcion = 0
	
	Mientras opcion <> 5 Hacer
		Limpiar Pantalla
		Escribir "*********  Opciones del sistema ***********"
		Escribir "1.- Saludar"
		Escribir "2.- Despedirse"		
		Escribir "3.- Men� 3"
		Escribir "4.- Men� 4"
		Escribir "5.- Salir"
		Escribir "Ingrese opcion:"
		Leer opcion
		
		si opcion = 1 Entonces
			Escribir "Hola usuario :)"	
			Escribir "Presione cualquier tecla para volver al men�"
			Esperar Tecla
		FinSi
		si opcion = 2 Entonces
			Escribir "Nos vimos! (Karen Rojo)"
			Escribir "Presione cualquier tecla para volver al men�"
			Esperar Tecla
		FinSi
	FinMientras
	Escribir "Sistema cerrado"
FinAlgoritmo
