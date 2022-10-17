serie = "N-02"

match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case 'N-03':
        print('Motorola')
    case _:
        print('No existe ese producto')

print('----------------------------')

cliente = {
    'nombre': 'Federico',
    'edad': 45,
    'ocupacion': 'instructor'
}
pelicula = {
    'titulo': 'Matrix',
    'ficha_tecnica': {
        'protagonista': 'Keanu Reeves',
        'director': 'Lana y Lilly Wachowski'
    }
}
elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {
            'nombre': nombre,
            'edad': edad,
            'ocupacion': ocupacion
        }:
            print('Es un cliente')
            print(f"Su nombre es {nombre} con {edad} y trabaja de {ocupacion}")
        case {
            'titulo': titulo,
            'ficha_tecnica': {
                'protagonista': protagonista,
                'director': director
            }
        }:
            print("Es una película")
            print(f"La película es {titulo} con {protagonista} y el director es {director}")
        case _:
            print("No se que es esto")

    print('----------------------------')