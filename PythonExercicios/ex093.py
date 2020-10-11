jogos = dict()
quantgols = []
s = 0
jogos['nome'] = str(input('Nome do jogador: '))
totjogos = int(input(f'Quantas partidas {jogos["nome"]} jogou? '))
for c in range(totjogos):
    gol = int(input(f'Quantos gols na partida {c+1}? '))
    s += gol
    quantgols.append(gol)
jogos['gols'] = quantgols
jogos['total'] = s
print('-='*30)
print(jogos)
print('-='*30)
for k, v in jogos.items():
    print(f' O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogos["nome"]} jogou {totjogos} partidas.')
for cont, g in enumerate(jogos['gols']):
    print(f'   => Na partida {cont+1}, fez {g} gols.')
print(f'Foi um total de {jogos["total"]} gols.')
