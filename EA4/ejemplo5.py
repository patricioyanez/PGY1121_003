import numpy as nu

matriz = nu.array([[1,2,3],[4,5,6]])
print("cantidad de dim", matriz.ndim)
print("cantidad de elem.", matriz.shape)
print("cantidad de elem.", len(matriz[0]))
print("cantidad de elem.", len(matriz[1]))

## acceder a los valores
print("valor 0,1: ", matriz[0,1])
print("valor 1,2: ", matriz[1,2])
print("valor 1,3: ", matriz[1,-1])

## calculos estadísticos
print(matriz)
print("Suma:", matriz.sum())
print("Mayor:", matriz.max())
print("Menor:", matriz.min())
print("Menor:", matriz.mean())

# porcion de una matriz
print(matriz[0])
print(matriz[0][1:2])
print(matriz[0,1:2])

matriz2 = nu.array([[1,2,3,4,5,6,7,8,9,10],[7,6,5,4,3,0,1,4,5,6]])
print("valores obtenidos:", matriz2[1,2:5:2])

