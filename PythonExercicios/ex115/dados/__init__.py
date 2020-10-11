def dados():
    arquivo = open('dados.txt', 'r')# le um arquivo
    lista = arquivo.readlines()
    for p in lista:
        certo = p.split(';')
        certo[1] = certo[1].replace('\n', '')
        print(f'{certo[0]:<30}{certo[1]:>3} Anos')


def adcdados(n='desconhecido', i=0):
    """Cria uma lista de pessoas e Adiciona novas pessoas ao arquivo"""
    arquivo = open('dados.txt', 'a')
    arquivo.write(f'{n};{i}\n')
    arquivo.close()
    print(f'Novo registro de {n} adicionado.')
