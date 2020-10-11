def ficha(nome='', gols=''):
    if len(r1) == 0:
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


r1 = str(input('Nome do jogador: '))
r2 = str(input('Número de Gols: ')).strip()
print(ficha(r1, r2))
