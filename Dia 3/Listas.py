mi_lista = ['a', 'b', 'c']
size = len(mi_lista)
indice = 0

print(f"Tipo de dato de lista es {type(mi_lista)} y tiene un tamaño de {size}")
print('-------------------')

resultado = mi_lista[indice]
print(f"Mostrando el indice [{indice}] es {resultado}")
print('-------------------')

mi_lista2 = mi_lista + ['d', 'e', 'f']
print(f"Concatenando listas {mi_lista2}")
print('-------------------')

mi_lista2[0:size] = 'alf'
mi_lista2.append('g')
print(f"Alterando y agregando elementos de la lista {mi_lista2}")
print('-------------------')

mi_lista2.pop()
mi_lista2.pop(mi_lista2.index('l'))
print(f"Remover elementos ['g', 'l'] de la lista {mi_lista2}")
print('-------------------')

mi_lista2 = mi_lista + ['x', 'h', '2', 't']
mi_lista2.sort()
print(f"Ordenar la lista {mi_lista2}")
print('-------------------')

mi_lista2.reverse()
print(f"Invertir la lista {mi_lista2}")
print('-------------------')