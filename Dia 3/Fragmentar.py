texto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

fragmento = texto[2]
print(f"El primer fragmento es {fragmento}")

fragmento = texto[2:5]
print(f"El segundo fragmento es {fragmento}")

fragmento = texto[2:]
print(f"El siguiente fragmento es {fragmento}")

fragmento = texto[:2]
print(f"El siguiente fragmento es {fragmento}")

fragmento = texto[2:10:2]
print(f"El ultimo fragmento es {fragmento}")

fragmento = texto[::-1]
print(f"El inverso fragmento es {fragmento}")