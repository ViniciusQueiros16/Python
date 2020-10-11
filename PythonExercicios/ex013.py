print('\033[31m=\033[m'*12, '\033[33mReajuste Salarial\033[m', '\033[31m=\033[m'*12)
sal = float(input('\033[35mQual é o salario do Funcionário? R$' ))
p = sal * 15/100
print('\033[4;32mUm funcionário que ganhava R$\033[34m{},\033[4;32m com 15% de aumento, passa a receber R$\033[34m{:.2f}.'.format(sal,(sal+p)))
