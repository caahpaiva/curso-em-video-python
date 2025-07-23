'''Crie um programa onde 4 jogadores joguem um dado e o tenham resultados aleatórios. 
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
'''


from random import randint
from time import sleep
from operator import itemgetter


jogadores = {
    'jogador1': 0,
    'jogador2': 0,
    'jogador3': 0,
    'jogador4': 0,
}

print('Valores sorteados:')
for k in jogadores.keys():
    num = randint(1,6)
    jogadores[k] = num
    sleep(1)
    print(f'O {k} tirou {num} no dado')


# ordenar = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True)) # Ordena o dicionario


ordenar = dict(sorted(jogadores.items(), key=itemgetter(1), reverse=True))

print('Ranking dos jogadores:')

posicao = 1
for k, v in ordenar.items():
    sleep(1)
    print(f'{posicao}º lugar: {k} com {v}')
    posicao +=1 