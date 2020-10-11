def leiaint():
    from ex115 import menu
    from ex115 import analise
    menu.menu()
    while True:
        try:
            while True:
                valor = int(input('\033[32mSua opção: \033[m'))
                if valor > 3 or valor < 1:
                    print('\033[31mERRO! Digite uma opção válida!\033[m')
                    menu.menu()
                else:
                    break
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número inteiro válido.\033[m')
        else:
            analise.analisador(valor)
            if valor != 3:
                menu.menu()
            if valor == 3:
                break
