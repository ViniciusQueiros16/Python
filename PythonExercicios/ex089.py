print('{:=^60}'.format(' Boletim com listas compostas '))
todos = list()
c = 0
s = 0
while True:
    aluno = str(input('Nome: '))
    c += 1
    todos.append([aluno])
    notas = []
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    media = (notas[0] + notas[1]) / 2

    todos[c-1].append(notas)
    todos[c-1].append(media)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print('No    NOME    MÉDIA')
print('-'*20)
for p, c in enumerate(todos):
    print(f'{p:^2} {c[0]:^10} {c[2]:^6.1f}')
print('-'*20)
print('-='*30)
while True:
    print('-' * 30)
    mostra = int(input('Mostra notas de qual aluno? (999 interrompe): '))
    if mostra == 999:
        break
    if mostra <= len(todos) - 1:
        print(f'Notas de {todos[mostra][0]} são {todos[mostra][1]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE! >>>')
