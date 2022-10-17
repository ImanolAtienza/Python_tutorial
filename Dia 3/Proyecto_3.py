texto = ''
lista_letras = []

texto = input("Introduce un texto: ")
lista_letras.append(input("Introduce una letra: ").lower())
lista_letras.append(input("Introduce otra letra: ").lower())
lista_letras.append(input("Introduce la última letra: ").lower())

print(f"El texto es {texto} y las letras son {lista_letras}")

for letra in lista_letras:
    print(f"La letra [{letra}] aparece {texto.count(letra)} veces")

palabras = texto.split()
num_palabras = len(palabras)
print(f"El número total de palabras es {num_palabras}")

primera_letra = texto[0]
ultima_letra = texto[-1]

print(f"La primera letra es {primera_letra} y la última es {ultima_letra}")

palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"El texto en orden inversion es '{texto_invertido}'")

print(f"¿Está la palabra 'Python' en el texto? {'Python' in texto}")