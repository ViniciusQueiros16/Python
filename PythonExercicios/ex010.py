import emoji
print('\033[33m=\033[m'*12,'\033[34mConversor de Moedas\033[m','\033[33m=\033[m'*12)
n = float(input('\033[1;31;43mQuanto dinheiro vc tem na carteira? R$\033[m'))
print('\033[32mCom R$\033[35m{}\033[m \033[32mvocê pode comprar US$\033[35m{:.2f}\033[m \033[32mou £\033[35m{:.2f}\033[35m'.format(n,(n/5.31), (n/5.77)))