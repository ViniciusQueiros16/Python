print(f'\033[31m{" Listagem de Preços ":=^60}')
listagem = ('Lápis', 1.75, 'Borracha', 2.00,
            'Caderno', 15.90, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
cont = 0
for pos in range(len(listagem)):
    if pos % 2 == 0:
        print(f'\033[36m{listagem[pos]:.<30}', end='\033[32mR$')
    elif pos % 2 == 1:
        print(f'{listagem[pos]:.2f}')
