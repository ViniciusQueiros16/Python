print('\033[35m='*12, '\033[36msorteando uma ordem na lista', '\033[35m='*12)
import random
al1 = input('\033[4;1;35;46mprimeiro aluno:\033[m ')
al2 = input('\033[4;1;35;46msegundo aluno:\033[m ')
al3 = input('\033[4;1;35;46mterceiro aluno:\033[m ')
al4 = input('\033[4;1;35;46mquarto aluno:\033[m ')
lista = [al1, al2, al3, al4]
embaralhar = random.shuffle(lista)
print('\033[4;31mA ordem de apresentaçao será:\033[m')
print(f'\033[35m{lista}')
