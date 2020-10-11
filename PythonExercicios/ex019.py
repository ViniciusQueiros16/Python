print('\033[31m='*12, '\033[33mSorteando um item na lista', '\033[31m='*12)
import random
p = input('\033[4;1;44mPrimeiro aluno:')
s = input('Segundo aluno: ')
t = input('Terceiro aluno:')
q = input('Quarto aluno:\033[m ')
lista = [p, s, t, q]
escolhido = random.choice(lista)
print(f'\033[4;31mO aluno escolhido foi {escolhido}.')
