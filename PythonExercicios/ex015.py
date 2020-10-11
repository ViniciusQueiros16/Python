print('\033[31m=\033[m'*12, '\033[36mAluguel de carros\033[m', '\033[31m=\033[m'*12)
#Calcular a quantidade de km pecorridos por um carro alugado
# e a quantidades de dias pelos quias el foi alugado, sabendo
# que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
dias = int(input('\033[35mQuantos dias o carro foi alugado?\033[35m'))
km = float(input('\033[35mQuantos Km rodados?\033[m'))
total = 60 * dias + 0.15 * km
print('\033[4;36mO total a pagar é de\033[31m R${}.'.format(total))
