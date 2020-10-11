print("\033[31m{:=^60}".format('\033[32m Validando expressões matemáticas \033[31m'))
lista = []
expre = str(input('\033[34mdigite a expressão: '))
for cont, pa in enumerate(expre):
    if pa == '(':
        lista.append('(')
    elif pa == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('\033[32mExpressão correta')
else:
    print('\033[31mExpressão incorreta')
