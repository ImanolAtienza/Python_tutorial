from random import shuffle

# Lista inicial
palitos = ['-', '--', '---', '----']

# Mezclar palitos
def mezclar(lista):
    shuffle(palitos)
    return lista

# Pedirle intento
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un número del 1 al 4: ')

    return int(intento)

# Comprobar intento
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print('A lavar los platos!')
    else:
        print('Esta vez te has salvado')

    print(f"Te toco {lista[intento - 1]}")

print('Vamos a mezclar los palitos')
palitos_mezclados = mezclar(palitos)

print('----------------------')
print('Vamos a escoger un palito...')
intento_obtenido = probar_suerte()

print('----------------------')
chequear_intento(palitos_mezclados, intento_obtenido)