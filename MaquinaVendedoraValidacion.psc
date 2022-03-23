Algoritmo MaquinaVendedoraValidacion
		// realizar la venta de 3 productos: Coca cola, Fanta y Sprite.
		//Los valores de estos son: 600, 500 y 350.
		// solicitar al usuario que producto quiere y la cantidad.
	// mostrar el total a pagar.
	// validad que la opcion sea valida y la cantidad mayor a cero
		Definir opcion Como Entero
		Definir cantidad Como Entero
		Definir total Como Entero
		
		Escribir "**** Venta de bebidas ****"
		Escribir "1.- Coca cola $600."
		Escribir "2.- Fanta     $500."
		Escribir "3.- Sprite    $350."
		Escribir "seleccione bebida:"
		Leer opcion
		
		si opcion < 1 o opcion > 3 Entonces
			Escribir "Opcion no valida"
		sino
			
			Escribir "Ingrese la cantidad a comprar"
			Leer cantidad
			
			si cantidad < 1 Entonces
				Escribir "cantidad no valida"
			sino
				si opcion = 1 Entonces
					total = 600 * cantidad
				SiNo
					si opcion = 2 Entonces
						total = 500 * cantidad
					SiNo
						total = 350 * cantidad
					FinSi
				FinSi			
				Escribir "El total a pagar es: ", total
			FinSi			
		FinSi
		
FinAlgoritmo

