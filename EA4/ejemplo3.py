import numpy as num
arreglo = num.array([1,2,3,4])
print(arreglo)
arreglo = arreglo + 1
print(arreglo)
arreglo += 1
print(arreglo)
arreglo -= 1
print(arreglo)
arreglo **= 2
print(arreglo)
arreglo **= 3
print(arreglo)

arreglo1 = num.ones(10)
print(arreglo1)
arreglo1 += 4
print(arreglo1)


arreglo2 = num.ones(10)

print("Suma: ", arreglo1 + arreglo2 )
print("Resta: ", arreglo1 - arreglo2 )

arreglo2 +=1

print("Resta: ", arreglo1 * arreglo2 )
print("Resta: ", arreglo1 ** arreglo2 )