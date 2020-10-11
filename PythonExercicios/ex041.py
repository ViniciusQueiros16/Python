from datetime import date
print('\033[36m='*12, '\033[31mClassificando Atletas', '\033[36m='*12)
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')
