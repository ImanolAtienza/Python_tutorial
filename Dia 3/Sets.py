mi_set = set([1, 2, 3, 1, 4, 5, 5, (10, 4, 23)])
otro_set = {1, 2, 3, 100}
size = len(mi_set)

print(f"El tipo es {type(mi_set)} su tamaño es {size} y su contenido es {mi_set}. El tipo del otro es {type(otro_set)}")
print('-------------------')

print(f"Se encuentra el 2 allí {2 in mi_set}")
print('-------------------')

mi_set.add(1914)
print(f"La unión es y añadir {mi_set.union(otro_set)}")
print('-------------------')

mi_set.remove((10, 4, 23))
print(f"Se ha eliminado {mi_set}")
print('-------------------')

mi_set.discard(10000)
print(f"No ha eliminado nada, además no dio error en {mi_set}")
print('-------------------')

mi_set.pop()
print(f"Eliminado contenido aleatoriamente en {mi_set}")
print('-------------------')

mi_set.clear()
print(f"Se ha vaciado el conjunto en {mi_set}")
print('-------------------')


