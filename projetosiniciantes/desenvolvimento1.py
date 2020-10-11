# Escolha 1 (motorista)
print(f'''De segunda a sábado {nick} roda seu táxi,
muito trabalhador', pois tinha dois filhos pequenos 
para sustentar, 'tinha saido de casa para trabalhar 
as 14:00 hrs,já cansado do dia corrido, as 20:00 hrs 
ele já estava voltando pra casa,quando então, 
uma passageira o chamou acenando para ele.''')
print('O que vc faz? continua dirigindo e passa direto[c] ou para e aceita mais uma corrida[p]?')
escolha1 = str(input('-> '))
if escolha1 == 'c':
    # Decisão c da escolaha1
    print(f'''Muito cansado,{nick} já estava no meio do trajeto para sua casa, 
    quando então ele olhou para o retrovisor e viu que um carro preto estava
    te seguindo a algum tempo...''')
    print('Você continua reto dirigindo pra casa[1] ou dobra a esquina pra tentar despistalo[2]')
    decisao = int(input('-> '))
    if decisao == '1':

