def tipo(**kwargs):
    print(type(kwargs))

def suma(num1, num2, *args, **kwargs):
    total = 0
    print(kwargs.items())
    print(f"El primer valor es: {num1}")
    print(f"El segundo valor es: {num2}")

    for argumento in args:
        print(f"El argumento que tengo ahora es: {argumento}")

    for clave, valor in kwargs.items():
        print(f"kwargs[{clave}] = {valor}")
        total += valor

    return total

tipo(x=3, y=1, v=0)
print('----------')
print(f"El valor total es: {suma(1, 2, [1, 2, 3, 4, 5, 6], {'x' : 3, 'y' : 1, 'v' : 0})}")