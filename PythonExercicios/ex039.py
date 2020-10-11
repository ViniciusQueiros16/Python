print('\033[36m='*12, '\033[32mAlistamento Militar', '\033[36m='*12)
from datetime import date
ano = int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual - ano
print(f'Você tem \033[32m{idade} \033[36manos em \033[32m{atual}.')
if idade == 18:
    print('\033[36mTa na hora de se alistar.')
elif idade < 18:
    print(f'\033[36mAinda falta(m) \033[32m{18 - idade} \033[36mano(s) para se alistar \nSeu alistamento será em \033[32m{ano+18}.')
elif idade > 18:
    print(f'\033[31mVocê deveria ter se alistado há \033[32m{idade - 18} \033[31manos atrás.\n\033[36mSeu alistamento foi em \033[32m{ano+18}.')
