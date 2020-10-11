print("\033[32m{:=^60}".format('\033[35mEstatistica de produto\033[32m'))
print('\033[34m-'*40)
print("{:^40}".format('\033[31mLOJAS QUEIRÓS'))
print('\033[34m-'*40)
c = menor = maisdemil = total = 0
while True:
    produto = str(input('Nome do Produto: '))
    valor = float(input('Preço do produto: R$'))
    c += 1
    total += valor
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if valor > 1000:
        maisdemil += 1
    if c == 1:# Se for o primeiro
        menor = valor # Ele passa a ser o menor valor
        mvp = produto
    else:# se não for o primeiro
        if valor < menor: # ele  tem q verifica se o valor é menor q o menor acima
            menor = valor # ai entao ele passa a ser o menor preço
            mvp = produto # mvp é pra o menor valor receber o nome do produto
    if continua == 'N':
        print("{:-^40}".format(' FIM DO PROGRAMA '))
        break
print(f'\033[35mO total da compra foi R${total:.2f}')
print(f'Temos {maisdemil} produtos custando mais de R$1000.00 ')
print(f'O produto mais barato foi {mvp} que custa R${menor:.2f}')
