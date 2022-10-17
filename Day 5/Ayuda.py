dic = {
    'clave1': 100,
    'clave2': 500
}
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

item_tuple = dic.popitem()

print(f"Vamos a mostrar que extrajo: {item_tuple} y el contenido: {dic}")

tex = texto.lstrip(',:%_#')
print(tex)