carro = [
    {'marca': 'Ferrari', 'ano': 2020},
    {'marca': 'Gol', 'ano': 2019},
    {'marca': 'Bmw', 'ano': 2016},
    {'marca': 'Fiat', 'ano': 2018},
    {'marca': 'Ford', 'ano': 2017}
    
]

def ordenar_carros(carro, chave):
    return sorted(carro, key=lambda x: x[chave], reverse=True)

carro_ordenado_ano = ordenar_carros(carro, 'ano')

print("Carros ordenados por ano:")
for item in carro_ordenado_ano:
    print(f"Marca: {item['marca']}, Ano: {item['ano']}")
