from random import choice

exito = False
intentos = 6
palabras = ['salchicha', 'lolo', 'perrito']
palabra_juego = ''
lista_incorrectas = []
lista_correctas = []


def comprobar_en_palabra(palabra, char):
    return char in palabra


def crear_ahorcado(palabra):
    nueva_palabra = ''

    for char in palabra:
        nueva_palabra = f"{nueva_palabra}-"

    return nueva_palabra


def modificar_ahorcado(palabra):
    return_palabra = []

    for c in palabra:
        if c in lista_correctas:
            return_palabra.append(c)
        else:
            return_palabra.append('-')

    return return_palabra


def juego_terminado(palabra):
    return '-' not in palabra


print('Vamos a comenzar con el juego del ahorcado...')
palabra_juego = choice(palabras)
ahorcado = crear_ahorcado(palabra_juego)

while intentos > 0:
    print(f"La palabra actual está así... {ahorcado}")
    caracter = input('Introduce un caracter: ')
    if comprobar_en_palabra(palabra_juego, caracter):
        if caracter in lista_correctas:
            print(f'Ya introdujiste ese caracter correcto antes')
        else:
            print('Caracter encontrado')

            lista_correctas.append(caracter)
            ahorcado = modificar_ahorcado(palabra_juego)

            if juego_terminado(ahorcado):
                exito = True
                break
    else:
        print('El caracter introducido no está en la palabra')
        lista_incorrectas.append(caracter)
        print(f"Está es la lista de caracteres incorrectos: {lista_incorrectas}")
        intentos -= 1

    print('-------------------------------')

if exito:
    print('Juego terminado con exito!')
else:
    print('Vuelve a intentarlo')