mi_tuple = (1, 2, 3, 4)

print(f"El tipo es {type(mi_tuple)}")
print('---------------')

indice = 0
print(f"El contenido en [{indice}] es {mi_tuple[indice]}")
print('---------------')

mi_tuple = (1, (10, 20), 3, 4)
indice = 1
print(f"El contenido en [{indice}] es {mi_tuple[indice]} y a su vez [{indice}][1] es {mi_tuple[indice][1]}")
print('---------------')

t = (1, 2, 3)
x, y, z = t
print(f"Contenido de x es {x}, y es {y}, y z es {z}")
print('---------------')

t = (1, 2, 3, 2)
size = len(t)
print(f"El tamaño de es {size}, el '2' aparece {t.count(2)} veces, por último, el número de indice es {t.index(3)}")
print('---------------')