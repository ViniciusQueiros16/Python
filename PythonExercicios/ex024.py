print('\033[33m='*12, '\033[1;32mVerificando as primeiras letras de um texto', '\033[33m='*12)
cidade = str(input('Em que cidade vc nasceu? '))
print('SANTO' in cidade.upper().split())
