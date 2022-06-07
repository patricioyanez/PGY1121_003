# numpy se debe descargar desde pipy
# usar el comando: pip install numpy
import numpy 
arreglo = numpy.array([0,1,2,3,4,5,6,7,8,9,10])
print(arreglo)

print("Cantidad de dimensiones: ", arreglo.ndim)
print("Cantidad de elementos  : ", arreglo.shape)
# devuelve los valores que estan dentro del rango del indice
# 1 al 5 - 1, o sea hasta el 4
print("Elementos seleccionados: ", arreglo[1:5])
# devuelve los valores que estan dentro del rango del indice
# 1 al 9 - 1, o sea hasta el 8, PERO, solo los valores de los
# indices que aumentan de 3, osea 1,4,5
print("Elementos seleccionados: ", arreglo[1:9:3])
# toma todo el arreglo pero solo muestra los indices
# que coincidan con la sumatoria del tres, incluye el cero
# ejemplo de indice: 0, 3, 6, 9
print("Elementos seleccionados: ", arreglo[::3])

print("Elementos seleccionados: ", arreglo[3::2])

print("El ultimo elemento es:", arreglo[-1])
print("El penultimo elemento es:", arreglo[-2])
