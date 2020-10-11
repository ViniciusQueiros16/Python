print('\033[36m{:=^40}'.format('\033[33mLojas Queirós\033[m\033[36m'))
produto = float(input('\033[34mValor do produto: '))
cheque = produto - (10/100 * produto)
avistac = produto - (5/100 * produto)
tres = produto + (20/100 * produto)
print('\033[35mVocê tem a opção de pagar: \n\033[4;36mÀ vista com dinheiro ou cheque = 10% de desconto\nÀ vista no cartão = 5% de desconto\nEm até 2x no cartão = o mesmo preço\n3x ou mais no cartão = 20% de juros')
condição = str(input('\033[35mComo deseja pagar?\033[m \033[33m')).upper()
if condição in 'A VISTA COM DINHEIRO OU CHEQUE,À VISTA COM DINHEIRO OU CHEQUE':
    print(f'O valor é de R${cheque}')
elif condição in 'Á VISTA NO CARTÃO, A VISTA NO CARTAO':
    print(f'O valor é de R${avistac}')
elif condição in '2X NO CARTAO':
    print('O valor é o mesmo')
else:
    print(f'O valor é de R${tres}')
