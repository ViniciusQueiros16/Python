jogador = dict()
jogadores = list()
c = s = 0
while True:
    print('-'*30)
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = list()
    for cont in range(0, partidas):
        gol = int(input(f'    Quantos gols na partida {cont}? '))
        gols.append(gol)
    jogador['gols'] = gols
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Por favor, responda apenas com S ou N.')
    if resp in 'N':
        break
print('-='*30)
print('  cod nome          gols         total')
print('-'*40)
for p, j in enumerate(jogadores):
    print(f'{p:>4}  ', end='')
    for v in j.values():
        print(f'{str(v):<15}', end='')
    print()
print('-'*40)
while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if resp == 999:
        break
    if resp >= len(jogadores):
        print('ERRO! Não existe jogador com código!')
    else:
        print(f'-- Levantamento do jogador {jogadores[resp]["nome"]}')
        for i, g in enumerate(jogadores[resp]['gols']):
            print(f'No jogo {i} fez {g} gols.')
    print('-'*40)
print('<<< Volte sempre >>>')
