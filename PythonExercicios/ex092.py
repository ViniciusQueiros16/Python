from datetime import date
info = dict()
info['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
info['idade'] = date.today().year - ano
info['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if info['ctps'] > 0:
    info['contratação'] = int(input('Ano de contratação: '))
    info['Salário'] = float(input('Salário: R$ '))
    anostrabalho = date.today().year - info['contratação']
    info['aposentadoria'] = 35 - anostrabalho + info['idade']
print('-='*30)
for k, v in info.items():
    print(f'- {k} tem o valor {v}')
