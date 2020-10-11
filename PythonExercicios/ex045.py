from time import sleep
import random
print('\033[036m{:=^60}'.format ('\033[032mPedra, Papel e Tesoura\033[036m'))
print('''\033[36mSuas opções:\033[32m
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
escolha = int(input('\033[36mQual vc escolhe? \033[32m'))
if escolha == 1:
    jo = 'Pedra'
elif escolha == 2:
    jo = 'Papel'
elif escolha == 3:
    jo = 'Tesoura'
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('\033[31m-='*13)
lista = 'Pedra Papel Tesoura'.split()
pc = random.choice(lista)
print(f'\033[34mComputador escolheu {pc}')
print(f'Jogador escolheu {jo}')
print('\033[31m-=\033[36m'*13)
if pc == 'Pedra' and jo == 'Tesoura' or pc == 'Papel' and jo == 'Pedra' or pc == 'Tesoura' and jo == 'Papel':
    print('computador vence!!!')
elif pc == 'Tesoura' and jo == 'Pedra' or pc == 'Pedra' and jo == 'Papel' or pc == 'Papel' and jo == 'Tesoura':
    print('Jogador vence!!!')
else:
    print('Deu empate!')
