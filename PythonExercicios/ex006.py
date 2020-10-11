print('\033[35m=\033[m'*12, '\033[36mTriplo e raiz quadrada\033[m', '\033[35m=\033[m'*12)
n = int(input('\033[7;30mDigite um valor:\033[m'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('\033[32mO dobro de {} é {}.'.format(n, d))
print('O triplo de {} é {}.'.format(n, t))
print(' A raiz de {} é {}.'.format(n, r))
