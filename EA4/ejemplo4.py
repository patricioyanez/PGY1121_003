import numpy as nu
# compación de arreglos
a1 = nu.array([1,2,3,4])
a2 = nu.array([1,2,3,4])
a3 = nu.array([6,2,3,9])

print("Igual:", a1 == a2)
print("Igual:", a1 == a3)
print("Mayores:", a1 > a3)
print("Menores:", a1 < a3)
print("Distintos:", a1 != a3)

# metodos para estadísticas
print(a1)
print("Suma:", a1.sum())
print("Mayor:", a1.max())
print("Menor:", a1.min())
print("Menor:", a1.mean())
print("Suma:", sum(a1))
print("Mayor:", max(a1))
print("Menor:", min(a1))
