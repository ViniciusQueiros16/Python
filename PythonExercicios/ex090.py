print('{:=^60}'.format(' Dicionário em Python '))
alunos = dict()
alunos['nome'] = str(input('Nome: '))
alunos['média'] = float(input(f'Média de {alunos["nome"]}: '))
if alunos['média'] >= 7:
    alunos['situação'] = 'Aprovado'
elif 5 < alunos['média'] < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'
print('-='*30)
print(f'- Nome é igual a {alunos["nome"]}')
print(f'- Média é igual a {alunos["média"]}')
print(f'- Situação é igual a {alunos["situação"]}')
