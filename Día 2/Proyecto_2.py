nombre = input('Cual es tú nombre: ')
ingresos = int(input('Indica los ingresos: '))
comision = round(((ingresos * 13) / 100))

print(f"\nOk {nombre}. Este mes ganaste {comision}€")