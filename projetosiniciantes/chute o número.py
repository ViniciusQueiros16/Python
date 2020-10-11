from random import randint
num = randint(10, 100)
while True:
    while True:
        try:
            jogador = int(input('\033[35mChute um número [999 para desistir]: '))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro por favor!\033[m')
        else:
            break
    if jogador == num:
        print('\033[1;36mPARABÉNS VOCÊ ACERTOU!!!\033[m')
        break
    elif jogador == 999:
        print('\033[1;34mhahaha, Acontece!')
        break
    elif jogador < num:
        valor = num - jogador
        print('\033[34mValor baixo!')
        if 5 < valor <= 10:
            print('\033[33mTa ficando quente!')
        elif valor < 5:
            print('\033[32mTA QUENTE!')
    elif jogador > num:
        valor = jogador - num
        print('\033[34mValor alto!')
        if 5 < valor <= 10:
            print('\033[33mTa ficando quente!')
        elif valor < 5:
            print('\033[32mTA QUENTE!')
