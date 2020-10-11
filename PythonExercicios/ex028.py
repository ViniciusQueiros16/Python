print('='*12, 'Jogo da Adivinhação', '='*12)
import random
from time import sleep
import emoji
lista = [0, 1, 2, 3, 4, 5]
n = random.choice(lista)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5.Tente adivinhar...')
print('-=-'*20)
a = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
print(f'Eu pensei em {n}')
if a == n:
    print(emoji.emojize('Parabéns vc venceu!!:wink:', use_aliases=True))
else:
    print(emoji.emojize('Você perdeu!!:disappointed:', use_aliases=True))
