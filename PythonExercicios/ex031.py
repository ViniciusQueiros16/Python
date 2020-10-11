print('='*12, 'Custo da Viagem', '='*12)
distancia = float(input('Qual é a distância da viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia}Km')
if distancia <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(distancia * 0.50))
else:
    print(f'E o preço da sua viagem será de {distancia*0.45:.2f}')
