print('\033[33m{:=^60}'.format('\033[35m Contando vogais em Tupla \033[33m'))
palavras = ('aprender', 'programar', 'linguagem',
            'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for n in palavras:
    print(f'\n\033[33mNa palavra \033[4;35m{n.upper()}\033[m \033[33mtemos ', end='')
    if 'a' in n:
        print('\033[35ma' * n.count('a'), end=' ')
    if 'e' in n:
        print('e' * n.count('e'), end=' ')
    if 'i' in n:
        print('i' * n.count('i'), end=' ')
    if 'o' in n:
        print('\033[35mo' * n.count('o'), end=' ')
    if 'u' in n:
        print('\033[35mu' * n.count('u'))
