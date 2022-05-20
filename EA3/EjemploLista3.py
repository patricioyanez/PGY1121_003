lista1 = [1,2,3,4]
print(lista1)
# elimina el valor señalado de la lista
lista1.remove(2)
print(lista1)

# elimina el ultimo elemento de la lista y devuelve el valor eliminado
nroEliminado = lista1.pop()
print(lista1)
print("El nro eliminado es:", nroEliminado)

lista1.insert(1, 2)
lista1.append(4)
print(lista1)
nroEliminado = lista1.pop(2)
print(lista1)
print("El nro eliminado es:", nroEliminado)

