n1 = 'Carina'
n2 = 'Jejeje-'
poema = '''Mil pequeños peces blancos
como sí hirviera
el color del agua'''

print(f"La concatenación sería {n1 + n2}")
print('-----------------')

print(f"La repetición de un string sería {n2 * 5}")
print('-----------------')

print(f"{poema}")
print('-----------------')

print(f"Existe 'hirviera' en el texto: {'hirviera' in poema}")
print('-----------------')

print(f"Existe 'sol' en el texto: {'sol' not in poema}")
print('-----------------')

print(f"El tamaño del poema: {len(poema)}")
