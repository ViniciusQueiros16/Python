from random import choice
respostas = ['Sim!', 'Claro', 'Obvio que sim', 'Logico que sim', 'Concerteza',
             'Não', 'de maneira alguma', 'acho que não', 'Infelizmente não', 'eu seila porra']
escolha = choice(respostas)
usuario = str(input('Faça alguma pergunta: '))
print(escolha)
