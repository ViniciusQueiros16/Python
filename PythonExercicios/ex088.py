print('{:=^60}'.format(' Palpites para a Mega Sena '))
import time
from random import randint
vezes = int(input('Quantos jogos você quer que eu sorteie? '))
todos = []
for c in range(vezes):
    jogo = []
    todos.append(jogo)
    while True:
        ale = randint(1, 60)
        if ale not in jogo:
            jogo.append(ale)
            if len(jogo) == 6:
                break
    jogo.sort()
print(f'-=-=-= Sorteando {len(todos)} Jogos -=-=-=')
for p, c in enumerate(todos):
    print(f'Jogo {p+1}: {c}')
    time.sleep(0.75)
print('-=-=-=-= < BOA SORTE! > =-=-=-=-')
