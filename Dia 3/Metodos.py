texto = 'Este es el texto de Imanol'
resultado = ''

print(texto)
print('-----------------------')
resultado = texto[0:3].upper()
print(resultado)
print('-----------------------')

resultado = texto.lower()
print(resultado)
print('-----------------------')

resultado = texto.split(' ')
print(resultado)
print('-----------------------')

a = 'Aprender'
b = 'Python'
c = 'es'
d = 'genial'
e = ' '.join([a, b, c, d])
print(e)
print('-----------------------')

resultado = texto.find('es')
print(resultado)
print('-----------------------')

resultado = texto.replace('es', 'no es')
print(resultado)
print('-----------------------')