def chequear_3_cifras(numero):
    return (numero in range(100, 1000))

def chequear_3_lista(lista):
    for n in lista:
        if n in range(100, 1000):
            return True
    set
    return False

def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    print(len(lista))
    return lista

print(f"El número tiene 3 cifras? {chequear_3_cifras(123)}")
print('---------------')
print(f"La lista tiene un número de 3 cifras? {chequear_3_lista([1, 12, 11111, 111, 1231231231])}")