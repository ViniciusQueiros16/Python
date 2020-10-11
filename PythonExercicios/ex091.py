from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
print('Valores Sorteados:')
for c in range(0, 4):
    jogadores[f'jogador {c+1}'] = randint(0, 10)
ranking = list()
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
#coloca em ordem os elementos #diz a posiçao dentro da chave #Reverte a ordem
print('-=-=-RANKING DOS JOGADORES-=-=-')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
