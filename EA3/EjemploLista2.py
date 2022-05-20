lista1 = [1,2,3]
lista1.append(4)
print(lista1)
lista2 = [5,6,7]

lista1.extend(lista2)
print(lista1)
# agrega una lista
lista1.append(lista2)
# acceder a elemento dentro de una lista
print(lista1[7][1])
lista3 = [8,9,10,11,12]
# similar al extend
lista1 += lista3
print(lista1)
# agrega un nuevo valor según el indice señalado
lista1.insert(2,5000)
print(lista1)
