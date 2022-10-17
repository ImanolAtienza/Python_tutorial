diccionario = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'s1': 100, 's2': 200}}
cliente = {'nombre': 'Juan', 'apellido': 'Fuentes', 'peso': 88, 'talla': 1.76}
clave = 'c1'

print(f"El tipo es {type(diccionario)} y su contenido {diccionario}")
print('----------------')

print(f"El contenido de la clave [{clave}] es {diccionario[clave]}")
print('----------------')

consulta = cliente['apellido']
print(f"El contenido de la clave ['apellido'] es {consulta}")
print('----------------')

print(f"El contenido de la clave ['c2'][1] es {diccionario['c2'][1]}")
print('----------------')

print(f"El contenido de la clave ['c3']['s2] es {diccionario['c3']['s2']}")
print('----------------')

clave = 'c2'
letra = 'e'
dic = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(f"La letra en mayuscula {dic[clave][dic[clave].index(letra)].upper()}")
print('----------------')

dic['c3'] = ['g', 'h']
print(f"Las keys son {dic.keys()} y los items son {dic.items()}")
print('----------------')