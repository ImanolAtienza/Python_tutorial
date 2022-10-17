from random import randint

nombre = input('Introduce tú nombre: ')
numero = randint(1, 100)
num_input = 0
exito = False

print(f"De acuerdo {nombre}, empecemos el juego!")
print('He pensado un núnero del 1 al 100...trata de adivinarlo en 8 intentos!')
print('-----------------------------')

for intento in range(1, 9):
    num_input = int(input('Introduce un número para ver sí lo conseguiste adivinar: '))

    if (num_input < 1) or (num_input > 100):
        print(f"Has introducido un número no permitido, {num_input}")
    elif num_input < numero:
        print(f"Incorrecto! Escogiste un número menor, {num_input}")
    elif num_input > numero:
        print(f"Incorrecto! Escogiste un número mayor, {num_input}")
    else:
        print(f"Ganaste! En el {intento} intento")
        exito = True
        break

    print(f"Vas por el intento {intento}, te quedan {8 - intento}")
    print('-----------------------------')

if not exito:
    print('No lo conseguiste, vuelve a intentarlo')