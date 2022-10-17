# from random import randint
from random import *

aleatorio = randint(1, 50)
print(f"El número aleatorio entero es: {aleatorio}")

aleatorio = uniform(1, 50)
print(f"El número aleatorio decimal es: {aleatorio}")

aleatorio = random()
print(f"El número aleatorio entre 0:1 es: {aleatorio}")

colores = ['azul', 'verde', 'rojo']
aleatorio = choice(colores)
print(f"El color escogido es: {aleatorio}")

numeros = list(range(5, 50, 5))
shuffle(numeros)
print(f"Los números barajeados son: {numeros}")
