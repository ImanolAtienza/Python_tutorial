mi_texto = 'Esta es una prueba'
resultado = ''
indice = 0
indice_empezar = 5
indice_hasta_buscar = 13

print(f"En el indice [{indice}] es {mi_texto[indice]}")

resultado = mi_texto.index('a')
print(f"He encontrado la primera 'a' en {resultado}")

resultado = mi_texto.index('a', indice_empezar, indice_hasta_buscar)
print(f"He encontrado la siguiente 'a' entre [{indice_empezar}] y [{indice_hasta_buscar}] en {resultado}")

resultado = mi_texto.index('es')
print(f"He encontrado la primera 'es' en {resultado}")

resultado = mi_texto.rindex(('prueba'))
print(f"He encontrado la ultima 'prueba' en {resultado}")