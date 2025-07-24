'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade 
de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, 
incluindo o total de gols feitos durante o campeonato.
'''

campeonato = {}
gols = []
total = 0

campeonato['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {campeonato["nome"]} jogou? '))

for i in range(0,partidas):
    gol  = int(input(f'Quantos gols na partida {i}? '))
    gols.append(gol)
    total += gol
    

campeonato['gols'] = gols[:]
# campeonato['total'] = sum(gols)
campeonato['total'] = total

print('-='*30)
print(campeonato)
print('-='*30)

for k, v in campeonato.items():
    print(f'O campo {k} tem o valor {v}')

print('-='*30)
print(f'O jogador {campeonato["nome"]} jogou {len(campeonato["gols"])}.')
for c, v in enumerate(gols):
    print(f'=> Na partida {c}, fez {v} gols.')

print(f'Foi um total de {campeonato["total"]} gols.')