print('\033[33m========\033[m', '\033[34mCalcula média aritimétrica\033[m', '\033[33m==========\033[m')
n1 = float(input('\033[4;35mPrimeira nota do aluno:\033[m '))
n2 = float(input('\033[4;35mSegunda nota do aluno: \033[m'))
m = (n1 + n2) / 2
print('\033[4;36mA média entre {:.1f} e {:.1f} é igual a {:.1f}\033[m'.format(n1, n2, m))
