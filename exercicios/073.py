'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro
de Futebol, na ordem de colcoação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os ultimos 4 colocados da tabela.
c) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Mirassol.
'''



times = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Bahia', 'Fluminense', 'Atlético-MG',
         'Botafogo', 'Mirassol', 'Corinthians', 'Grêmio', 'Ceará', 'Vasco', 'São Paulo',
         'Santos', 'Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport')


print('=-'*30)
print(f'Lista de times do Brasileirão: {times}')
print('=-'*30)
print(f'Os 5 primeiros são:{times[0:5]}')
print('=-'*30)
print(f'Os 4 últimos são:{times[-4:]}')
print('=-'*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-'*30)
print(f'O Mirassol está na posição {times.index('Mirassol')+1}')


