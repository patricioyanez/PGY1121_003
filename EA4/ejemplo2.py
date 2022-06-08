import numpy as num

# metodos de numpy
arreglo = num.arange(10) # 0 - 9
print(arreglo)
arreglo = num.arange(10.0) # 0. - 9.
print(arreglo)
arreglo = num.arange(4, 9) #
print(arreglo)
arreglo = num.arange(2, 11, 3) #
print(arreglo)
arreglo = num.arange(2, 11, 2) #
print(arreglo)
arreglo = num.arange(1, 11, 2) #
print(arreglo)

# cambio de valor de un arreglo
var = arreglo
var[0] = 55
print(arreglo[0]) #???
print(arreglo) #???

a = 10
b = a
b = 20
print(a)

var = arreglo.copy()
var[0] = 100
print("arreglo", arreglo)
print("var", var)