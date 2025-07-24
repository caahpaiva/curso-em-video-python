'''
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um
sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

jogadores = []
jogador = {}
gols = []
resposta = 'S'

while resposta in 'S':
    jogador.clear()      
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    total = 0
    for i in range(0,partidas):     
        gol  = int(input(f'Quantos gols na partida {i+1}? '))
        gols.append(gol)
        total += gol
    jogador['gols'] = gols[:]
    jogador['total'] = total
    jogadores.append(jogador.copy())
    while True:
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

print('-='*30)
print(jogadores)
print('-='*30)

print(f'cod nome   gols  total')
print('-'*30)

for c, va in enumerate(jogadores):
    print(f'{c:>3} ', end='')
    for v in va.values():
        print(f'{str(v):<15} ', end='')
    print()


view = 0

while view != 999:   
    print('-'*30)
    view = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if view < len(jogadores):       
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[view]["nome"]}: ')
        for i, g in enumerate(jogadores[view] ["gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')
    else: 
         print(f'ERRO! Não existe jogador com código {view}!')



print('<< VOLTE SEMPRE >>')
