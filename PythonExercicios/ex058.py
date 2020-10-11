print("\033[34m{:=^60}".format('\033[36m Jogo da Adivinhação v2.0 \033[34m'))
from random import randint
print('\033[31m-*'*22)
print('''\033[34mOlá! Eu me chamo Paulo Cesar (PC) 
Acabei de pensar em um número entre 0 e 10
Será que vc consegui advinhar qual é?''')
print('\033[31m-*'*22)
pc = randint(0, 10)
tenta = int(input('\033[36mVamos lá. Tente Advinhar: '))
jogador = 1
i = 0
if tenta != pc:
    while jogador != pc:
        if jogador < pc:
            jogador = int(input('\033[34mMais... Tente novamente: '))
        else:
            jogador = int(input('\033[34mMenos... Tente novamente: '))
        i += 1
print(f'\033[36mParabéns você acertou! Você precisou de {i+1} tentativas.')
