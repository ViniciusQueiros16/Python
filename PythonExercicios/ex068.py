print("\033[34m{:=^60}".format(' \033[36mJogo do par ou Impar\033[34m '))
from random import randint
i = 0
while True:
    pc = randint(1, 10)
    jogador = int(input('Diga um valor: '))
    pi = str(input('Voê escolhe Par ou Impar: ')).upper().strip()
    if (pc + jogador) % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'
    print('-'*40)
    print(f'\033[35mVocê jogou {jogador} e o pc jogou {pc}.Total de {pc + jogador} deu {result}')
    print('\033[34m-'*40)
    if pi == 'PAR' and result == 'PAR' or pi == 'IMPAR' and result == 'IMPAR':
        print('\033[36mVocê venceu! Vamos jogar novamente...')
        i += 1
    else:
        print('Você perdeu!')
        break
print(f'Game Over! Você venceu {i} vezes.')