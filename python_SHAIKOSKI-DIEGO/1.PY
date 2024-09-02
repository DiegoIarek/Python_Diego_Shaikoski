#ordenação dos carros em ordem alfabetica

print('ordem natual ')

carros = [
   'volkswagen', 'Ferrari','Fiat' , 'Abart'
]
carros.sort()
print(carros)

print('======================================================================')

#ordenação customizada pelo numero de letras  

print('ordem customizada ')

lista_carro = ['Ferrari','Gol','Fiat','Ford','Bmw']
lista_ordenada = sorted(lista_carro, key=len)
print(lista_ordenada)

#ordenação customizada de forma que pode ser o ano ou a marca escolhido mais sempre vai ser do maior para o menor  

print('======================================================================')

print('ordem customizada ')

carro = [
    {'marca': 'Ferrari', 'ano': 2020},
    {'marca': 'Gol', 'ano': 2019},
    {'marca': 'Fiat', 'ano': 2018},
    {'marca': 'Ford', 'ano': 2017},
    {'marca': 'Bmw', 'ano': 2016}
]
carro_ordenado = sorted(carro, key=lambda x: x['marca'])
print(carro_ordenado)