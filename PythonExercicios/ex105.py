def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param num: uma ou mais notas de vários alunos.
    :param sit: valor opcional, indicando se deve ou não adicionar a sítuação da turma.
    :return: dicionário com várias informações sobre a sítuação da turma.
    """
    num = list()
    while True:
        nots = float(input('Digite uma nota: [999 para parar] '))
        if nots != 999:
            num.append(nots)
        if nots == 999:
            break
    situação = str(input('Quer ver a situação dos alunos? [S/N] ')).upper()[0]
    if situação == 'S':
        sit = True
    dados = dict()
    dados['total'] = len(num)
    dados['maior'] = max(num)
    dados['menor'] = min(num)
    dados['média'] = sum(num) / len(num)
    if sit:
        if dados['média'] >= 7:
            dados['sit'] = 'BOA'
        elif 5 <= dados['média'] < 7:
            dados['sit'] = 'RAZOÁVEL'
        elif dados['média'] < 5:
            dados['sit'] = 'RUIM'
    print('-=' * 30)
    return dados


print(notas())
