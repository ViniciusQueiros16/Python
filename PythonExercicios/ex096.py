def area(larg=float(input('LARGURA (m): ')), compr=float(input('COMPRIMENTO (m): '))):
    tot = larg * compr
    print(f'A área de um terreno {larg} x {compr} è de {tot}m²')


print('-'*30)
print('  Controle de Terrenos')
print('-'*30)
area()
