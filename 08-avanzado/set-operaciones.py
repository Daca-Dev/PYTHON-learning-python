# Unión
mi_set1 = {3, 4, 5}
mi_set2 = {5, 6, 7}
print('mi set 1:', mi_set1)
print('mi set 2:', mi_set2)

mi_set3 = mi_set1 | mi_set2
print('Unión')
print(mi_set3)

# Intersección
mi_set3 = mi_set1 & mi_set2
print('Intersección')
print(mi_set3)

# Diferencia
mi_set3 = mi_set1 - mi_set2
print('Diferencia 1 - 2')
print(mi_set3)
mi_set3 = mi_set2 - mi_set1
print('Diferencia 2 - 1')
print(mi_set3)

# Diferencia simetrica
mi_set3 = mi_set1 ^ mi_set2
print('Diferencia 1 ^ 2')
print(mi_set3)
