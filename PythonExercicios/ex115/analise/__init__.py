def analisador(resp):
    from ex115 import dados
    if resp == 1:
        print('-' * 50)
        print(f'\t\t\t\t{"PESSOAS CADASTRADAS"}')
        print('-' * 50)
        dados.dados()
    if resp == 2:
        print('-' * 50)
        print(f'\t\t\t\t{"NOVO CADASTRO"}')
        print('-' * 50)
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        dados.adcdados(nome, idade)
    if resp == 3:
        print('-' * 50)
        print(f'\t\t{"Saindo do sistema... Até logo!"}')
        print('-' * 50)
