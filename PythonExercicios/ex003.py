print('\033[34m=\033[m'*12, '\033[31mSomando dois números\033[m', '\033[34m=\033[m'*12)
n1 = int(input("\033[7;30mDigite um valor:"))
n2 = int(input("Digite outro:\033[m"))
s = n1 + n2
print('\033[35mA soma entre {} e {}, é igual á {}\033[m'.format(n1, n2, s))
