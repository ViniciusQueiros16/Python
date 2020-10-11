from random import randint
from time import sleep
def sorteia(num):
    for s in range(0, 5):
        numero.append(randint(0, 10))
    print('Sorteando 5 valores da lista: ', end='')
    for n in numero:
        print(n, end=' ')
        sleep(0.5)
    print(' Pronto!')
def somapar():
    soma = 0
    for p in numero:
        if p % 2 == 0:
            soma += p
    print(f'Somando os valores pares de {numero}, temos {soma}')


numero = list()
sorteia(numero)
somapar()
