lista = [letra for letra in 'python']
print(f"La lista de caracteres es: {lista}")

lista = [numero if (numero * 2) > 10 else 'no' for numero in range(0, 21, 2)]
print(f"La lista de números es: {lista}")

pies = [10, 20, 30, 40, 50]
metros = [(pie * 3.281) for pie in pies]
comprimido = list(zip(pies, metros))
print(f"La conversión es: {comprimido}")