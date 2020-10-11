print('\033[33m=\033[m'*12, '\033[36mCalculando Descontos\033[m', '\033[33m=\033[m'*12)
p = float(input('\033[34mQual é o preço do produto? R$\033[m'))
f = p * 5/100
print('\033[36mO produto que custava R$\033[33m{}\033[36m, na promoção com desconto de 5% vai custar R$\033[33m{:.2f}'.format(p, (p-f)))
