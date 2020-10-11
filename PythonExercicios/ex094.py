galera = dict()
lista = list()
s = 0
while True:
    galera['nome'] = str(input('Nome: '))
    while True:
        galera['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if galera['sexo'] in 'MF':
            break
        print('Erro! Por favor digite apenas M ou F.')
    galera['idade'] = int(input('Idade: '))
    s += galera['idade']
    lista.append(galera.copy())
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    while True:
        if resp != 'S' and resp != 'N':
            print('Resposta Incorreta! Responda com S ou N.')
            resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        else:
            break
    if resp in 'N':
        break
media = s / len(lista)
print('-='*30)
print(f'- O grupo tem {len(lista)} pessoas.')
print(f'- A média de idade é de {media:5.2f} anos.')
print('- As mulheres cadastradas foram: ', end=' ')
for p in lista:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('- Lista das pessoas que estão acima da média:')
for c in lista:
    if c['idade'] >= media:
        print('   ', end='')
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')
