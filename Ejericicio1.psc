Algoritmo Ejericicio1
	// definir variables
	Definir sueldoTrabajador1 Como Entero
	Definir sueldoTrabajador2 Como Entero
	Definir sueldoTrabajador3 Como Entero
	
	// solicitar sueldos al usuario
	Escribir "Ingrese 1er sueldo: "
	Leer sueldoTrabajador1
	Escribir "Ingrese 2do sueldo: "
	Leer sueldoTrabajador2
	Escribir "Ingrese 3er sueldo: "
	Leer sueldoTrabajador3
	
	si sueldoTrabajador1 > sueldoTrabajador2 Entonces
		si sueldoTrabajador1 > sueldoTrabajador3 Entonces
			Escribir "El trabajor 1 gana más"
		SiNo
			Escribir "El trabajor 3 gana más"
		FinSi
	sino	
		si sueldoTrabajador2 > sueldoTrabajador3 Entonces
			Escribir "El trabajor 2 gana más"
		SiNo
			Escribir "El trabajor 3 gana más"
		FinSi
	FinSi
	
	
	
FinAlgoritmo
