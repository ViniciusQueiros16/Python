print('\033[31m<\033[m'*12, '\033[36mAntecessor e Sucessor\033[m', '\033[31m>\033[m'*12)
n = int(input('\033[4;35mDigite um numero:\033[m'))
print('\033[1;32mAnalisando o valor {}, seu antecessor é {} e o sucessor é {}\033[m'.format(n, (n-1), (n+1)))
